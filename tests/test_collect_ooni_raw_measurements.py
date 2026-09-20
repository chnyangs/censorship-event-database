"""Synthetic identity/capture fixtures; never raw-measurement research evidence."""
import json
from pathlib import Path
import urllib.error
import urllib.request

import pytest

import collect_ooni_raw_measurements as mod


def metadata(uid='synthetic-a',anomaly=True):
    return {'measurement_uid':uid,'measurement_url':'https://api.ooni.io/api/v1/raw_measurement?measurement_uid='+uid,
            'report_id':'synthetic-report','input':'https://example.test/', 'probe_cc':'ET','probe_asn':'AS123',
            'test_name':'web_connectivity','measurement_start_time':'2025-11-01T09:49:53.000000Z',
            'anomaly':anomaly,'confirmed':False,'failure':False}


def raw_record(meta=None):
    meta=meta or metadata()
    raw={k:meta[k] for k in mod.IDENTITY_FIELDS}
    raw['measurement_start_time']='2025-11-01 09:49:53'
    raw['test_keys']={'blocking':'dns','accessible':None,'control_failure':None,
                      'control':{'dns':{'addrs':['192.0.2.1']}},'requests':[{'failure':'synthetic-timeout'}]}
    return raw


def source_fixture(path):
    path.mkdir();a=metadata();b=metadata('synthetic-b',False)
    planned=[{'query_id':'q1','event_id':'synthetic-event'},{'query_id':'q2','event_id':'synthetic-event'}]
    summaries=[]
    for query,rows in zip(planned,[[a],[a,b]]):
        directory=path/'captures'/query['query_id'];directory.mkdir(parents=True)
        body=json.dumps({'results':rows}).encode();(directory/'page.body').write_bytes(body)
        item={'query':query,'status':'complete','pagination_complete':True,'retrieved_rows':len(rows),
              'measurement_rows':rows,'pages':[{'body_file':'page.body','body_sha256':mod.sha(body)}]}
        mod.write_json(directory/'summary.json',item);summaries.append(item)
    mod.write_json(path/'manifest.json',{'query_count':2,'queries':planned})
    mod.write_json(path/'summary.json',{'status':'complete','query_count':2,'complete_queries':2,'failed_or_incomplete_queries':0})
    mod.write_json(path/'query_summaries.json',summaries)
    return path


def test_freeze_waits_for_final_metadata_frame(tmp_path):
    source=tmp_path/'source';source.mkdir()
    with pytest.raises(ValueError,match='wait for metadata run completion'):
        mod.freeze(source,tmp_path/'protocol',2)
    source.rmdir();source_fixture(source)
    with pytest.raises(ValueError,match='entire declared query frame'):
        mod.freeze(source,tmp_path/'protocol',624)
    assert not (tmp_path/'protocol').exists()


def test_freeze_keeps_anomaly_nonanomaly_and_duplicate_provenance(tmp_path):
    source=source_fixture(tmp_path/'source');protocol=tmp_path/'protocol'
    result=mod.freeze(source,protocol,2)
    assert result['metadata_row_appearances']==3 and result['distinct_metadata_rows']==2
    assert result['distinct_raw_urls']==2
    assert {r['metadata']['anomaly'] for r in result['metadata_rows']}=={True,False}
    assert sorted(len(r['query_references']) for r in result['metadata_rows'])==[1,2]
    assert result['censorship_finding'] is None and result['human_review_complete'] is False
    with pytest.raises(ValueError,match='overwrite'):mod.freeze(source,protocol,2)


def test_source_capture_changes_prevent_freeze_and_run(tmp_path):
    source=source_fixture(tmp_path/'source');protocol=tmp_path/'protocol'
    mod.freeze(source,protocol,2)
    (source/'captures/q1/page.body').write_bytes(b'changed')
    with pytest.raises(ValueError,match='body hash mismatch'):mod.freeze(source,tmp_path/'second',2)
    calls=[]
    with pytest.raises(ValueError,match='source changed'):
        mod.run(protocol,tmp_path/'run',fetch=lambda *args:calls.append(args))
    assert not calls and not (tmp_path/'run').exists()


@pytest.mark.parametrize('url',[
    'http://api.ooni.io/api/v1/raw_measurement?measurement_uid=x',
    'https://example.test/api/v1/raw_measurement?measurement_uid=x',
    'https://api.ooni.io:bad/api/v1/raw_measurement?measurement_uid=x',
    'https://api.ooni.io/api/v1/measurements?measurement_uid=x',
    'https://api.ooni.io/api/v1/raw_measurement?measurement_uid=x&measurement_uid=y',
])
def test_invalid_locator_is_explicit_not_fetched(url):
    assert mod.locator_error(url) is not None


