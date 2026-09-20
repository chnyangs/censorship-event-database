"""Offline evidence checks for distinct OONI API, JSONL and postcan stages."""
from collections import Counter, defaultdict
from datetime import datetime
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import urllib.parse

from collect_ooni_raw_measurements import canonical, locator_error, review_fields, validate_identity

STAGES={
    'ooni_raw':('analysis/evidence_repairs/l0_ooni_raw_protocol_v1','sources/evidence_repairs/l0_ooni_raw_v1'),
    'ooni_jsonl':('analysis/evidence_repairs/l0_ooni_s3_protocol_v1','sources/evidence_repairs/l0_ooni_s3_v1'),
    'ooni_postcan':('analysis/evidence_repairs/l0_ooni_postcan_protocol_v2','sources/evidence_repairs/l0_ooni_postcan_v2'),
}
ORIGIN='https://ooni-data-eu-fra.s3.eu-central-1.amazonaws.com'


def require(condition,message):
    if not condition:raise ValueError('OONI audit: '+message)


def equal(actual,expected,label):
    require(actual==expected,f'{label} mismatch')


def digest(raw):return 'sha256:'+hashlib.sha256(raw).hexdigest()


def stamp(value):
    parsed=datetime.fromisoformat(value.replace('Z','+00:00'))
    require(parsed.tzinfo is not None,'timezone missing in provenance timestamp')
    return parsed


def machine(record):
    require(record.get('censorship_finding') is None,'collection promoted to censorship finding')
    require(record.get('human_review_complete',False) is False,'collection promoted to human review')


def freeze(inputs,name):
    directory,run=STAGES[name]
    seal=inputs.read(directory+'/freeze_hashes.json')['files']
    require('manifest.json' in seal,'freeze seal omits manifest')
    for relative,expected in seal.items():
        require(not Path(relative).is_absolute() and '..' not in Path(relative).parts,'unsafe frozen path')
        inputs.verify_hash(directory+'/'+relative,expected)
    manifest=inputs.read(directory+'/manifest.json');machine(manifest)
    inputs.verify_hash(directory+'/collector_source.py',manifest['collector_sha256'])
    for field,filename in [('s3_helper_sha256','collect_ooni_s3_fallback.py'),
                           ('identity_helper_sha256','collect_ooni_raw_measurements.py')]:
        if field in manifest:inputs.verify_hash(directory+'/'+filename,manifest[field])
    for reference in manifest.get('metadata_source_hashes',manifest.get('source_hashes',[])):
        inputs.verify_hash(reference['path'],reference['sha256'])
    execution=inputs.read(run+'/execution_manifest.json')
    equal(execution['protocol_sha256'],digest(inputs.blob(directory+'/manifest.json')),'execution protocol hash')
    equal(execution['limits'],manifest['limits'],'execution limits')
    started=execution.get('created_before_requests_at_utc',execution.get('created_before_object_requests_at_utc'))
    require(stamp(started)>=stamp(manifest['frozen_at_utc']),'execution predates freeze')
    return manifest,execution,stamp(started)


def rows_by_id(rows):
    output={}
    for row in rows:
        rid=row['metadata_row_id']
        require(rid not in output,'duplicate frozen metadata row ID')
        equal(rid,hashlib.sha256(canonical(row['metadata']).encode()).hexdigest(),'canonical metadata row hash')
        output[rid]=row
    return output


def check_ids(actual,expected,label):
    equal(len(actual),len(set(actual)),label+' duplicates')
    equal(set(actual),set(expected),label)


def checks_for(payload,rows):
    return [{'metadata_row_id':r['metadata_row_id'],**validate_identity(payload,r['metadata'])} for r in rows]


def checked_review(inputs,path,payload):
    actual=inputs.read(path);machine(actual)
    equal(actual,review_fields(payload),'derived raw review fields')


