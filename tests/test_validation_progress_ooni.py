"""Synthetic offline OONI evidence chains; never research measurements."""
import hashlib
import json
from pathlib import Path

import pytest

import validation_progress_ooni as audit


def write(root,path,value):
    target=root/path;target.parent.mkdir(parents=True,exist_ok=True)
    target.write_bytes(value if isinstance(value,bytes) else (json.dumps(value,sort_keys=True)+'\n').encode())


class Inputs:
    def __init__(self,root):self.root,self.records=root,{}
    def relative(self,path):
        path=Path(path)
        if path.is_absolute():path=path.relative_to(self.root)
        assert '..' not in path.parts
        return path.as_posix()
    def blob(self,path):
        relative=self.relative(path);raw=(self.root/relative).read_bytes()
        self.records[relative]={'sha256':audit.digest(raw)};return raw
    def read(self,path):return json.loads(self.blob(path))
    def verify_hash(self,path,expected):
        raw=self.blob(path);audit.equal(audit.digest(raw),expected,'input hash');return raw


def fixture(root,metadata_change=None):
    content={'report_id':'synthetic-report','input':'https://example.test/','probe_cc':'ET','probe_asn':'AS123',
             'test_name':'web_connectivity','measurement_start_time':'2025-10-15 06:01:49',
             'test_keys':{'blocking':False,'accessible':True,'control_failure':None}}
    body=json.dumps({'format':'json','content':content}).encode()
    uid='20251015060213.849829_ET_webconnectivity_'+hashlib.sha512(body).hexdigest()[:16]
    url='https://api.ooni.io/api/v1/raw_measurement?measurement_uid='+uid
    meta={k:v for k,v in content.items() if k!='test_keys'}
    meta.update(measurement_uid=uid,measurement_url=url,anomaly=False)
    meta.update(metadata_change or {})
    rid=hashlib.sha256(audit.canonical(meta).encode()).hexdigest()
    row={'metadata_row_id':rid,'metadata':meta,'locator_validation_error':None}
    prefix='raw/20251015/06/ET/webconnectivity/'
    selected={**row,'s3_prefix':prefix,'api_retrieval_status':'retrieval_gap'}
    limits={'max_attempts_per_url':2,'max_compressed_bytes':100_000_000}
    plans={name:{'metadata_source_hashes':[],'source_hashes':[],'limits':limits,'frozen_at_utc':'2026-09-20T00:00:00Z',
                 'censorship_finding':None,'human_review_complete':False} for name in audit.STAGES}
    raw_plan,raw_run=audit.STAGES['ooni_raw']
    plans['ooni_raw']['metadata_rows']=[row]
    qid=hashlib.sha256(url.encode()).hexdigest();directory=raw_run+'/captures/'+qid
    attempt={'body_path':str(root/directory/'attempt_1/response.body'),'body_sha256':audit.digest(b''),'body_bytes':0,
             'requested_url':url,'http_status':None,'transport_error':'synthetic timeout','truncated':False,
             'started_at_utc':'2026-09-20T00:00:02Z','finished_at_utc':'2026-09-20T00:00:03Z'}
    result={'request_id':qid,'measurement_url':url,'metadata_row_ids':[rid],'attempts':[attempt],
            'identity_checks':[],'raw_review_path':None,'status':'retrieval_gap','censorship_finding':None}
    write(root,directory+'/attempt_1/response.body',b'');write(root,directory+'/attempt_1/capture.json',attempt)
    write(root,directory+'/result.json',result);write(root,raw_run+'/results.json',[result]);write(root,raw_run+'/invalid_locator_rows.json',[])
    reports={'ooni_raw':{'status':'raw_retrieval_partial','frozen_metadata_rows':1,'frozen_raw_urls':1,'raw_urls_attempted':1,
              'url_status_counts':{'retrieval_gap':1},'identity_valid_metadata_rows':0,'invalid_locator_rows':0,
              'http_attempts':1,'censorship_finding':None,'human_review_complete':False}}
    objects={}
    for name,ext,size in [('ooni_jsonl','jsonl.gz',10),('ooni_postcan','tar.gz',20)]:
        objects[name]={'key':prefix+'2025101506_ET_webconnectivity.n4.0.'+ext,'content_length':size,'etag':'"test-etag"'}
    for name in ['ooni_jsonl','ooni_postcan']:
        protocol,run=audit.STAGES[name];obj=objects[name]
        plans[name].update(selected_rows=[selected],objects=[obj],object_count=1,
                           total_compressed_content_length=obj['content_length'],download_eligible=True)
        if name=='ooni_jsonl':plans[name]['listings']=[{'objects':list(objects.values())}]
        else:plans[name]['source_jsonl_protocol']=str(root/audit.STAGES['ooni_jsonl'][0])
        url_object=audit.ORIGIN+'/'+obj['key']
        captured={'key':obj['key'],'requested_url':url_object,'final_url':url_object,'http_status':200,
                  'request_headers':{'If-Match':obj['etag']},'headers':{'ETag':obj['etag'],'Content-Length':str(obj['content_length'])},
                  'status':'stream_scanned','error':None,'compressed_bytes':obj['content_length'],
                  'streamed_compressed_bytes':obj['content_length'],'compressed_body_sha256':'sha256:'+'0'*64,
                  'streamed_compressed_prefix_sha256':'sha256:'+'0'*64,'identity_mismatches':[],
                  'started_at_utc':'2026-09-20T00:00:02Z','finished_at_utc':'2026-09-20T00:00:03Z'}
        records=[]
        if name=='ooni_postcan':
            captured['exact_uid_members']=1
            checksum=audit.digest(body);path=run+'/records/'+checksum.removeprefix('sha256:')+'/post.json'
            payload={**content,'measurement_uid':uid}
            records=[{'measurement_uid':uid,'object_key':obj['key'],'member_name':'spool/'+uid+'.post',
                      'uid_source':'postcan_member_basename','uid_content_hash_valid':True,'post_body_sha256':checksum,
                      'post_path':str(root/path),'identity_checks':audit.checks_for(payload,[row])}]
            write(root,path,body);write(root,str(Path(path).parent/'review_fields.json'),audit.review_fields(payload))
        write(root,run+'/objects/'+hashlib.sha256(obj['key'].encode()).hexdigest()+'.json',captured)
        status='retrieved_identity_valid' if records else 'retrieval_gap'
        write(root,run+'/uid_results.json',[{'measurement_uid':uid,'metadata_row_ids':[rid],'records':records,'status':status,
                                            'human_review_complete':False,'censorship_finding':None}])
        reports[name]={'status':'postcan_fallback_collection_finished' if records else 's3_fallback_collection_finished',
                       'selected_uids':1,'objects_attempted':1,'objects_stream_scanned':1,'uid_status_counts':{status:1},
                       'identity_valid_metadata_rows':int(bool(records)),'frozen_total_compressed_content_length':obj['content_length'],
                       'human_review_complete':False,'censorship_finding':None}
    for name,(protocol,run) in audit.STAGES.items():
        code=('synthetic frozen '+name).encode();plans[name]['collector_sha256']=audit.digest(code)
        write(root,protocol+'/collector_source.py',code);write(root,protocol+'/manifest.json',plans[name])
        write(root,protocol+'/freeze_hashes.json',{'files':{p.name:audit.digest(p.read_bytes()) for p in (root/protocol).iterdir()}})
        execution={'protocol_sha256':audit.digest((root/protocol/'manifest.json').read_bytes()),'limits':limits,
                   'created_before_requests_at_utc':'2026-09-20T00:00:01Z'}
        if name=='ooni_raw':execution.update(frozen_distinct_metadata_rows=1,frozen_distinct_raw_urls=1)
        else:execution.update(selected_uids=[uid],object_count=1,total_compressed_content_length=objects[name]['content_length'])
        write(root,run+'/execution_manifest.json',execution)
    return Inputs(root),reports


