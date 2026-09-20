#!/usr/bin/env python3
"""Freeze public S3 listings for unresolved OONI UIDs, then bounded stream retrieval.

Only exact-UID, metadata-identity-matching raw records are retained. Missing
records, incomplete prefixes and transport failures remain gaps, never negatives.
"""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime
import gzip
import hashlib
import json
from pathlib import Path
import re
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
import zlib

import collect_ooni_raw_measurements as raw_api

BUCKET = 'ooni-data-eu-fra'
ORIGIN = 'https://ooni-data-eu-fra.s3.eu-central-1.amazonaws.com'
LIMITS = {'max_compressed_bytes':100_000_000,'minimum_request_start_interval_seconds':1.0,
          'max_attempts_per_object':1,'max_attempts_per_listing_page':1,'timeout_seconds':30,
          'max_listing_pages_per_prefix':4,'max_listing_response_bytes':2_000_000,
          'max_prefixes':24,'max_objects':100,'max_json_line_bytes':8_000_000,
          'max_uncompressed_bytes_per_object':200_000_000,
          'max_retained_matching_bytes':100_000_000}
sha, now, write_json = raw_api.sha, raw_api.now, raw_api.write_json


def require(condition,message):
    if not condition:raise ValueError(message)


def file_reference(path):
    path=path.resolve();return {'path':str(path),'sha256':sha(path.read_bytes())}


def uid_prefix(metadata):
    uid=metadata.get('measurement_uid')
    match=re.fullmatch(r'(\d{8})(\d{2})(\d{4})\.\d+_ET_webconnectivity_[0-9a-f]+',uid or '')
    require(match is not None,'UID outside declared ET/web_connectivity modern format')
    datetime.strptime(''.join(match.groups()),'%Y%m%d%H%M%S')
    require(metadata.get('probe_cc')=='ET' and metadata.get('test_name')=='web_connectivity','UID and metadata country/test disagree')
    return f'raw/{match[1]}/{match[2]}/ET/webconnectivity/'


def select_unresolved(protocol,api_run):
    required=[protocol/'manifest.json',protocol/'freeze_hashes.json',api_run/'summary.json',
              api_run/'results.json',api_run/'execution_manifest.json']
    require(all(p.is_file() for p in required),'Wait for final raw API summary/results before S3 selection')
    references=[file_reference(p) for p in required]
    manifest=json.loads(required[0].read_text())
    frozen=json.loads(required[1].read_text())
    for name,expected in frozen['files'].items():
        require(raw_api.safe_component(name) and sha((protocol/name).read_bytes())==expected,'Raw API protocol hash mismatch')
    summary=json.loads(required[2].read_text());results=json.loads(required[3].read_text())
    execution=json.loads(required[4].read_text())
    require(execution['protocol_sha256']==sha(required[0].read_bytes()),'API execution and protocol differ')
    require(summary['status'] in {'raw_retrieval_complete','raw_retrieval_partial'},'API run is not final')
    groups={}
    for row in manifest['metadata_rows']:
        if row['locator_validation_error'] is None:groups.setdefault(row['metadata']['measurement_url'],[]).append(row)
    by_url={r['measurement_url']:r for r in results}
    require(len(results)==len(by_url) and set(by_url)==set(groups),'API results do not cover frozen URL frame')
    require(summary['raw_urls_attempted']==summary['frozen_raw_urls']==len(groups),'API URL accounting mismatch')
    require(summary['url_status_counts']==dict(Counter(r['status'] for r in results)),'API status accounting mismatch')
    selected=[]
    for url,result in sorted(by_url.items()):
        require(result['status'] in {'retrieval_gap','retrieved_identity_mismatch','retrieved_identity_valid'},'Unknown API result status')
        directory=api_run/'captures'/hashlib.sha256(url.encode()).hexdigest()
        saved=directory/'result.json'
        require(json.loads(saved.read_text())==result,'API aggregate and preserved result differ')
        references.append(file_reference(saved))
        for attempt in result['attempts']:
            body=Path(attempt['body_path']).resolve()
            require(body.is_relative_to(directory.resolve()) and sha(body.read_bytes())==attempt['body_sha256'],'API body provenance mismatch')
            references.append(file_reference(body))
            capture=body.parent/'capture.json'
            require(json.loads(capture.read_text())==attempt,'API attempt metadata mismatch')
            references.append(file_reference(capture))
        expected_ids={r['metadata_row_id'] for r in groups[url]}
        require(set(result['metadata_row_ids'])==expected_ids,'API result metadata IDs mismatch')
        if result['status']=='retrieved_identity_valid':
            require({c['metadata_row_id'] for c in result['identity_checks'] if c['valid']}==expected_ids,'API valid status lacks identity checks')
            continue
        for row in groups[url]:
            prefix=uid_prefix(row['metadata'])
            selected.append({**row,'s3_prefix':prefix,'api_retrieval_status':result['status']})
    require(len({r['s3_prefix'] for r in selected})<=LIMITS['max_prefixes'],'Declared prefix count exceeds bound')
    return selected,references


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self,req,fp,code,msg,headers,newurl):
        raise urllib.error.HTTPError(req.full_url,code,'Redirect refused for frozen S3 request',headers,fp)


