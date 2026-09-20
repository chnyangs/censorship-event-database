#!/usr/bin/env python3
"""Freeze all distinct final OONI metadata rows, then fetch immutable raw records.

Anomaly and non-anomaly rows are retained alike. Identity checks and extracted
OONI test fields are machine evidence preparation, never censorship adjudication.
"""
from __future__ import annotations

import argparse
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path
import re
import threading
import time
import urllib.error
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
LIMITS = {'workers':3,'minimum_request_start_interval_seconds':1.0,'max_attempts_per_url':2,
          'timeout_seconds':25,'max_response_bytes':8_000_000,'max_retry_after_seconds':30}
IDENTITY_FIELDS = ('report_id','input','probe_cc','probe_asn','test_name','measurement_start_time')


def now():return datetime.now(timezone.utc).isoformat().replace('+00:00','Z')
def sha(raw):return 'sha256:'+hashlib.sha256(raw).hexdigest()
def canonical(value):return json.dumps(value,sort_keys=True,separators=(',',':'),ensure_ascii=False)
def write_json(path,value):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(value,indent=2,sort_keys=True,ensure_ascii=False)+'\n')


def safe_component(value):
    return isinstance(value,str) and bool(re.fullmatch(r'[A-Za-z0-9_.-]+',value)) and value not in {'.','..'}


def locator_error(url,metadata=None):
    if not isinstance(url,str):return 'measurement_url_missing'
    try:
        parts=urllib.parse.urlsplit(url)
        port=parts.port
    except ValueError:return 'measurement_url_malformed'
    if parts.scheme!='https' or parts.hostname!='api.ooni.io' or port not in (None,443) or parts.username or parts.password:
        return 'measurement_url_outside_official_https_host'
    if parts.path!='/api/v1/raw_measurement' or parts.fragment:return 'measurement_url_not_raw_endpoint'
    query=urllib.parse.parse_qs(parts.query,keep_blank_values=True)
    if set(query)!={'measurement_uid'} or len(query['measurement_uid'])!=1 or not query['measurement_uid'][0]:
        return 'measurement_url_missing_unique_uid'
    if metadata and metadata.get('measurement_uid') and metadata['measurement_uid']!=query['measurement_uid'][0]:
        return 'measurement_url_uid_disagrees_with_metadata'
    return None


def load_metadata_bundle(directory,role):
    names=('manifest.json','summary.json','query_summaries.json')
    if not all((directory/name).is_file() for name in names):
        raise ValueError(f'Final {role} metadata summary/query_summaries are not present; wait for metadata run completion')
    raw={name:(directory/name).read_bytes() for name in names}
    plan,summary,queries=(json.loads(raw[name]) for name in names)
    if not isinstance(queries,list):raise ValueError('Final query summaries must be a list')
    actual={}
    for item in queries:
        query=item.get('query') if isinstance(item,dict) else None
        qid=query.get('query_id') if isinstance(query,dict) else None
        if not safe_component(qid) or qid in actual:raise ValueError('Malformed or duplicate final query identity')
        complete=item.get('pagination_complete')
        if not isinstance(complete,bool) or item.get('status')!=('complete' if complete else 'incomplete'):
            raise ValueError('Query completion accounting is inconsistent')
        actual[qid]=item
    return raw,plan,summary,actual