def test_legacy_raw_utc_timestamp_and_optional_uid_are_explicit():
    result=mod.validate_identity(raw_record(),metadata())
    assert result['valid'] and result['raw_uid_status']=='not_exposed_by_raw'
    assert result['legacy_naive_raw_time_interpreted_as_utc']
    altered=raw_record();altered['probe_asn']=123
    assert mod.validate_identity(altered,metadata())['valid']


@pytest.mark.parametrize('field,value',[
    ('probe_cc','TH'),('probe_asn','AS999'),('input','https://other.test/'),
    ('report_id','wrong'),('report_id',''),('test_name','dnscheck'),
    ('measurement_start_time','2025-11-01 09:49:54'),('measurement_uid','wrong'),
])
def test_raw_identity_mismatch_is_not_valid_evidence(field,value):
    raw=raw_record();raw[field]=value
    assert not mod.validate_identity(raw,metadata())['valid']


def test_review_fields_preserve_control_failures_without_adjudication():
    result=mod.review_fields(raw_record())
    assert result['test_keys']['blocking']=='dns'
    assert result['test_keys']['control']['dns']['addrs']==['192.0.2.1']
    assert any(f['json_pointer']=='/test_keys/requests/0/failure' for f in result['failure_fields'])
    assert result['censorship_finding'] is None and result['human_review_complete'] is False


def test_successful_raw_collection_keeps_body_hash_and_identity_checks(tmp_path):
    row={'metadata_row_id':'synthetic-row','metadata':metadata()}
    body=json.dumps(raw_record()).encode()
    def fetch(url,limits,limiter):
        return {'http_status':200,'transport_error':None,'headers':{},'truncated':False},body
    result=mod.collect_url(row['metadata']['measurement_url'],[row],tmp_path,mod.LIMITS,None,fetch)
    assert result['status']=='retrieved_identity_valid' and len(result['attempts'])==1
    capture=result['attempts'][0]
    assert mod.sha(Path(capture['body_path']).read_bytes())==capture['body_sha256']
    assert result['identity_checks'][0]['valid'] and result['censorship_finding'] is None


def test_timeout_and_truncated_body_remain_retrieval_gaps(tmp_path):
    row={'metadata_row_id':'synthetic-row','metadata':metadata()}
    def fetch(url,limits,limiter):
        return {'http_status':None,'transport_error':'Timeout','headers':{},'truncated':False},b''
    result=mod.collect_url(row['metadata']['measurement_url'],[row],tmp_path,mod.LIMITS,None,fetch)
    assert result['status']=='retrieval_gap' and len(result['attempts'])==2
    assert result['identity_checks']==[] and result['censorship_finding'] is None


@pytest.mark.parametrize('url',['https://example.test/raw','http://api.ooni.io/raw','https://api.ooni.io:bad/raw',
                              'https://api.ooni.io/api/v1/measurements?measurement_uid=synthetic-a',
                              'https://api.ooni.io/api/v1/raw_measurement?measurement_uid=other-record',
                              'https://api.ooni.io/api/v1/raw_measurement?measurement_uid=synthetic-a&measurement_uid=other-record'])
def test_cross_host_or_insecure_redirect_is_refused(url):
    redirect=mod.SameHostRedirect(metadata()['measurement_url'])
    request=urllib.request.Request(metadata()['measurement_url'])
    with pytest.raises(urllib.error.HTTPError):redirect.redirect_request(request,None,302,'Found',{},url)


def test_excessive_retry_after_stops_without_waiting(tmp_path):
    row={'metadata_row_id':'synthetic-row','metadata':metadata()}
    def fetch(url,limits,limiter):
        return {'http_status':429,'transport_error':'rate limited','headers':{'Retry-After':'3600'},'truncated':False},b''
    result=mod.collect_url(row['metadata']['measurement_url'],[row],tmp_path,mod.LIMITS,None,fetch)
    assert len(result['attempts'])==1 and 'bounded wait' in result['retry_stop_reason']


