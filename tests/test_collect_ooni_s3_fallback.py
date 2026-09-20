"""Synthetic S3 and OONI fixtures only; no live requests or research outcomes."""
import gzip
import hashlib
import io
import json
from pathlib import Path
import urllib.parse
import xml.etree.ElementTree as ET

import pytest

import collect_ooni_s3_fallback as mod


UID='20251015060213.849829_ET_webconnectivity_c5425aac65a93796'
OTHER_UID='20251015060226.070977_ET_webconnectivity_88e332665bc76b0b'
PREFIX='raw/20251015/06/ET/webconnectivity/'
KEY=PREFIX+'2025101506_ET_webconnectivity.n0.0.jsonl.gz'


def metadata(uid=UID,anomaly=True):
    return {'measurement_uid':uid,'measurement_url':'https://api.ooni.io/api/v1/raw_measurement?measurement_uid='+uid,
            'report_id':'synthetic-report','input':'https://example.test/','probe_cc':'ET','probe_asn':'AS123',
            'test_name':'web_connectivity','measurement_start_time':'2025-10-15T06:01:49Z','anomaly':anomaly}


def raw_record(uid=UID):
    record={k:v for k,v in metadata(uid).items() if k not in {'measurement_url','anomaly'}}
    record['test_keys']={'blocking':'dns','control_failure':None,'control':{'dns':{'addrs':['192.0.2.1']}}}
    return record


def xml_page(objects=(),truncated=False,token=None,following=None,prefix=PREFIX):
    root=ET.Element('ListBucketResult',xmlns='http://s3.amazonaws.com/doc/2006-03-01/')
    fields={'Name':mod.BUCKET,'Prefix':prefix,'KeyCount':str(len(objects)),'MaxKeys':'1000','IsTruncated':str(truncated).lower()}
    if token is not None:fields['ContinuationToken']=token
    if following is not None:fields['NextContinuationToken']=following
    for name,value in fields.items():ET.SubElement(root,name).text=value
    for key,size in objects:
        item=ET.SubElement(root,'Contents')
        for name,value in [('Key',key),('Size',str(size)),('ETag','"synthetic-etag"'),('LastModified','2025-10-15T07:00:00Z')]:
            ET.SubElement(item,name).text=value
    return ET.tostring(root)


class Response(io.BytesIO):
    def __init__(self,body,url,headers=None,status=200):
        super().__init__(body);self.url=url;self.status=status
        self.headers=headers or {'Content-Length':str(len(body)),'ETag':'"synthetic-etag"'}


@pytest.fixture(autouse=True)
def no_wait(monkeypatch):
    monkeypatch.setattr(mod.raw_api.RateLimiter,'wait',lambda self:None)


def api_fixture(tmp_path,second_valid=False):
    protocol=tmp_path/'api_protocol';run=tmp_path/'api_run';protocol.mkdir();run.mkdir()
    rows=[];results=[]
    for index,uid in enumerate((UID,OTHER_UID)):
        meta=metadata(uid,bool(index));row={'metadata_row_id':str(index),'metadata':meta,'locator_validation_error':None}
        rows.append(row);valid=bool(index and second_valid)
        result={'measurement_url':meta['measurement_url'],'metadata_row_ids':[str(index)],'attempts':[],
                'status':'retrieved_identity_valid' if valid else 'retrieval_gap',
                'identity_checks':[{'metadata_row_id':str(index),'valid':True}] if valid else []}
        results.append(result)
        mod.write_json(run/'captures'/hashlib.sha256(meta['measurement_url'].encode()).hexdigest()/'result.json',result)
    mod.write_json(protocol/'manifest.json',{'metadata_rows':rows})
    mod.write_json(protocol/'freeze_hashes.json',{'files':{'manifest.json':mod.sha((protocol/'manifest.json').read_bytes())}})
    mod.write_json(run/'execution_manifest.json',{'protocol_sha256':mod.sha((protocol/'manifest.json').read_bytes())})
    mod.write_json(run/'results.json',results)
    mod.write_json(run/'summary.json',{'status':'raw_retrieval_partial','raw_urls_attempted':2,'frozen_raw_urls':2,
                                      'url_status_counts':dict(mod.Counter(r['status'] for r in results))})
    return protocol,run