def freeze(source,out,expected_queries=624,retry_dir=None):
    source=source.resolve();out=out.resolve()
    if out.exists():raise ValueError('Refusing to overwrite frozen raw-measurement protocol')
    raw_inputs,plan,summary,actual=load_metadata_bundle(source,'primary')
    expected=plan['query_count']
    if expected!=expected_queries or summary.get('query_count')!=expected or len(actual)!=expected:
        raise ValueError('Metadata run has not finalized the entire declared query frame')
    complete_count=sum(item['pagination_complete'] for item in actual.values())
    if (summary.get('status')!=('complete' if complete_count==expected else 'partial')
            or summary.get('complete_queries')!=complete_count
            or summary.get('failed_or_incomplete_queries')!=expected-complete_count):
        raise ValueError('Metadata final completion accounting is inconsistent')
    declared={q['query_id']:q for q in plan['queries']}
    if len(plan['queries'])!=expected or len(declared)!=expected or set(declared)!=set(actual):
        raise ValueError('Final query identities differ from frozen metadata frame')
    runs=[('primary',source,raw_inputs,actual)]
    retry_plan=retry_summary=None;retry_actual={}
    if retry_dir is not None:
        retry_dir=retry_dir.resolve()
        retry_raw,retry_plan,retry_summary,retry_actual=load_metadata_bundle(retry_dir,'retry')
        if retry_plan.get('status')!='frozen_before_retry_requests':raise ValueError('Retry manifest was not frozen before requests')
        if Path(retry_plan['source_directory']).resolve()!=source:raise ValueError('Retry source directory mismatch')
        for key,name in (('source_manifest_sha256','manifest.json'),
                         ('source_query_summaries_sha256','query_summaries.json'),
                         ('source_summary_sha256','summary.json')):
            if retry_plan.get(key)!=sha(raw_inputs[name]):raise ValueError('Retry parent source hash mismatch')
        incomplete={qid for qid,item in actual.items() if not item['pagination_complete']}
        retry_queries=retry_plan.get('queries',[])
        retry_declared={q['query_id']:q for q in retry_queries}
        if (retry_plan.get('retry_query_count')!=len(incomplete) or len(retry_queries)!=len(incomplete)
                or set(retry_declared)!=incomplete or set(retry_actual)!=incomplete):
            raise ValueError('Retry set must contain every and only primary pagination-incomplete query')
        for qid,item in retry_actual.items():
            if retry_declared[qid]!=declared[qid] or item['query']!=declared[qid]:
                raise ValueError('Retry query identity mismatch')
        retry_complete=sum(item['pagination_complete'] for item in retry_actual.values())
        if (retry_summary.get('retry_query_count')!=len(incomplete)
                or retry_summary.get('completed_retries')!=retry_complete
                or retry_summary.get('still_incomplete')!=len(incomplete)-retry_complete
                or retry_summary.get('status')!=('complete' if retry_complete==len(incomplete) else 'partial')):
            raise ValueError('Retry final completion accounting is inconsistent')
        runs.append(('retry',retry_dir,retry_raw,retry_actual))
    inputs=[];distinct={};appearances=0
    for role,directory,run_inputs,run_queries in runs:
        inputs.extend({'path':str(directory/name),'sha256':sha(raw),'metadata_run':role}
                      for name,raw in run_inputs.items())
        for qid,item in sorted(run_queries.items()):
            if item['query']!=declared[qid]:raise ValueError('Query identity mismatch')
            query_dir=directory/'captures'/qid;saved=query_dir/'summary.json';saved_raw=saved.read_bytes()
            if json.loads(saved_raw)!=item:raise ValueError('Final query summary differs from preserved per-query summary')
            inputs.append({'path':str(saved),'sha256':sha(saved_raw),'metadata_run':role})
            for page in item.get('pages',[]):
                filename=page['body_file']
                if not safe_component(filename):raise ValueError('Unsafe metadata capture filename')
                path=query_dir/filename;raw=path.read_bytes()
                if sha(raw)!=page['body_sha256']:raise ValueError('Metadata response-body hash mismatch')
                inputs.append({'path':str(path),'sha256':sha(raw),'metadata_run':role})
            rows=item.get('measurement_rows')
            if not isinstance(rows,list) or item.get('retrieved_rows')!=len(rows):raise ValueError('Metadata row accounting mismatch')
            for row in rows:
                if not isinstance(row,dict):raise ValueError('Metadata row is not an object')
                appearances+=1
                row_id=hashlib.sha256(canonical(row).encode()).hexdigest()
                if row_id not in distinct:
                    distinct[row_id]={'metadata_row_id':row_id,'metadata':row,'query_references':[],
                                      'locator_validation_error':locator_error(row.get('measurement_url'),row)}
                distinct[row_id]['query_references'].append({'query_id':qid,'event_id':item['query']['event_id'],
                        'metadata_run':role,'query_summary_path':str(saved),'query_summary_sha256':sha(saved_raw),
                        'metadata_query_status':item['status'],'metadata_pagination_complete':item['pagination_complete']})
    effective=[]
    for qid,item in sorted(actual.items()):
        use_retry=qid in retry_actual and retry_actual[qid]['pagination_complete']
        selected=retry_actual[qid] if use_retry else item
        selected_dir=retry_dir if use_retry else source
        effective.append({'query_id':qid,'selected_metadata_run':'retry' if use_retry else 'primary',
                          'query_summary_path':str(selected_dir/'captures'/qid/'summary.json'),
                          'status':selected['status'],'pagination_complete':selected['pagination_complete'],
                          'retry_available':qid in retry_actual})
    effective_complete=sum(item['pagination_complete'] for item in effective)
    rows=[distinct[k] for k in sorted(distinct)]
    urls={row['metadata'].get('measurement_url') for row in rows if row['locator_validation_error'] is None}
    manifest={'procedure_version':'ooni-raw-all-metadata-v1','status':'frozen_before_raw_requests',
              'frozen_at_utc':now(),'metadata_source_directory':str(source),
              'metadata_retry_directory':str(retry_dir) if retry_dir is not None else None,
              'metadata_queries_finalized':expected,'metadata_primary_frame_status':summary['status'],
              'metadata_frame_status':'complete' if effective_complete==expected else 'partial',
              'metadata_complete_queries_after_retry':effective_complete,
              'metadata_incomplete_queries_after_retry':expected-effective_complete,
              'metadata_effective_query_summaries':effective,
              'metadata_retry_frame_status':retry_summary['status'] if retry_summary else None,
              'metadata_row_appearances':appearances,'distinct_metadata_rows':len(rows),'distinct_raw_urls':len(urls),
              'invalid_locator_rows':sum(r['locator_validation_error'] is not None for r in rows),
              'anomaly_flag_counts':dict(Counter(str(r['metadata'].get('anomaly')) for r in rows)),
              'selection':'Every distinct canonical metadata row from every final primary and optional retry query summary, including incomplete queries and anomaly/non-anomaly/missing-flag rows. No outcome filtering. One URL may serve multiple distinct metadata rows; each is checked separately.',
              'retry_overlay_policy':'A pagination-complete retry updates the effective query summary only. All rows from both runs are retained and canonical-full-row deduplicated, with both provenances; no primary rows are discarded even if absent in the retry. Otherwise the primary incomplete summary remains effective and both runs contribute rows.',
              'identity_policy':'Compare report_id, exact input URL, normalized country/ASN, test_name and UTC-normalized measurement_start_time. Legacy OONI raw timestamps without an offset are interpreted as UTC explicitly. Raw measurement_uid is checked if exposed; its absence is recorded, not fabricated.',
              'limits':LIMITS,'collector_sha256':sha(Path(__file__).read_bytes()),
              'metadata_source_hashes':inputs,'metadata_rows':rows,'censorship_finding':None,
              'human_review_complete':False,'conclusion':'Raw retrieval and identity validation are not a blocking/nonblocking conclusion.'}
    out.mkdir(parents=True)
    write_json(out/'manifest.json',manifest)
    (out/'collector_source.py').write_bytes(Path(__file__).read_bytes())
    for role,_,run_inputs,_ in runs:
        prefix='metadata_' if role=='primary' else 'retry_metadata_'
        for name,raw in run_inputs.items():(out/(prefix+name)).write_bytes(raw)
    write_json(out/'freeze_hashes.json',{'files':{p.name:sha(p.read_bytes()) for p in out.iterdir() if p.is_file()}})
    return manifest