def open_url(url,headers=None):
    parts=urllib.parse.urlsplit(url)
    require(parts.scheme=='https' and parts.netloc==urllib.parse.urlsplit(ORIGIN).netloc and not parts.fragment,'Outside official S3 origin')
    return urllib.request.build_opener(NoRedirect()).open(urllib.request.Request(url,headers={
        'User-Agent':'CensorshipCorpusS3Review/1.0 (bounded read-only research)',
        'Accept-Encoding':'identity',**(headers or {})}),timeout=LIMITS['timeout_seconds'])


def listing_url(prefix,token=None):
    params={'list-type':'2','prefix':prefix,'max-keys':'1000'}
    if token is not None:params['continuation-token']=token
    return ORIGIN+'/?'+urllib.parse.urlencode(params)


def parse_listing(body,prefix,token=None):
    require(b'<!DOCTYPE' not in body.upper(),'DTD not permitted in listing XML')
    root=ET.fromstring(body);ns='{http://s3.amazonaws.com/doc/2006-03-01/}'
    require(root.tag==ns+'ListBucketResult','Unexpected S3 XML root/namespace')
    def get(name):return root.findtext(ns+name)
    require(get('Name')==BUCKET and get('Prefix')==prefix,'Listing bucket/prefix mismatch')
    require(get('ContinuationToken') in (None,'') if token is None else get('ContinuationToken')==token,'Listing continuation-token mismatch')
    require(get('EncodingType') in (None,'') and not root.findall(ns+'CommonPrefixes'),'Unexpected encoded or grouped listing')
    truncated=get('IsTruncated');require(truncated in {'true','false'},'Missing explicit pagination state')
    next_token=get('NextContinuationToken')
    require(bool(next_token) if truncated=='true' else next_token in (None,''),'Inconsistent next-page token')
    objects=[]
    for node in root.findall(ns+'Contents'):
        key=node.findtext(ns+'Key') or '';size=node.findtext(ns+'Size') or '';etag=node.findtext(ns+'ETag')
        require(key.startswith(prefix) and raw_api.safe_component(key[len(prefix):]),'Object outside exact prefix or unsafe object path')
        require(re.fullmatch(r'\d+',size) is not None,'Invalid listed object size')
        require(isinstance(etag,str) and re.fullmatch(r'"[A-Za-z0-9-]+"',etag) is not None,'Missing or unsafe listed ETag')
        objects.append({'key':key,'content_length':int(size),'etag':etag,'last_modified':node.findtext(ns+'LastModified'),
                        'selected_jsonl_gzip':key.endswith('.jsonl.gz')})
    require(get('KeyCount')==str(len(objects)) and len(objects)<=1000,'Listing key count mismatch')
    require([o['key'] for o in objects]==sorted({o['key'] for o in objects}),'Duplicate or unsorted object keys')
    return objects,next_token


def list_prefix(prefix,out,limiter,opener=open_url):
    records=[];objects=[];token=None;seen=set();error=None
    for index in range(LIMITS['max_listing_pages_per_prefix']):
        url=listing_url(prefix,token);limiter.wait();body=b''
        record={'requested_url':url,'started_at_utc':now(),'http_status':None,'error':None}
        try:
            with opener(url) as response:
                record.update(http_status=response.status,headers=dict(response.headers.items()),final_url=response.url)
                require(response.status==200 and response.url==url,'Listing HTTP status/final URL mismatch')
                body=response.read(LIMITS['max_listing_response_bytes']+1)
                require(len(body)<=LIMITS['max_listing_response_bytes'],'Listing response byte cap exceeded')
            page,following=parse_listing(body,prefix,token)
            require(not objects or not page or objects[-1]['key']<page[0]['key'],'Overlapping or regressing listing pages')
            objects.extend(page)
            if following is not None:
                require(following not in seen,'Repeated pagination token');seen.add(following)
            token=following
        except (OSError,ValueError,ET.ParseError) as exc:
            error=record['error']=f'{type(exc).__name__}: {exc}'
            if isinstance(exc,urllib.error.HTTPError):record.update(http_status=exc.code,headers=dict(exc.headers.items()))
        record.update(finished_at_utc=now(),body_sha256=sha(body),body_bytes=len(body))
        dest=out/f'page_{index+1}';dest.mkdir(parents=True,exist_ok=False)
        (dest/'response.xml').write_bytes(body);write_json(dest/'capture.json',record);records.append(record)
        if error or token is None:break
    if token is not None and not error:error='Frozen listing-page cap reached'
    return {'prefix':prefix,'pagination_complete':error is None,'error':error,'objects':objects,'pages':records}


