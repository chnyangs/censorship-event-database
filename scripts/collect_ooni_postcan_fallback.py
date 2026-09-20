#!/usr/bin/env python3
"""Recover exact OONI UIDs from frozen official postcan objects, without extraction.

The official uploader omits added UIDs from JSONL content, while postcan member
basenames retain the upload UID. Source JSONL attempts remain unchanged.
"""
from __future__ import annotations

import argparse
from collections import Counter
import gzip
import hashlib
import json
from pathlib import Path, PurePosixPath
import tarfile
import urllib.error
import urllib.parse
import zlib

import collect_ooni_s3_fallback as s3

raw_api=s3.raw_api
sha,now,write_json,require=s3.sha,s3.now,s3.write_json,s3.require
LIMITS={**s3.LIMITS,'max_post_member_bytes':8_000_000}


def freeze(source,out):
    source,out=source.resolve(),out.resolve();require(not out.exists(),'Refusing to overwrite postcan protocol')
    original=s3.verify_protocol(source)
    objects=[o for listing in original['listings'] for o in listing['objects'] if o['key'].endswith('.tar.gz')]
    total=sum(o['content_length'] for o in objects)
    require(len({o['key'] for o in objects})==len(objects),'Duplicate postcan objects')
    inputs=[s3.file_reference(p) for p in sorted(source.rglob('*')) if p.is_file()]+original['source_hashes']
    prefixes=original['prefixes']
    manifest={'status':'frozen_before_postcan_requests','frozen_at_utc':now(),
              'selection':'Every unresolved UID from the frozen API-to-S3 selection; all .tar.gz objects in its already captured complete exact-hour prefix listings. No repeated API, listing or JSONL requests, and no anomaly filtering.',
              'source_jsonl_protocol':str(source),'source_hashes':inputs,'selected_rows':original['selected_rows'],
              'prefixes':prefixes,'objects':objects,'object_count':len(objects),
              'total_compressed_content_length':total,
              'empty_postcan_prefixes':[p for p in prefixes if not any(o['key'].startswith(p) for o in objects)],
              'download_eligible':len(objects)<=LIMITS['max_objects'] and total<=LIMITS['max_compressed_bytes'],
              'limits':LIMITS,'collector_sha256':sha(Path(__file__).read_bytes()),
              's3_helper_sha256':sha(Path(s3.__file__).read_bytes()),
              'identity_helper_sha256':sha(Path(raw_api.__file__).read_bytes()),
              'format_sources':['https://github.com/ooni/api/blob/master/newapi/ooni_api_uploader.py',
                                'https://github.com/ooni/data/blob/main/oonidata/src/oonidata/dataclient.py',
                                'https://github.com/ooni/api/blob/master/newapi/ooniapi/probe_services.py'],
              'identity_policy':'Exact .post member basename UID; verify SHA-512(original POST bytes) first 16 hex characters equals UID suffix; parse format=json and content object; compare all six frozen metadata identity fields. Existing content measurement_uid must agree. Filename-derived UID provenance is explicit.',
              'body_retention':'Only original bytes of exact UID and identity-matching POST members are retained. No tar members extracted to filesystem. Compressed objects are streamed and hashed, not archived.',
              'censorship_finding':None,'human_review_complete':False}
    out.mkdir(parents=True);write_json(out/'manifest.json',manifest)
    for name,path in [('collector_source.py',Path(__file__)),('collect_ooni_s3_fallback.py',Path(s3.__file__)),
                      ('collect_ooni_raw_measurements.py',Path(raw_api.__file__))]:
        (out/name).write_bytes(path.read_bytes())
    write_json(out/'freeze_hashes.json',{'files':{p.name:sha(p.read_bytes()) for p in sorted(out.iterdir())}})
    return manifest


class ExpandedReader:
    def __init__(self,stream,limit):self.stream,self.limit,self.size=stream,limit,0
    def read(self,size=-1):
        remaining=self.limit-self.size
        data=self.stream.read(min(size,remaining+1) if size>=0 else remaining+1)
        self.size+=len(data);require(self.size<=self.limit,'Uncompressed postcan byte cap exceeded')
        return data


def member_uid(member):
    parts=PurePosixPath(member.name).parts
    require(not member.name.startswith('/') and parts and all(raw_api.safe_component(p) for p in parts),'Unsafe tar member path')
    require(not member.issym() and not member.islnk(),'Tar links are not permitted')
    if not member.isfile() or not parts[-1].endswith('.post'):return None
    return parts[-1][:-5]