class RateLimiter:
    def __init__(self,interval):self.interval,self.next_start,self.lock=interval,0.0,threading.Lock()
    def wait(self):
        with self.lock:
            current=time.monotonic();delay=max(0.0,self.next_start-current)
            if delay:time.sleep(delay)
            self.next_start=time.monotonic()+self.interval


class SameHostRedirect(urllib.request.HTTPRedirectHandler):
    def __init__(self,url):
        parts=urllib.parse.urlsplit(url)
        self.hostname=parts.hostname
        self.uid=urllib.parse.parse_qs(parts.query,keep_blank_values=True).get('measurement_uid')
    def redirect_request(self,req,fp,code,msg,headers,newurl):
        try:
            parts=urllib.parse.urlsplit(newurl)
            query=urllib.parse.parse_qs(parts.query,keep_blank_values=True)
            valid=(parts.scheme=='https' and parts.hostname==self.hostname and parts.port in (None,443)
                   and not parts.username and not parts.password and not parts.fragment
                   and parts.path=='/api/v1/raw_measurement' and set(query)=={'measurement_uid'}
                   and len(query['measurement_uid'])==1 and query['measurement_uid']==self.uid)
        except ValueError:valid=False
        if not valid:
            raise urllib.error.HTTPError(req.full_url,code,'Redirect changed host/security/raw path/measurement UID',headers,fp)
        return super().redirect_request(req,fp,code,msg,headers,newurl)