def freeze(protocol,api_run,out,opener=open_url):
    protocol,api_run,out=(p.resolve() for p in (protocol,api_run,out))
    require(not out.exists(),'Refusing to overwrite S3 protocol')
    selected,inputs=select_unresolved(protocol,api_run)
    prefixes=sorted({r['s3_prefix'] for r in selected})
    selection={'selected_at_utc':now(),'selection_rule':'Every metadata row tied to an unresolved raw-API URL; no anomaly/outcome filtering.',
               'selected_rows':selected,'prefixes':prefixes,'source_hashes':inputs,'limits':LIMITS,
               'collector_sha256':sha(Path(__file__).read_bytes()),'identity_helper_sha256':sha(Path(raw_api.__file__).read_bytes()),
               'official_format_source':'https://github.com/ooni/data',
               'official_reader_source':'https://github.com/ooni/data/blob/main/oonidata/src/oonidata/dataclient.py',
               'official_uid_source':'https://github.com/ooni/api/blob/master/newapi/ooniapi/probe_services.py',
               'uid_prefix_semantics':'The official receive_measurement handler derives both its hourly spool directory and measurement_uid timestamp from the same UTC receive/upload time. The official dataclient parses modern JSONL filename timestamps at hour precision. This procedure uses that UID hour, not measurement_start_time.',
               'prefix_limit':'Only the receive-time hour encoded in each UID is enumerated. Missing objects or alternate layouts remain retrieval gaps.'}
    out.mkdir(parents=True);write_json(out/'selection_before_listing.json',selection)
    limiter=raw_api.RateLimiter(LIMITS['minimum_request_start_interval_seconds'])
    listings=[list_prefix(prefix,out/'listings'/hashlib.sha256(prefix.encode()).hexdigest(),limiter,opener) for prefix in prefixes]
    objects=[o for listing in listings for o in listing['objects'] if o['selected_jsonl_gzip']]
    for listing in listings:
        listing['candidate_jsonl_gzip_objects']=sum(o['selected_jsonl_gzip'] for o in listing['objects'])
        listing['selected_uid_count']=len({r['metadata']['measurement_uid'] for r in selected if r['s3_prefix']==listing['prefix']})
    require(len({o['key'] for o in objects})==len(objects),'Duplicate frozen object identity')
    total=sum(o['content_length'] for o in objects)
    complete=all(item['pagination_complete'] for item in listings)
    eligible=complete and total<=LIMITS['max_compressed_bytes'] and len(objects)<=LIMITS['max_objects']
    manifest={**selection,'status':'frozen_before_object_downloads','frozen_at_utc':now(),'listings':listings,
              'objects':objects,'object_count':len(objects),'total_compressed_content_length':total,
              'listing_complete':complete,'download_eligible':eligible,'object_downloads_performed':0,
              'every_selected_prefix_has_jsonl_gzip_object':all(item['candidate_jsonl_gzip_objects']>0 for item in listings),
              'empty_jsonl_gzip_prefixes':[item['prefix'] for item in listings if item['candidate_jsonl_gzip_objects']==0],
              'censorship_finding':None,'human_review_complete':False,
              'interpretation':'Listed Size is frozen as expected Content-Length and checked before streaming. ETag binds the GET through If-Match; it is not assumed to be a cryptographic body hash. Unmatched UIDs remain gaps.'}
    write_json(out/'manifest.json',manifest)
    (out/'collector_source.py').write_bytes(Path(__file__).read_bytes())
    (out/'collect_ooni_raw_measurements.py').write_bytes(Path(raw_api.__file__).read_bytes())
    write_json(out/'freeze_hashes.json',{'files':{p.relative_to(out).as_posix():sha(p.read_bytes()) for p in sorted(out.rglob('*')) if p.is_file()}})
    return manifest