@pytest.mark.parametrize('status,headers',[(429,{}),(503,{}),(429,{'Retry-After':'not-a-duration'})])
def test_rate_limit_without_usable_header_does_not_retry(tmp_path,status,headers):
    row={'metadata_row_id':'synthetic-row','metadata':metadata()}
    def fetch(url,limits,limiter):
        return {'http_status':status,'transport_error':'temporarily unavailable','headers':headers,'truncated':False},b''
    result=mod.collect_url(row['metadata']['measurement_url'],[row],tmp_path,mod.LIMITS,None,fetch)
    assert len(result['attempts'])==1 and result['status']=='retrieval_gap'


def test_source_paths_are_bound_independently_of_working_directory(tmp_path,monkeypatch):
    source_fixture(tmp_path/'source')
    monkeypatch.chdir(tmp_path)
    result=mod.freeze(Path('source'),Path('protocol'),2)
    assert all(Path(row['path']).is_absolute() for row in result['metadata_source_hashes'])
    assert Path(result['metadata_source_directory']).is_absolute()


def test_truncated_http200_never_yields_identity_valid_result(tmp_path):
    row={'metadata_row_id':'synthetic-row','metadata':metadata()}
    def fetch(url,limits,limiter):
        return {'http_status':200,'transport_error':'Body exceeds limit','headers':{},'truncated':True},b'{'
    result=mod.collect_url(row['metadata']['measurement_url'],[row],tmp_path,mod.LIMITS,None,fetch)
    assert result['status']=='retrieval_gap' and not result['identity_checks']


def retry_fixture(tmp_path,complete=True,rows=None):
    source=source_fixture(tmp_path/'source')
    summaries=json.loads((source/'query_summaries.json').read_text())
    summaries[1].update(status='incomplete',pagination_complete=False)
    mod.write_json(source/'captures/q2/summary.json',summaries[1])
    mod.write_json(source/'query_summaries.json',summaries)
    mod.write_json(source/'summary.json',{'status':'partial','query_count':2,'complete_queries':1,'failed_or_incomplete_queries':1})
    retry=tmp_path/'retry';retry.mkdir()
    retry_rows=rows if rows is not None else [metadata(),metadata('synthetic-c',False)]
    query=summaries[1]['query'];directory=retry/'captures/q2';directory.mkdir(parents=True)
    body=json.dumps({'results':retry_rows}).encode();(directory/'retry.body').write_bytes(body)
    item={'query':query,'status':'complete' if complete else 'incomplete','pagination_complete':complete,
          'retrieved_rows':len(retry_rows),'measurement_rows':retry_rows,
          'pages':[{'body_file':'retry.body','body_sha256':mod.sha(body)}]}
    manifest={'status':'frozen_before_retry_requests','source_directory':str(source),
              'source_manifest_sha256':mod.sha((source/'manifest.json').read_bytes()),
              'source_query_summaries_sha256':mod.sha((source/'query_summaries.json').read_bytes()),
              'source_summary_sha256':mod.sha((source/'summary.json').read_bytes()),
              'retry_query_count':1,'queries':[query]}
    mod.write_json(retry/'manifest.json',manifest)
    mod.write_json(retry/'captures/q2/summary.json',item)
    mod.write_json(retry/'query_summaries.json',[item])
    mod.write_json(retry/'summary.json',{'status':'complete' if complete else 'partial','retry_query_count':1,
                                       'completed_retries':int(complete),'still_incomplete':int(not complete)})
    return source,retry


def test_complete_retry_upgrades_query_but_retains_all_primary_rows_and_provenance(tmp_path):
    source,retry=retry_fixture(tmp_path)
    result=mod.freeze(source,tmp_path/'protocol',2,retry)
    assert result['metadata_primary_frame_status']=='partial'
    assert result['metadata_frame_status']=='complete'
    assert result['metadata_complete_queries_after_retry']==2
    assert result['metadata_row_appearances']==5 and result['distinct_metadata_rows']==3
    rows={r['metadata']['measurement_uid']:r for r in result['metadata_rows']}
    assert set(rows)=={'synthetic-a','synthetic-b','synthetic-c'}
    assert {r['metadata_run'] for r in rows['synthetic-a']['query_references']}=={'primary','retry'}
    assert rows['synthetic-b']['query_references'][0]['metadata_run']=='primary'
    assert all(r['query_summary_sha256'] for r in rows['synthetic-a']['query_references'])
    selected={q['query_id']:q for q in result['metadata_effective_query_summaries']}
    assert selected['q2']['selected_metadata_run']=='retry' and selected['q2']['pagination_complete']
    assert (tmp_path/'protocol/retry_metadata_manifest.json').is_file()
    assert {h['metadata_run'] for h in result['metadata_source_hashes']}=={'primary','retry'}
    assert {r['metadata']['anomaly'] for r in result['metadata_rows']}=={True,False}