def request(url,limits,limiter):
    limiter.wait();record={'requested_url':url,'started_at_utc':now(),'http_status':None,'final_url':url,'headers':{},'transport_error':None,'truncated':False};raw=b''
    try:
        req=urllib.request.Request(url,headers={'User-Agent':'CensorshipCorpusRawReview/1.0 (bounded read-only research)','Accept':'application/json'})
        with urllib.request.build_opener(SameHostRedirect(url)).open(req,timeout=limits['timeout_seconds']) as response:
            record.update(http_status=response.status,final_url=response.url,headers=dict(response.headers.items()))
            raw=response.read(limits['max_response_bytes']+1)
    except urllib.error.HTTPError as exc:
        record.update(http_status=exc.code,transport_error=str(exc),headers=dict(exc.headers.items()))
        raw=exc.read(limits['max_response_bytes']+1)
    except (OSError,TimeoutError,urllib.error.URLError) as exc:record['transport_error']=f'{type(exc).__name__}: {exc}'
    if len(raw)>limits['max_response_bytes']:
        record.update(truncated=True,transport_error='Body exceeds frozen byte cap; retained prefix is incomplete')
    record['finished_at_utc']=now()
    return record,raw


def time_value(value):
    if not isinstance(value,str):return None
    try:
        parsed=datetime.fromisoformat(value.replace('Z','+00:00'))
        if parsed.tzinfo is None:parsed=parsed.replace(tzinfo=timezone.utc)
        return parsed.astimezone(timezone.utc)
    except ValueError:return None


def asn_value(value):
    if isinstance(value,bool):return None
    match=re.fullmatch(r'(?:AS)?([0-9]+)',str(value),re.I)
    return int(match.group(1)) if match else None