class HashingReader:
    def __init__(self,response,limit):self.response,self.limit,self.size,self.hasher=response,limit,0,hashlib.sha256()
    def read(self,size=-1):
        remaining=self.limit-self.size
        raw=self.response.read(min(size,remaining+1) if size>=0 else remaining+1)
        self.size+=len(raw);self.hasher.update(raw)
        require(self.size<=self.limit,'Compressed object exceeds frozen size')
        return raw


def scan_object(response,obj,selected,limits=LIMITS,audit=None):
    headers={k.lower():v for k,v in response.headers.items()}
    require(response.status==200,'Object HTTP status is not 200')
    require(headers.get('content-length')==str(obj['content_length']),'Object Content-Length differs from frozen listing')
    require(headers.get('etag')==obj['etag'],'Object ETag differs from frozen listing')
    reader=HashingReader(response,obj['content_length']);matches=[];mismatches=[];line_count=0;expanded=0;retained=0
    try:
        with gzip.GzipFile(fileobj=reader,mode='rb') as stream:
            while True:
                line=stream.readline(limits['max_json_line_bytes']+1)
                if not line:break
                require(len(line)<=limits['max_json_line_bytes'],'JSONL line cap exceeded')
                expanded+=len(line);require(expanded<=limits['max_uncompressed_bytes_per_object'],'Uncompressed object byte cap exceeded')
                line_count+=1
                if not line.strip():continue
                record=json.loads(line);require(isinstance(record,dict),'JSONL record is not an object')
                uid=record.get('measurement_uid')
                if not isinstance(uid,str) or uid not in selected:continue
                checks=[{'metadata_row_id':r['metadata_row_id'],**raw_api.validate_identity(record,r['metadata'])} for r in selected[uid]]
                if all(c['valid'] for c in checks):
                    retained+=len(line);require(retained<=limits['max_retained_matching_bytes'],'Matching-record byte cap exceeded')
                    matches.append({'measurement_uid':uid,'line_number':line_count,'line_sha256':sha(line),
                                    'line':line,'identity_checks':checks,'review_fields':raw_api.review_fields(record)})
                else:mismatches.append({'measurement_uid':uid,'line_number':line_count,'line_sha256':sha(line),'identity_checks':checks})
        require(reader.size==obj['content_length'],'Compressed response ended before frozen size')
    finally:
        if audit is not None:audit.update(streamed_compressed_bytes=reader.size,
                                         streamed_compressed_prefix_sha256='sha256:'+reader.hasher.hexdigest())
    return {'compressed_body_sha256':'sha256:'+reader.hasher.hexdigest(),'compressed_bytes':reader.size,
            'uncompressed_bytes':expanded,'lines_scanned':line_count,'matches':matches,'identity_mismatches':mismatches}


def verify_protocol(protocol):
    for name,expected in json.loads((protocol/'freeze_hashes.json').read_text())['files'].items():
        path=(protocol/name).resolve()
        require(path.is_relative_to(protocol) and sha(path.read_bytes())==expected,'Frozen S3 protocol hash mismatch')
    manifest=json.loads((protocol/'manifest.json').read_text())
    require(manifest['collector_sha256']==sha(Path(__file__).read_bytes()),'S3 collector changed after freeze')
    require(manifest['identity_helper_sha256']==sha(Path(raw_api.__file__).read_bytes()),'Identity helper changed after freeze')
    require(manifest['limits']==LIMITS,'S3 request limits changed')
    for ref in manifest['source_hashes']:require(sha(Path(ref['path']).read_bytes())==ref['sha256'],'API source changed after S3 freeze')
    total=sum(o['content_length'] for o in manifest['objects'])
    require(total==manifest['total_compressed_content_length'] and total<=LIMITS['max_compressed_bytes'],'Compressed total exceeds 100 MB or disagrees with freeze')
    require(manifest['download_eligible'] is True and manifest['listing_complete'] is True,'Incomplete or ineligible frozen S3 listing')
    require(len(manifest['objects'])==manifest['object_count']<=LIMITS['max_objects'],'Object count exceeds frozen bound')
    return manifest


