"""Synthetic postcan identity and safe-streaming regressions; no live requests."""
import hashlib
import io
import json
from pathlib import Path
import tarfile

import pytest

import collect_ooni_postcan_fallback as mod

PREFIX='raw/20251015/06/ET/webconnectivity/'


def metadata(uid='synthetic',anomaly=False):
    return {'measurement_uid':uid,'measurement_url':'https://api.ooni.io/api/v1/raw_measurement?measurement_uid='+uid,
            'report_id':'synthetic-report','input':'https://example.test/','probe_cc':'ET','probe_asn':'AS123',
            'test_name':'web_connectivity','measurement_start_time':'2025-10-15T06:01:49Z','anomaly':anomaly}


def raw_record():
    record={k:v for k,v in metadata().items() if k not in {'measurement_url','anomaly'}}
    record['test_keys']={'blocking':'dns','control_failure':None,'control':{'dns':{'addrs':['192.0.2.1']}}}
    return record


class Response(io.BytesIO):
    def __init__(self,body,url,headers=None):
        super().__init__(body);self.url=url;self.status=200
        self.headers=headers or {'Content-Length':str(len(body)),'ETag':'"synthetic-etag"'}


def post_record():
    record=raw_record();record.pop('measurement_uid')
    body=json.dumps({'format':'json','content':record}).encode()
    uid='20251015060213.849829_ET_webconnectivity_'+hashlib.sha512(body).hexdigest()[:16]
    return uid,body


def archive_bytes(entries):
    out=io.BytesIO()
    with tarfile.open(fileobj=out,mode='w:gz') as archive:
        for name,body,kind in entries:
            entry=tarfile.TarInfo(name);entry.type=kind;entry.size=len(body)
            if kind==tarfile.SYMTYPE:entry.linkname='/outside/path';entry.size=0
            archive.addfile(entry,io.BytesIO(body))
    return out.getvalue()


@pytest.fixture(autouse=True)
def no_wait(monkeypatch):
    monkeypatch.setattr(mod.raw_api.RateLimiter,'wait',lambda self:None)


def frozen_source(tmp_path,entries=None,metadata_change=None,size=None):
    uid,post=post_record()
    if entries is None:entries=[('spool/incoming/2025101506_ET_webconnectivity/'+uid+'.post',post,tarfile.REGTYPE)]
    body=archive_bytes(entries);meta=metadata(uid,False)
    if metadata_change:meta.update(metadata_change)
    tar_object={'key':PREFIX+'2025101506_ET_webconnectivity.n4.0.tar.gz',
                'content_length':len(body) if size is None else size,'etag':'"synthetic-etag"','selected_jsonl_gzip':False}
    jsonl_object={'key':PREFIX+'2025101506_ET_webconnectivity.n4.0.jsonl.gz',
                  'content_length':10,'etag':'"jsonl-etag"','selected_jsonl_gzip':True}
    source=tmp_path/'jsonl_protocol';source.mkdir()
    manifest={'selected_rows':[{'metadata_row_id':'synthetic-row','metadata':meta,'s3_prefix':PREFIX}],
              'prefixes':[PREFIX],'objects':[jsonl_object],'object_count':1,'listing_complete':True,
              'listings':[{'prefix':PREFIX,'pagination_complete':True,'objects':[jsonl_object,tar_object]}],
              'source_hashes':[],'total_compressed_content_length':10,'download_eligible':True,
              'collector_sha256':mod.sha(Path(mod.s3.__file__).read_bytes()),
              'identity_helper_sha256':mod.sha(Path(mod.raw_api.__file__).read_bytes()),'limits':mod.s3.LIMITS}
    mod.write_json(source/'manifest.json',manifest)
    mod.write_json(source/'freeze_hashes.json',{'files':{'manifest.json':mod.sha((source/'manifest.json').read_bytes())}})
    protocol=tmp_path/'postcan_protocol';frozen=mod.freeze(source,protocol)
    return protocol,frozen,body


def test_freeze_uses_existing_tar_inventory_without_network_and_binds_hashes(tmp_path):
    protocol,frozen,body=frozen_source(tmp_path)
    assert frozen['object_count']==1 and frozen['total_compressed_content_length']==len(body)
    assert frozen['download_eligible'] and not frozen['empty_postcan_prefixes']
    assert frozen['objects'][0]['key'].endswith('.tar.gz')
    for name,digest in json.loads((protocol/'freeze_hashes.json').read_text())['files'].items():
        assert mod.sha((protocol/name).read_bytes())==digest