def raw_stage(inputs,report,manifest,execution,started):
    _,run=STAGES['ooni_raw'];rows=rows_by_id(manifest['metadata_rows']);groups=defaultdict(list);invalid={}
    for rid,row in rows.items():
        error=locator_error(row['metadata'].get('measurement_url'),row['metadata'])
        equal(error,row['locator_validation_error'],'frozen raw locator validation')
        if error is None:groups[row['metadata']['measurement_url']].append(row)
        else:invalid[rid]=error
    invalid_rows=inputs.read(run+'/invalid_locator_rows.json')
    check_ids([r['metadata_row_id'] for r in invalid_rows],invalid,'invalid locator rows')
    for row in invalid_rows:equal(row['reason'],invalid[row['metadata_row_id']],'invalid locator reason')
    results=inputs.read(run+'/results.json');by_url={r['measurement_url']:r for r in results}
    equal(len(results),len(by_url),'unique API result URLs');equal(set(by_url),set(groups),'complete API URL set')
    attempts=0;valid_rows=0
    for url,result in by_url.items():
        machine(result);qid=hashlib.sha256(url.encode()).hexdigest();directory=run+'/captures/'+qid
        equal(result['request_id'],qid,'API request ID');equal(result,inputs.read(directory+'/result.json'),'API result ledger')
        check_ids(result['metadata_row_ids'],[r['metadata_row_id'] for r in groups[url]],'API metadata row set')
        require(0<len(result['attempts'])<=manifest['limits']['max_attempts_per_url'],'API attempts outside frozen cap')
        alternatives=[]
        for index,attempt in enumerate(result['attempts'],1):
            attempts+=1;prefix=directory+f'/attempt_{index}'
            equal(inputs.relative(attempt['body_path']),prefix+'/response.body','API body path')
            body=inputs.verify_hash(attempt['body_path'],attempt['body_sha256'])
            equal(len(body),attempt['body_bytes'],'API captured body bytes')
            equal(inputs.read(prefix+'/capture.json'),attempt,'API attempt capture')
            equal(attempt['requested_url'],url,'API request URL')
            require(started<=stamp(attempt['started_at_utc'])<=stamp(attempt['finished_at_utc']),'API attempt chronology')
            if attempt['http_status']==200 and not attempt.get('transport_error') and not attempt.get('truncated'):
                try:
                    payload=json.loads(body);checks=checks_for(payload,groups[url])
                    alternatives.append((payload,checks))
                except (ValueError,TypeError,KeyError):pass
        checks=result['identity_checks']
        if checks:require(any(checks==computed for _,computed in alternatives),'API identity checks lack captured body support')
        valid_rows+=sum(c['valid'] for c in checks)
        if result['status']=='retrieved_identity_valid':
            require(checks and all(c['valid'] for c in checks),'API valid status lacks valid identities')
            payload=next(payload for payload,computed in alternatives if computed==checks)
            equal(inputs.relative(result['raw_review_path']),directory+'/review_fields.json','API review path')
            checked_review(inputs,result['raw_review_path'],payload)
        elif result['status']=='retrieved_identity_mismatch':require(checks and not all(c['valid'] for c in checks),'API mismatch status disagrees with checks')
        else:require(result['status']=='retrieval_gap' and not checks,'API gap status disagrees with checks')
    computed={'frozen_metadata_rows':len(rows),'frozen_raw_urls':len(groups),'raw_urls_attempted':len(results),
              'url_status_counts':dict(Counter(r['status'] for r in results)),'identity_valid_metadata_rows':valid_rows,
              'invalid_locator_rows':len(invalid),'http_attempts':attempts}
    for key,value in computed.items():equal(value,report[key],key)
    equal(execution['frozen_distinct_metadata_rows'],len(rows),'execution metadata count')
    equal(execution['frozen_distinct_raw_urls'],len(groups),'execution URL count')
    expected='raw_retrieval_complete' if all(r['status']=='retrieved_identity_valid' for r in results) and not invalid else 'raw_retrieval_partial'
    equal(report['status'],expected,'API final status')
    return computed