def mutate(inputs,path,change):
    data=inputs.read(path);change(data);write(inputs.root,path,data)


def test_all_stages_recompute_separately_and_bind_retained_evidence(tmp_path):
    inputs,reports=fixture(tmp_path)
    audited={name:audit.audit_stage(inputs,name,report) for name,report in reports.items()}
    assert [audited[n]['identity_valid_metadata_rows'] for n in audit.STAGES]==[0,0,1]
    assert all(r['offline_artifact_accounting_verified'] for r in audited.values())
    assert audited['ooni_postcan']['full_compressed_objects_retained'] is False
    assert any(p.endswith('/post.json') for p in inputs.records)
    assert all(r['human_review_complete'] is False and r['censorship_finding'] is None for r in audited.values())


@pytest.mark.parametrize('field,value',[('report_id','wrong'),('input','https://wrong.test/'),('probe_asn','AS999'),
                                       ('probe_cc','TH'),('test_name','dnscheck'),('measurement_start_time','2025-10-15T06:00:00Z')])
def test_postcan_checks_actual_six_fields_not_only_saved_valid_flags(tmp_path,field,value):
    inputs,reports=fixture(tmp_path,{field:value})
    with pytest.raises(ValueError,match='metadata identity'):
        audit.audit_stage(inputs,'ooni_postcan',reports['ooni_postcan'])