def test_incomplete_retry_retains_both_runs_without_upgrading_completeness(tmp_path):
    source,retry=retry_fixture(tmp_path,complete=False,rows=[metadata('synthetic-c',False)])
    result=mod.freeze(source,tmp_path/'protocol',2,retry)
    assert result['metadata_frame_status']=='partial'
    assert result['metadata_incomplete_queries_after_retry']==1
    assert result['distinct_metadata_rows']==3 and result['metadata_row_appearances']==4
    selected={q['query_id']:q for q in result['metadata_effective_query_summaries']}
    assert selected['q2']['selected_metadata_run']=='primary' and not selected['q2']['pagination_complete']
    assert selected['q2']['retry_available']


@pytest.mark.parametrize('key',['source_manifest_sha256','source_query_summaries_sha256','source_summary_sha256'])
def test_retry_overlay_rejects_changed_parent_hash(tmp_path,key):
    source,retry=retry_fixture(tmp_path)
    manifest=json.loads((retry/'manifest.json').read_text());manifest[key]='sha256:'+'0'*64
    mod.write_json(retry/'manifest.json',manifest)
    with pytest.raises(ValueError,match='parent source hash mismatch'):
        mod.freeze(source,tmp_path/'protocol',2,retry)
    assert not (tmp_path/'protocol').exists()


@pytest.mark.parametrize('change',['omit','add_complete','identity','duplicate'])
def test_retry_overlay_rejects_wrong_query_set_or_identity(tmp_path,change):
    source,retry=retry_fixture(tmp_path)
    manifest=json.loads((retry/'manifest.json').read_text())
    if change=='omit':manifest['queries']=[]
    elif change=='add_complete':manifest['queries'].append({'query_id':'q1','event_id':'synthetic-event'})
    elif change=='identity':manifest['queries'][0]['event_id']='changed-event'
    else:manifest['queries'].append(manifest['queries'][0])
    mod.write_json(retry/'manifest.json',manifest)
    with pytest.raises(ValueError,match='Retry (set|query identity)'):
        mod.freeze(source,tmp_path/'protocol',2,retry)


def test_retry_capture_and_summary_hashes_are_bound_before_raw_requests(tmp_path):
    source,retry=retry_fixture(tmp_path)
    protocol=tmp_path/'protocol';mod.freeze(source,protocol,2,retry)
    (retry/'captures/q2/retry.body').write_bytes(b'changed retry body')
    with pytest.raises(ValueError,match='body hash mismatch'):
        mod.freeze(source,tmp_path/'second',2,retry)
    calls=[]
    with pytest.raises(ValueError,match='source changed'):
        mod.run(protocol,tmp_path/'run',fetch=lambda *args:calls.append(args))
    assert not calls and not (tmp_path/'run').exists()


def test_retry_requires_final_outputs_and_consistent_completion_accounting(tmp_path):
    source,retry=retry_fixture(tmp_path)
    (retry/'summary.json').unlink()
    with pytest.raises(ValueError,match='wait for metadata run completion'):
        mod.freeze(source,tmp_path/'protocol',2,retry)
    mod.write_json(retry/'summary.json',{'status':'complete','retry_query_count':1,'completed_retries':0,'still_incomplete':1})
    with pytest.raises(ValueError,match='Retry final completion accounting'):
        mod.freeze(source,tmp_path/'protocol',2,retry)


def test_retry_paths_are_absolute_and_checked_after_cwd_changes(tmp_path,monkeypatch):
    source,retry=retry_fixture(tmp_path)
    monkeypatch.chdir(tmp_path)
    result=mod.freeze(Path('source'),Path('protocol'),2,Path('retry'))
    assert Path(result['metadata_retry_directory']).is_absolute()
    assert all(Path(row['path']).is_absolute() for row in result['metadata_source_hashes'])
    monkeypatch.chdir(tmp_path.parent)
    def fetch(url,limits,limiter):
        uid=url.rsplit('=',1)[-1]
        return {'http_status':200,'transport_error':None,'headers':{},'truncated':False},json.dumps(raw_record(metadata(uid))).encode()
    report=mod.run(tmp_path/'protocol',tmp_path/'run',fetch=fetch)
    assert report['frozen_raw_urls']==3 and report['identity_valid_metadata_rows']==3