def selected_rows(inputs,name,manifest):
    rows=rows_by_id(manifest['selected_rows'])
    if name=='ooni_postcan':
        equal(inputs.relative(manifest['source_jsonl_protocol']),STAGES['ooni_jsonl'][0],'postcan source protocol')
        parent=inputs.read(STAGES['ooni_jsonl'][0]+'/manifest.json')
        equal(manifest['selected_rows'],parent['selected_rows'],'postcan preserves JSONL selected rows')
        expected=[o for listing in parent['listings'] for o in listing['objects'] if o['key'].endswith('.tar.gz')]
        equal(manifest['objects'],expected,'postcan uses captured tar inventory')
    else:
        source=inputs.read(STAGES['ooni_raw'][0]+'/manifest.json')
        results=inputs.read(STAGES['ooni_raw'][1]+'/results.json')
        unresolved={r['measurement_url'] for r in results if r['status']!='retrieved_identity_valid'}
        expected={r['metadata_row_id']:r for r in source['metadata_rows'] if r['metadata']['measurement_url'] in unresolved}
        equal(set(rows),set(expected),'S3 selects every unresolved API metadata row')
        for rid,row in rows.items():equal(row['metadata'],expected[rid]['metadata'],'S3 preserves API metadata')
    groups=defaultdict(list)
    for row in rows.values():
        meta=row['metadata'];require(locator_error(meta['measurement_url'],meta) is None,'invalid selected raw locator')
        groups[meta['measurement_uid']].append(row)
    return groups