def frozen_fixture(tmp_path,body=None,size=None):
    source,run=api_fixture(tmp_path)
    body=body if body is not None else gzip.compress((json.dumps(raw_record())+'\n').encode(),mtime=0)
    size=len(body) if size is None else size
    def listing(url,headers=None):
        assert 'list-type=2' in url
        return Response(xml_page([(KEY,size)]),url)
    out=tmp_path/'s3_protocol';manifest=mod.freeze(source,run,out,opener=listing)
    return out,manifest,body


def test_selection_waits_for_final_api_results_and_is_outcome_independent(tmp_path):
    source,run=api_fixture(tmp_path)
    rows,_=mod.select_unresolved(source,run)
    assert {r['metadata']['anomaly'] for r in rows}=={False,True}
    assert {r['s3_prefix'] for r in rows}=={PREFIX}
    (run/'summary.json').unlink()
    with pytest.raises(ValueError,match='Wait for final'):mod.select_unresolved(source,run)


def test_resolved_api_uid_excluded_and_changed_source_identity_rejected(tmp_path):
    source,run=api_fixture(tmp_path,second_valid=True)
    rows,_=mod.select_unresolved(source,run)
    assert [r['metadata']['measurement_uid'] for r in rows]==[UID]
    results=json.loads((run/'results.json').read_text());results[0]['metadata_row_ids']=['unrelated']
    mod.write_json(run/'results.json',results)
    with pytest.raises(ValueError,match='aggregate and preserved'):mod.select_unresolved(source,run)


@pytest.mark.parametrize('uid',[UID.replace('_ET_','_TH_'),UID.replace('20251015','20251315'),UID.replace('webconnectivity','dnscheck'),'../bad'])
def test_uid_prefix_refuses_wrong_country_test_or_time(uid):
    with pytest.raises(ValueError):mod.uid_prefix(metadata(uid))


def test_xml_pagination_capture_and_path_filter(tmp_path):
    keys=[KEY,KEY.replace('n0.0','n0.1')]
    calls=[]
    def opener(url,headers=None):
        calls.append(url)
        if len(calls)==1:return Response(xml_page([(keys[0],12)],True,following='next /+='),url)
        assert urllib.parse.parse_qs(urllib.parse.urlsplit(url).query)['continuation-token']==['next /+=']
        return Response(xml_page([(keys[1],34)],token='next /+='),url)
    result=mod.list_prefix(PREFIX,tmp_path/'list',mod.raw_api.RateLimiter(1),opener)
    assert result['pagination_complete'] and len(result['objects'])==2 and len(calls)==2
    for record,path in zip(result['pages'],sorted((tmp_path/'list').glob('*/response.xml'))):
        assert mod.sha(path.read_bytes())==record['body_sha256']


@pytest.mark.parametrize('objects,kwargs',[
    ([(KEY.replace('/ET/','/TH/'),10)],{}),([(PREFIX+'../x.jsonl.gz',10)],{}),
    ([(KEY,-1)],{}),([(KEY,1),(KEY,1)],{}),([],{'truncated':True}),
])
def test_invalid_s3_listing_rejected(objects,kwargs):
    with pytest.raises(ValueError):mod.parse_listing(xml_page(objects,**kwargs),PREFIX)


def test_repeated_token_or_incomplete_pagination_stays_gap(tmp_path):
    def opener(url,headers=None):
        token=urllib.parse.parse_qs(urllib.parse.urlsplit(url).query).get('continuation-token',[None])[0]
        return Response(xml_page([],True,token=token,following='repeat'),url)
    result=mod.list_prefix(PREFIX,tmp_path/'list',mod.raw_api.RateLimiter(1),opener)
    assert not result['pagination_complete'] and 'Repeated' in result['error']