def run(protocol,out,opener=open_url):
    protocol,out=protocol.resolve(),out.resolve();require(not out.exists(),'Refusing to overwrite S3 run')
    manifest=verify_protocol(protocol);selected={}
    for row in manifest['selected_rows']:selected.setdefault(row['metadata']['measurement_uid'],[]).append(row)
    out.mkdir(parents=True)
    write_json(out/'execution_manifest.json',{'created_before_object_requests_at_utc':now(),
               'protocol_sha256':sha((protocol/'manifest.json').read_bytes()),'limits':LIMITS,
               'selected_uids':sorted(selected),'object_count':len(manifest['objects']),
               'total_compressed_content_length':manifest['total_compressed_content_length']})
    limiter=raw_api.RateLimiter(LIMITS['minimum_request_start_interval_seconds']);results=[];found={};retained_bytes=0
    for obj in manifest['objects']:
        url=ORIGIN+'/'+urllib.parse.quote(obj['key'],safe='/');limiter.wait()
        capture={'key':obj['key'],'requested_url':url,'request_headers':{'If-Match':obj['etag']},
                 'started_at_utc':now(),'status':'retrieval_gap','error':None,'http_status':None}
        try:
            with opener(url,{'If-Match':obj['etag']}) as response:
                capture.update(http_status=response.status,headers=dict(response.headers.items()),final_url=response.url)
                require(response.url==url,'Object redirect changed frozen key')
                scanned=scan_object(response,obj,selected,audit=capture)
            matches=scanned.pop('matches');capture.update(scanned,status='stream_scanned')
            new_bytes=sum(len(m['line']) for m in matches)
            require(retained_bytes+new_bytes<=LIMITS['max_retained_matching_bytes'],'Campaign matching-record byte cap exceeded')
            retained_bytes+=new_bytes
            for match in matches:
                line=match.pop('line');key=hashlib.sha256(line).hexdigest();dest=out/'records'/key
                if not dest.exists():
                    dest.mkdir(parents=True);(dest/'measurement.jsonl').write_bytes(line)
                    write_json(dest/'review_fields.json',match['review_fields'])
                entry={k:v for k,v in match.items() if k!='review_fields'}
                entry.update(object_key=obj['key'],raw_record_path=str(dest/'measurement.jsonl'))
                found.setdefault(match['measurement_uid'],[]).append(entry)
        except (OSError,ValueError,EOFError,zlib.error) as exc:
            capture.update(status='retrieval_gap',error=f'{type(exc).__name__}: {exc}')
            if isinstance(exc,urllib.error.HTTPError):capture.update(http_status=exc.code,headers=dict(exc.headers.items()))
        capture['finished_at_utc']=now();results.append(capture)
        write_json(out/'objects'/(hashlib.sha256(obj['key'].encode()).hexdigest()+'.json'),capture)
    uid_results=[]
    for uid,rows in sorted(selected.items()):
        records=found.get(uid,[]);unique={r['line_sha256'] for r in records}
        status='retrieved_identity_valid' if len(unique)==1 else 'conflicting_exact_uid_records' if unique else 'retrieval_gap'
        uid_results.append({'measurement_uid':uid,'metadata_row_ids':[r['metadata_row_id'] for r in rows],
                            'status':status,'records':records,'censorship_finding':None,'human_review_complete':False})
    summary={'status':'s3_fallback_collection_finished','selected_uids':len(selected),'objects_attempted':len(results),
             'objects_stream_scanned':sum(r['status']=='stream_scanned' for r in results),
             'uid_status_counts':dict(Counter(r['status'] for r in uid_results)),
             'identity_valid_metadata_rows':sum(len(r['metadata_row_ids']) for r in uid_results if r['status']=='retrieved_identity_valid'),
             'frozen_total_compressed_content_length':manifest['total_compressed_content_length'],
             'censorship_finding':None,'human_review_complete':False,
             'interpretation':'Exact-UID records recovered from bounded official S3 prefixes; unmatched UIDs remain retrieval gaps. Only matched records retained, full compressed objects hashed while streamed but not archived. No censorship or independent probe conclusion.'}
    write_json(out/'uid_results.json',uid_results);write_json(out/'summary.json',summary)
    return summary


def main():
    parser=argparse.ArgumentParser(description=__doc__);sub=parser.add_subparsers(dest='command',required=True)
    planned=sub.add_parser('freeze');planned.add_argument('--raw-protocol',type=Path,required=True);planned.add_argument('--raw-run',type=Path,required=True);planned.add_argument('--out-dir',type=Path,required=True)
    execute=sub.add_parser('run');execute.add_argument('--protocol',type=Path,required=True);execute.add_argument('--out-dir',type=Path,required=True)
    args=parser.parse_args();result=freeze(args.raw_protocol,args.raw_run,args.out_dir) if args.command=='freeze' else run(args.protocol,args.out_dir)
    print(json.dumps({k:v for k,v in result.items() if k not in {'selected_rows','source_hashes','listings','objects'}},indent=2))


if __name__=='__main__':main()