def object_stage(inputs,name,report,manifest,execution,started):
    _,run=STAGES[name];groups=selected_rows(inputs,name,manifest)
    check_ids(execution['selected_uids'],groups,'execution selected UIDs')
    objects={o['key']:o for o in manifest['objects']}
    equal(len(objects),manifest['object_count'],'frozen unique object count')
    total=sum(o['content_length'] for o in objects.values())
    equal(total,manifest['total_compressed_content_length'],'frozen compressed total')
    require(total<=manifest['limits']['max_compressed_bytes'] and manifest['download_eligible'] is True,'ineligible compressed download total')
    equal(execution['object_count'],len(objects),'execution object count')
    equal(execution['total_compressed_content_length'],total,'execution compressed total')
    captured={}
    for path in sorted((inputs.root/run/'objects').glob('*.json')):
        capture=inputs.read(path.relative_to(inputs.root).as_posix());key=capture['key']
        require(key in objects and key not in captured,'foreign or duplicate captured S3 object')
        equal(path.name,hashlib.sha256(key.encode()).hexdigest()+'.json','S3 object capture filename')
        obj=objects[key];url=ORIGIN+'/'+urllib.parse.quote(key,safe='/')
        equal(capture['requested_url'],url,'S3 frozen object URL');equal(capture['request_headers']['If-Match'],obj['etag'],'S3 request ETag')
        require(started<=stamp(capture['started_at_utc'])<=stamp(capture['finished_at_utc']),'S3 object chronology')
        if capture['status']=='stream_scanned':
            require(capture['http_status']==200 and capture['error'] is None,'successful S3 scan has transport error')
            equal(capture['final_url'],url,'S3 final URL');headers={k.lower():v for k,v in capture['headers'].items()}
            equal(headers['etag'],obj['etag'],'S3 response ETag');equal(headers['content-length'],str(obj['content_length']),'S3 Content-Length')
            equal(capture['compressed_bytes'],obj['content_length'],'S3 streamed compressed bytes')
            equal(capture['streamed_compressed_bytes'],obj['content_length'],'S3 stream audit bytes')
            require(re.fullmatch(r'sha256:[0-9a-f]{64}',capture['compressed_body_sha256']) is not None,'malformed recorded S3 stream hash')
            equal(capture['streamed_compressed_prefix_sha256'],capture['compressed_body_sha256'],'S3 complete/prefix stream hash')
        else:equal(capture['status'],'retrieval_gap','S3 capture status')
        captured[key]=capture
    equal(set(captured),set(objects),'complete S3 object attempt set')
    results=inputs.read(run+'/uid_results.json');check_ids([r['measurement_uid'] for r in results],groups,'S3 UID result set')
    record_counts=Counter();valid_rows=0
    for result in results:
        machine(result);uid=result['measurement_uid'];rows=groups[uid]
        check_ids(result['metadata_row_ids'],[r['metadata_row_id'] for r in rows],'S3 result row set');hashes=set()
        for record in result['records']:
            equal(record['measurement_uid'],uid,'record UID');key=record['object_key']
            require(key in captured and captured[key]['status']=='stream_scanned','matched record lacks complete captured object')
            require(all(key.startswith(r['s3_prefix']) for r in rows),'matched object is outside selected UID prefix')
            if name=='ooni_postcan':
                member=PurePosixPath(record['member_name'])
                require(not member.is_absolute() and '..' not in member.parts and member.name==uid+'.post','unsafe or mismatching postcan member UID')
                path=inputs.relative(record['post_path']);digest_value=record['post_body_sha256']
                equal(path,run+'/records/'+digest_value.removeprefix('sha256:')+'/post.json','retained POST path')
                body=inputs.verify_hash(path,digest_value);post=json.loads(body)
                equal(hashlib.sha512(body).hexdigest()[:16],uid.rsplit('_',1)[-1],'UID original POST hash suffix')
                require(record['uid_content_hash_valid'] is True and record['uid_source']=='postcan_member_basename','postcan UID provenance')
                require(isinstance(post.get('format'),str) and post['format'].lower()=='json' and isinstance(post.get('content'),dict),'invalid POST content format')
                payload=dict(post['content']);require(payload.get('measurement_uid') in (None,uid),'embedded POST UID mismatch');payload['measurement_uid']=uid
            else:
                path=inputs.relative(record['raw_record_path']);digest_value=record['line_sha256']
                equal(path,run+'/records/'+digest_value.removeprefix('sha256:')+'/measurement.jsonl','retained JSONL path')
                payload=json.loads(inputs.verify_hash(path,digest_value));equal(payload.get('measurement_uid'),uid,'JSONL exact UID')
            checks=checks_for(payload,rows);require(all(c['valid'] for c in checks),'retained raw content fails metadata identity')
            equal(record['identity_checks'],checks,'retained record identity checks')
            checked_review(inputs,str(Path(path).parent/'review_fields.json'),payload)
            hashes.add(digest_value);record_counts[key]+=1
        expected='retrieved_identity_valid' if len(hashes)==1 else 'conflicting_exact_uid_records' if hashes else 'retrieval_gap'
        equal(result['status'],expected,'UID result status')
        if expected=='retrieved_identity_valid':valid_rows+=len(rows)
    if name=='ooni_postcan':
        for key,capture in captured.items():
            if capture['status']=='stream_scanned':equal(capture['exact_uid_members'],record_counts[key]+len(capture['identity_mismatches']),'postcan exact member accounting')
    computed={'selected_uids':len(groups),'objects_attempted':len(captured),
              'objects_stream_scanned':sum(r['status']=='stream_scanned' for r in captured.values()),
              'uid_status_counts':dict(Counter(r['status'] for r in results)),
              'identity_valid_metadata_rows':valid_rows,'frozen_total_compressed_content_length':total}
    for key,value in computed.items():equal(value,report[key],key)
    equal(report['status'],'postcan_fallback_collection_finished' if name=='ooni_postcan' else 's3_fallback_collection_finished','S3 final status')
    return computed


def audit_stage(inputs,name,report):
    """Return recomputed stage metrics; malformed evidence raises ValueError."""
    require(name in STAGES,'unknown evidence stage');machine(report)
    manifest,execution,started=freeze(inputs,name)
    computed=raw_stage(inputs,report,manifest,execution,started) if name=='ooni_raw' else object_stage(inputs,name,report,manifest,execution,started)
    return {**computed,'censorship_finding':None,'human_review_complete':False,
            'offline_artifact_accounting_verified':True,
            'full_compressed_objects_retained':False if name!='ooni_raw' else None}