@pytest.mark.parametrize('stage,field,value',[('ooni_raw','http_attempts',2),('ooni_jsonl','objects_stream_scanned',0),
                                            ('ooni_postcan','identity_valid_metadata_rows',2),('ooni_postcan','human_review_complete',True)])
def test_summary_inflation_and_human_promotion_rejected(tmp_path,stage,field,value):
    inputs,reports=fixture(tmp_path);reports[stage][field]=value
    with pytest.raises(ValueError):audit.audit_stage(inputs,stage,reports[stage])


def test_modified_frozen_code_and_execution_binding_rejected(tmp_path):
    inputs,reports=fixture(tmp_path);protocol,run=audit.STAGES['ooni_raw']
    mutate(inputs,run+'/execution_manifest.json',lambda x:x.update(protocol_sha256='sha256:'+'1'*64))
    with pytest.raises(ValueError,match='execution protocol'):audit.audit_stage(inputs,'ooni_raw',reports['ooni_raw'])
    write(tmp_path,protocol+'/collector_source.py',b'changed')
    with pytest.raises(ValueError,match='input hash'):audit.audit_stage(inputs,'ooni_raw',reports['ooni_raw'])


def test_duplicate_uid_or_foreign_object_ledger_rejected(tmp_path):
    inputs,reports=fixture(tmp_path);_,run=audit.STAGES['ooni_postcan']
    mutate(inputs,run+'/uid_results.json',lambda x:x.append(x[0]))
    with pytest.raises(ValueError,match='duplicates'):audit.audit_stage(inputs,'ooni_postcan',reports['ooni_postcan'])


def test_changed_original_post_or_review_fields_are_detected(tmp_path):
    inputs,reports=fixture(tmp_path);_,run=audit.STAGES['ooni_postcan']
    record=inputs.read(run+'/uid_results.json')[0]['records'][0]
    path=inputs.relative(record['post_path']);review=str(Path(path).parent/'review_fields.json')
    mutate(inputs,review,lambda r:r['test_keys'].update(blocking='dns'))
    with pytest.raises(ValueError,match='review fields'):audit.audit_stage(inputs,'ooni_postcan',reports['ooni_postcan'])
    write(tmp_path,path,b'changed original')
    with pytest.raises(ValueError,match='input hash'):audit.audit_stage(inputs,'ooni_postcan',reports['ooni_postcan'])


@pytest.mark.parametrize('change',['wrong-member','bad-etag','wrong-bytes','interior-foreign-path'])
def test_postcan_object_and_member_provenance_checked(tmp_path,change):
    inputs,reports=fixture(tmp_path);_,run=audit.STAGES['ooni_postcan']
    if change=='wrong-member':mutate(inputs,run+'/uid_results.json',lambda x:x[0]['records'][0].update(member_name='../unrelated.post'))
    elif change=='interior-foreign-path':mutate(inputs,run+'/uid_results.json',lambda x:x[0]['records'][0].update(post_path=str(tmp_path/'unrelated.json')))
    else:
        path=next((tmp_path/run/'objects').glob('*.json')).relative_to(tmp_path).as_posix()
        mutate(inputs,path,lambda x:x['headers'].update(ETag='"changed"') if change=='bad-etag' else x.update(compressed_bytes=999))
    with pytest.raises((ValueError,AssertionError)):audit.audit_stage(inputs,'ooni_postcan',reports['ooni_postcan'])