def test_freeze_has_size_source_and_listing_hashes_without_object_get(tmp_path):
    protocol,manifest,body=frozen_fixture(tmp_path)
    assert manifest['download_eligible'] and manifest['object_downloads_performed']==0
    assert manifest['total_compressed_content_length']==len(body)
    for name,expected in json.loads((protocol/'freeze_hashes.json').read_text())['files'].items():
        assert mod.sha((protocol/name).read_bytes())==expected
    assert (protocol/'selection_before_listing.json').is_file()


def test_over_100mb_total_refuses_all_body_requests(tmp_path):
    protocol,manifest,_=frozen_fixture(tmp_path,size=100_000_001)
    assert not manifest['download_eligible']
    calls=[]
    with pytest.raises(ValueError,match='100 MB'):
        mod.run(protocol,tmp_path/'out',opener=lambda *args:calls.append(args))
    assert not calls and not (tmp_path/'out').exists()


def test_streamed_gzip_keeps_only_exact_uid_and_matching_identity(tmp_path):
    good=raw_record();other=raw_record('unrelated-uid');mismatch=raw_record(OTHER_UID);mismatch['probe_asn']='AS999'
    lines=[json.dumps(r).encode()+b'\n' for r in (other,good,mismatch)]
    body=gzip.compress(b''.join(lines),mtime=0);protocol,manifest,_=frozen_fixture(tmp_path,body)
    calls=[]
    def opener(url,headers=None):
        calls.append((url,headers));return Response(body,url)
    summary=mod.run(protocol,tmp_path/'out',opener)
    assert len(calls)==1 and calls[0][1]=={'If-Match':'"synthetic-etag"'}
    assert summary['uid_status_counts']=={'retrieved_identity_valid':1,'retrieval_gap':1}
    retained=list((tmp_path/'out/records').glob('*/measurement.jsonl'))
    assert len(retained)==1 and retained[0].read_bytes()==lines[1]
    capture=json.loads(next((tmp_path/'out/objects').glob('*.json')).read_text())
    assert capture['compressed_body_sha256']==mod.sha(body)
    assert len(capture['identity_mismatches'])==1
    assert summary['censorship_finding'] is None and not summary['human_review_complete']


@pytest.mark.parametrize('corruption',['gzip','length','etag','linecap'])
def test_invalid_object_is_gap_without_promoting_partial_records(tmp_path,corruption,monkeypatch):
    body=gzip.compress((json.dumps(raw_record())+'\n').encode(),mtime=0)
    if corruption=='gzip':body=body[:-6]
    if corruption=='linecap':monkeypatch.setitem(mod.LIMITS,'max_json_line_bytes',10)
    protocol,_,_=frozen_fixture(tmp_path,body)
    headers={'Content-Length':str(len(body)),'ETag':'"synthetic-etag"'}
    if corruption=='length':headers['Content-Length']=str(len(body)+1)
    if corruption=='etag':headers['ETag']='"changed"'
    summary=mod.run(protocol,tmp_path/'out',lambda url,headers_arg=None:Response(body,url,headers))
    assert summary['objects_stream_scanned']==0 and summary['identity_valid_metadata_rows']==0
    assert not (tmp_path/'out/records').exists()


def test_frozen_or_parent_hash_change_refuses_network(tmp_path):
    protocol,_,_=frozen_fixture(tmp_path)
    listing=next((protocol/'listings').glob('*/page_1/response.xml'));listing.write_bytes(b'changed')
    with pytest.raises(ValueError,match='protocol hash'):mod.run(protocol,tmp_path/'out',lambda *args:pytest.fail('network'))


def test_complete_empty_listing_stays_visible_uid_gap(tmp_path):
    source,run=api_fixture(tmp_path)
    protocol=tmp_path/'s3_protocol'
    frozen=mod.freeze(source,run,protocol,lambda url:Response(xml_page(),url))
    assert frozen['listing_complete'] and frozen['download_eligible']
    assert not frozen['every_selected_prefix_has_jsonl_gzip_object']
    assert frozen['empty_jsonl_gzip_prefixes']==[PREFIX]
    result=mod.run(protocol,tmp_path/'out',lambda *args:pytest.fail('body request for empty listing'))
    assert result['uid_status_counts']=={'retrieval_gap':2} and result['objects_attempted']==0