def test_exact_member_uid_post_hash_and_six_fields_recover_original_content(tmp_path):
    protocol,_,body=frozen_source(tmp_path)
    calls=[]
    def opener(url,headers):
        calls.append((url,headers));return Response(body,url)
    report=mod.run(protocol,tmp_path/'run',opener)
    assert report['uid_status_counts']=={'retrieved_identity_valid':1} and report['identity_valid_metadata_rows']==1
    assert len(calls)==1 and calls[0][1]=={'If-Match':'"synthetic-etag"'}
    result=json.loads((tmp_path/'run/uid_results.json').read_text())[0]['records'][0]
    assert result['uid_source']=='postcan_member_basename' and result['uid_content_hash_valid']
    assert Path(result['post_path']).read_bytes()==post_record()[1]
    capture=json.loads(next((tmp_path/'run/objects').glob('*.json')).read_text())
    assert capture['compressed_body_sha256']==mod.sha(body) and capture['exact_uid_members']==1
    assert not list((tmp_path/'run').rglob('*.tar.gz'))
    assert report['censorship_finding'] is None and report['human_review_complete'] is False


@pytest.mark.parametrize('field,value',[('report_id','wrong'),('input','https://wrong.test/'),('probe_asn','AS999'),
                                       ('probe_cc','TH'),('test_name','dnscheck'),('measurement_start_time','2025-10-15T06:00:00Z')])
def test_any_metadata_identity_mismatch_keeps_gap_and_does_not_retain_body(tmp_path,field,value):
    protocol,_,body=frozen_source(tmp_path,metadata_change={field:value})
    report=mod.run(protocol,tmp_path/'run',lambda url,headers:Response(body,url))
    assert report['uid_status_counts']=={'retrieval_gap':1} and not (tmp_path/'run/records').exists()
    capture=json.loads(next((tmp_path/'run/objects').glob('*.json')).read_text())
    assert len(capture['identity_mismatches'])==1


@pytest.mark.parametrize('name,kind',[('../escape.post',tarfile.REGTYPE),('/absolute.post',tarfile.REGTYPE),
                                    ('symlink.post',tarfile.SYMTYPE),('hardlink.post',tarfile.LNKTYPE)])
def test_unsafe_member_paths_or_links_never_extract_or_count(tmp_path,name,kind):
    protocol,_,body=frozen_source(tmp_path,entries=[(name,b'{}',kind)])
    report=mod.run(protocol,tmp_path/'run',lambda url,headers:Response(body,url))
    assert report['objects_stream_scanned']==0 and report['uid_status_counts']=={'retrieval_gap':1}
    assert not (tmp_path/'run/records').exists()


def test_correct_member_name_with_wrong_original_post_hash_is_rejected(tmp_path):
    uid,post=post_record();changed=post+b' '
    protocol,_,body=frozen_source(tmp_path,entries=[('safe/'+uid+'.post',changed,tarfile.REGTYPE)])
    report=mod.run(protocol,tmp_path/'run',lambda url,headers:Response(body,url))
    assert report['uid_status_counts']=={'retrieval_gap':1}
    capture=json.loads(next((tmp_path/'run/objects').glob('*.json')).read_text())
    assert capture['identity_mismatches'][0]['uid_content_hash_valid'] is False


def test_truncated_compression_does_not_retain_preceding_valid_member(tmp_path):
    protocol,_,body=frozen_source(tmp_path);truncated=body[:-5]
    report=mod.run(protocol,tmp_path/'run',lambda url,headers:Response(truncated,url,{'Content-Length':str(len(body)),'ETag':'"synthetic-etag"'}))
    assert report['objects_stream_scanned']==0 and not (tmp_path/'run/records').exists()


def test_size_or_frozen_hash_refuses_all_requests(tmp_path):
    protocol,frozen,_=frozen_source(tmp_path,size=100_000_001)
    assert not frozen['download_eligible']
    with pytest.raises(ValueError,match='100 MB'):
        mod.run(protocol,tmp_path/'run',lambda *args:pytest.fail('network'))
    (protocol/'collector_source.py').write_text('changed')
    with pytest.raises(ValueError,match='protocol hash'):
        mod.run(protocol,tmp_path/'run',lambda *args:pytest.fail('network'))


def test_post_member_and_decompressed_limits_leave_gap(tmp_path,monkeypatch):
    monkeypatch.setitem(mod.LIMITS,'max_post_member_bytes',10)
    protocol,_,body=frozen_source(tmp_path)
    report=mod.run(protocol,tmp_path/'run',lambda url,headers:Response(body,url))
    assert report['objects_stream_scanned']==0 and not (tmp_path/'run/records').exists()