def validate_identity(raw,metadata):
    if not isinstance(raw,dict):return {'valid':False,'errors':['Raw response is not a measurement object'],'raw_uid_status':'unavailable'}
    errors=[]
    for field in IDENTITY_FIELDS:
        actual,expected=raw.get(field),metadata.get(field)
        if field=='measurement_start_time':actual,expected=time_value(actual),time_value(expected)
        elif field=='probe_asn':actual,expected=asn_value(actual),asn_value(expected)
        elif field=='probe_cc':actual,expected=(v.upper() if isinstance(v,str) else None for v in (actual,expected))
        elif not isinstance(actual,str) or not isinstance(expected,str):actual=None
        if actual is None or expected is None or actual=='' or expected=='' or actual!=expected:errors.append('Identity mismatch or missing '+field)
    uid=raw.get('measurement_uid');expected_uid=metadata.get('measurement_uid') or urllib.parse.parse_qs(urllib.parse.urlsplit(metadata['measurement_url']).query)['measurement_uid'][0]
    if uid is not None and uid!=expected_uid:errors.append('Identity mismatch measurement_uid')
    return {'valid':not errors,'errors':errors,'raw_uid_status':'matched' if uid==expected_uid else 'not_exposed_by_raw' if uid is None else 'mismatch',
            'legacy_naive_raw_time_interpreted_as_utc':isinstance(raw.get('measurement_start_time'),str) and time_value(raw.get('measurement_start_time')) is not None and not re.search(r'(Z|[+-]\d{2}:?\d{2})$',raw['measurement_start_time'])}


def review_fields(raw):
    keys=raw.get('test_keys')
    failures=[]
    def walk(value,path):
        if isinstance(value,dict):
            for k,v in value.items():
                current=path+'/'+k
                if 'failure' in k.lower():failures.append({'json_pointer':current,'value':v})
                else:walk(v,current)
        elif isinstance(value,list):
            for i,v in enumerate(value):walk(v,path+'/'+str(i))
    walk(keys,'/test_keys')
    return {'identity_fields':{k:raw.get(k) for k in IDENTITY_FIELDS},'test_keys':keys,
            'test_helpers':raw.get('test_helpers'),'failure_fields':failures,
            'test_keys_is_object':isinstance(keys,dict),'censorship_finding':None,'human_review_complete':False,
            'interpretation':'Values such as blocking/accessible/anomaly are original automated test outputs, not this project\'s adjudication.'}


def collect_url(url,rows,out,limits,limiter,fetch=request):
    request_id=hashlib.sha256(url.encode()).hexdigest();root=out/'captures'/request_id
    result={'measurement_url':url,'request_id':request_id,'metadata_row_ids':[r['metadata_row_id'] for r in rows],
            'status':'retrieval_gap','attempts':[],'identity_checks':[],'raw_review_path':None,'censorship_finding':None}
    for attempt in range(1,limits['max_attempts_per_url']+1):
        record,body=fetch(url,limits,limiter)
        dest=root/f'attempt_{attempt}';dest.mkdir(parents=True,exist_ok=False);(dest/'response.body').write_bytes(body)
        record.update(body_path=str(dest/'response.body'),body_sha256=sha(body),body_bytes=len(body))
        write_json(dest/'capture.json',record);result['attempts'].append(record)
        if record['http_status']==200 and not record['transport_error'] and not record.get('truncated'):
            try:
                raw=json.loads(body)
                checks=[{'metadata_row_id':r['metadata_row_id'],**validate_identity(raw,r['metadata'])} for r in rows]
                result['identity_checks']=checks
                if all(c['valid'] for c in checks):
                    review=review_fields(raw);write_json(root/'review_fields.json',review)
                    result.update(status='retrieved_identity_valid',raw_review_path=str(root/'review_fields.json'),test_keys_is_object=review['test_keys_is_object'])
                    break
                result['status']='retrieved_identity_mismatch'
            except (ValueError,TypeError,KeyError) as exc:
                record['parse_or_validation_error']=str(exc);write_json(dest/'capture.json',record)
        headers={k.lower():v for k,v in record.get('headers',{}).items()}
        if record['http_status'] in (429,503) and attempt<limits['max_attempts_per_url']:
            delay=headers.get('retry-after')
            if not delay:
                result['retry_stop_reason']='Missing Retry-After; no automatic retry';break
            try:delay=float(delay)
            except ValueError:
                result['retry_stop_reason']='Unparsed Retry-After; no automatic retry';break
            if not math.isfinite(delay) or delay>limits['max_retry_after_seconds'] or delay<0:
                result['retry_stop_reason']='Retry-After outside bounded wait; no automatic retry';break
            time.sleep(delay)
    write_json(root/'result.json',result)
    return result