def scan_object(response,obj,selected,audit=None,limits=LIMITS):
    headers={k.lower():v for k,v in response.headers.items()}
    require(response.status==200,'Postcan HTTP status is not 200')
    require(headers.get('content-length')==str(obj['content_length']),'Postcan Content-Length differs from frozen size')
    require(headers.get('etag')==obj['etag'],'Postcan ETag differs from frozen listing')
    compressed=s3.HashingReader(response,obj['content_length']);matches=[];mismatches=[];members=0;exact=0;retained=0
    expanded=None
    try:
        with gzip.GzipFile(fileobj=compressed,mode='rb') as stream:
            expanded=ExpandedReader(stream,limits['max_uncompressed_bytes_per_object'])
            with tarfile.open(fileobj=expanded,mode='r|') as archive:
                for member in archive:
                    members+=1;uid=member_uid(member)
                    require(member.size>=0,'Negative tar member size')
                    if uid not in selected:continue
                    exact+=1
                    require(member.size<=limits['max_post_member_bytes'],'POST member byte cap exceeded')
                    handle=archive.extractfile(member)
                    require(handle is not None,'Matched POST member has no regular content')
                    body=handle.read(limits['max_post_member_bytes']+1)
                    require(len(body)==member.size,'POST member truncated or exceeds declared size')
                    body_hash=sha(body)
                    entry={'measurement_uid':uid,'member_name':member.name,'post_body_sha256':body_hash,
                           'uid_source':'postcan_member_basename','uid_content_hash_valid':hashlib.sha512(body).hexdigest()[:16]==uid.rsplit('_',1)[-1]}
                    if not entry['uid_content_hash_valid']:
                        mismatches.append({**entry,'identity_checks':[],'error':'UID suffix differs from original POST hash'});continue
                    post=json.loads(body)
                    require(isinstance(post,dict) and isinstance(post.get('format'),str)
                            and post['format'].lower()=='json' and isinstance(post.get('content'),dict),
                            'Matched POST is not format=json with object content')
                    record=dict(post['content'])
                    if record.get('measurement_uid') not in (None,uid):
                        mismatches.append({**entry,'identity_checks':[],'error':'Embedded UID disagrees with member UID'});continue
                    record['measurement_uid']=uid
                    checks=[{'metadata_row_id':r['metadata_row_id'],**raw_api.validate_identity(record,r['metadata'])} for r in selected[uid]]
                    entry['identity_checks']=checks
                    if all(c['valid'] for c in checks):
                        retained+=len(body);require(retained<=limits['max_retained_matching_bytes'],'Matching POST byte cap exceeded')
                        matches.append({**entry,'body':body,'review_fields':raw_api.review_fields(record)})
                    else:mismatches.append(entry)
            while expanded.read(65536):pass
        require(compressed.size==obj['content_length'],'Postcan response ended before frozen size')
    finally:
        if audit is not None:audit.update(streamed_compressed_bytes=compressed.size,
                streamed_compressed_prefix_sha256='sha256:'+compressed.hasher.hexdigest(),
                streamed_uncompressed_bytes=expanded.size if expanded else 0)
    return {'compressed_body_sha256':'sha256:'+compressed.hasher.hexdigest(),'compressed_bytes':compressed.size,
            'members_scanned':members,'exact_uid_members':exact,'identity_mismatches':mismatches,'matches':matches}


def verify_protocol(protocol):
    for name,expected in json.loads((protocol/'freeze_hashes.json').read_text())['files'].items():
        require(raw_api.safe_component(name) and sha((protocol/name).read_bytes())==expected,'Frozen postcan protocol hash mismatch')
    manifest=json.loads((protocol/'manifest.json').read_text())
    for key,path in [('collector_sha256',Path(__file__)),('s3_helper_sha256',Path(s3.__file__)),('identity_helper_sha256',Path(raw_api.__file__))]:
        require(manifest[key]==sha(path.read_bytes()),'Postcan code/helper changed after freeze')
    for ref in manifest['source_hashes']:require(sha(Path(ref['path']).read_bytes())==ref['sha256'],'Source changed after postcan freeze')
    require(manifest['limits']==LIMITS,'Postcan limits changed')
    total=sum(o['content_length'] for o in manifest['objects'])
    require(total==manifest['total_compressed_content_length'] and total<=LIMITS['max_compressed_bytes'],'Postcan total exceeds 100 MB or differs from freeze')
    require(manifest['download_eligible'] is True and len(manifest['objects'])==manifest['object_count']<=LIMITS['max_objects'],'Postcan inventory is ineligible')
    return manifest


def run(protocol,out,opener=s3.open_url):
    protocol,out=protocol.resolve(),out.resolve();require(not out.exists(),'Refusing to overwrite postcan run')
    manifest=verify_protocol(protocol);selected={}
    for row in manifest['selected_rows']:selected.setdefault(row['metadata']['measurement_uid'],[]).append(row)
    out.mkdir(parents=True)
    write_json(out/'execution_manifest.json',{'created_before_requests_at_utc':now(),
               'protocol_sha256':sha((protocol/'manifest.json').read_bytes()),'limits':LIMITS,
               'selected_uids':sorted(selected),'object_count':len(manifest['objects']),
               'total_compressed_content_length':manifest['total_compressed_content_length']})
    limiter=raw_api.RateLimiter(LIMITS['minimum_request_start_interval_seconds']);results=[];found={};retained=0
    for obj in manifest['objects']:
        url=s3.ORIGIN+'/'+urllib.parse.quote(obj['key'],safe='/');limiter.wait()
        capture={'key':obj['key'],'requested_url':url,'request_headers':{'If-Match':obj['etag']},
                 'started_at_utc':now(),'status':'retrieval_gap','http_status':None,'error':None}
        try:
            with opener(url,{'If-Match':obj['etag']}) as response:
                capture.update(http_status=response.status,headers=dict(response.headers.items()),final_url=response.url)
                require(response.url==url,'Postcan redirect changed frozen key')
                scanned=scan_object(response,obj,selected,audit=capture)
            matches=scanned.pop('matches');capture.update(scanned,status='stream_scanned')
            retained+=sum(len(m['body']) for m in matches)
            require(retained<=LIMITS['max_retained_matching_bytes'],'Campaign POST retention byte cap exceeded')
            for match in matches:
                body=match.pop('body');dest=out/'records'/hashlib.sha256(body).hexdigest()
                if not dest.exists():
                    dest.mkdir(parents=True);(dest/'post.json').write_bytes(body)
                    write_json(dest/'review_fields.json',match['review_fields'])
                entry={k:v for k,v in match.items() if k!='review_fields'}
                entry.update(object_key=obj['key'],post_path=str(dest/'post.json'))
                found.setdefault(match['measurement_uid'],[]).append(entry)
        except (OSError,ValueError,EOFError,tarfile.TarError,zlib.error) as exc:
            capture.update(status='retrieval_gap',error=f'{type(exc).__name__}: {exc}')
            if isinstance(exc,urllib.error.HTTPError):capture.update(http_status=exc.code,headers=dict(exc.headers.items()))
        capture['finished_at_utc']=now();results.append(capture)
        write_json(out/'objects'/(hashlib.sha256(obj['key'].encode()).hexdigest()+'.json'),capture)
    outcomes=[]
    for uid,rows in sorted(selected.items()):
        records=found.get(uid,[]);unique={r['post_body_sha256'] for r in records}
        status='retrieved_identity_valid' if len(unique)==1 else 'conflicting_exact_uid_records' if unique else 'retrieval_gap'
        outcomes.append({'measurement_uid':uid,'metadata_row_ids':[r['metadata_row_id'] for r in rows],
                         'status':status,'records':records,'censorship_finding':None,'human_review_complete':False})
    summary={'status':'postcan_fallback_collection_finished','selected_uids':len(selected),
             'objects_attempted':len(results),'objects_stream_scanned':sum(r['status']=='stream_scanned' for r in results),
             'uid_status_counts':dict(Counter(r['status'] for r in outcomes)),
             'identity_valid_metadata_rows':sum(len(r['metadata_row_ids']) for r in outcomes if r['status']=='retrieved_identity_valid'),
             'frozen_total_compressed_content_length':manifest['total_compressed_content_length'],
             'censorship_finding':None,'human_review_complete':False,
             'interpretation':'Exact member UID, original POST hash suffix and six metadata identity fields validated; raw/control fields are retained for review only. Missing records remain retrieval gaps. No censorship, independence, population denominator or human adjudication conclusion.'}
    write_json(out/'uid_results.json',outcomes);write_json(out/'summary.json',summary)
    return summary


def main():
    parser=argparse.ArgumentParser(description=__doc__);sub=parser.add_subparsers(dest='command',required=True)
    planned=sub.add_parser('freeze');planned.add_argument('--jsonl-protocol',type=Path,required=True);planned.add_argument('--out-dir',type=Path,required=True)
    execute=sub.add_parser('run');execute.add_argument('--protocol',type=Path,required=True);execute.add_argument('--out-dir',type=Path,required=True)
    args=parser.parse_args();result=freeze(args.jsonl_protocol,args.out_dir) if args.command=='freeze' else run(args.protocol,args.out_dir)
    print(json.dumps({k:v for k,v in result.items() if k not in {'source_hashes','selected_rows','objects'}},indent=2))


if __name__=='__main__':main()