def run(protocol,out,fetch=request):
    protocol=protocol.resolve()
    out=out.resolve()
    if out.exists():raise ValueError('Refusing to overwrite raw-measurement run')
    hashes=json.loads((protocol/'freeze_hashes.json').read_text())
    for name,expected in hashes['files'].items():
        if not safe_component(name) or sha((protocol/name).read_bytes())!=expected:raise ValueError('Frozen raw protocol hash mismatch')
    manifest=json.loads((protocol/'manifest.json').read_text())
    if manifest['collector_sha256']!=sha(Path(__file__).read_bytes()):raise ValueError('Collector differs from frozen version')
    for reference in manifest['metadata_source_hashes']:
        if sha(Path(reference['path']).read_bytes())!=reference['sha256']:raise ValueError('Metadata source changed after freeze')
    groups={}
    invalid=[]
    for row in manifest['metadata_rows']:
        if row['locator_validation_error'] is not None:invalid.append({'metadata_row_id':row['metadata_row_id'],'status':'invalid_locator_gap','reason':row['locator_validation_error']})
        else:groups.setdefault(row['metadata']['measurement_url'],[]).append(row)
    out.mkdir(parents=True)
    write_json(out/'execution_manifest.json',{'created_before_requests_at_utc':now(),'protocol_sha256':sha((protocol/'manifest.json').read_bytes()),'frozen_distinct_metadata_rows':len(manifest['metadata_rows']),'frozen_distinct_raw_urls':len(groups),'limits':manifest['limits'],'human_review_complete':False})
    limiter=RateLimiter(manifest['limits']['minimum_request_start_interval_seconds'])
    with ThreadPoolExecutor(max_workers=manifest['limits']['workers']) as pool:
        results=list(pool.map(lambda item:collect_url(item[0],item[1],out,manifest['limits'],limiter,fetch),sorted(groups.items())))
    summary={'completed_at_utc':now(),'status':'raw_retrieval_complete' if all(r['status']=='retrieved_identity_valid' for r in results) and not invalid else 'raw_retrieval_partial',
             'frozen_metadata_rows':len(manifest['metadata_rows']),'frozen_raw_urls':len(groups),'raw_urls_attempted':len(results),
             'url_status_counts':dict(Counter(r['status'] for r in results)),
             'identity_valid_metadata_rows':sum(c['valid'] for r in results for c in r['identity_checks']),
             'invalid_locator_rows':len(invalid),'http_attempts':sum(len(r['attempts']) for r in results),
             'censorship_finding':None,'human_review_complete':False,
             'interpretation':'Every frozen valid raw locator was attempted. Retrieval completeness is not metadata-frame completeness, representativeness, independent probe coverage or a censorship conclusion.'}
    write_json(out/'results.json',results);write_json(out/'invalid_locator_rows.json',invalid);write_json(out/'summary.json',summary)
    return summary


def main():
    parser=argparse.ArgumentParser(description=__doc__);sub=parser.add_subparsers(dest='command',required=True)
    freezing=sub.add_parser('freeze');freezing.add_argument('--source-dir',type=Path,default=ROOT/'analysis/evidence_repairs/l0_ooni_daily_v1');freezing.add_argument('--out-dir',type=Path,required=True);freezing.add_argument('--expected-queries',type=int,default=624);freezing.add_argument('--retry-dir',type=Path)
    running=sub.add_parser('run');running.add_argument('--protocol',type=Path,required=True);running.add_argument('--out-dir',type=Path,required=True)
    args=parser.parse_args();result=freeze(args.source_dir,args.out_dir,args.expected_queries,args.retry_dir) if args.command=='freeze' else run(args.protocol,args.out_dir)
    print(json.dumps({k:v for k,v in result.items() if k not in {'metadata_source_hashes','metadata_rows','metadata_effective_query_summaries'}},indent=2))


if __name__=='__main__':main()
