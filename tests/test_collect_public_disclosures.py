"""Synthetic fixtures protect disclosure scope and completeness semantics."""
import json
from pathlib import Path

import pytest

import collect_public_disclosures as mod


def action():
    return {'action_url':'https://ofac.treasury.gov/recent-actions/20220405',
            'window_start_inclusive_utc':'2022-03-29T00:00:00Z',
            'window_end_exclusive_utc':'2022-05-06T00:00:00Z',
            'targets':[{'measurement_unit_id':'synthetic-unit','normalized_address':'0x'+'a'*40,
                        'lexical_queries':[{'query':'Example Target','normalized_query':'example target','derivation':'synthetic'}]}]}


def post(number=1, text='Unrelated content', date='2022-04-05T12:00:00'):
    return {'id':number,'status':'publish','date_gmt':date,'link':f'https://blog.kraken.com/p{number}',
            'title':{'rendered':'Research fixture'},'content':{'rendered':text,'protected':False}}


class FakeFetcher:
    limits=mod.LIMITS
    def __init__(self, pages):self.pages=iter(pages);self.urls=[]
    def get(self,url):
        self.urls.append(url)
        posts,total,pages=next(self.pages)
        return {'url':url,'status':'retrieved','body':json.dumps(posts).encode(),
                'headers':{'X-WP-Total':str(total),'X-WP-TotalPages':str(pages)},
                'attempts':[{'capture_path':'fixture-only'}]}


def test_only_complete_archive_unlocks_lexical_negative():
    fetch=FakeFetcher([([post()],1,1)])
    result=mod.wordpress_window(fetch,mod.PANELS['kraken'],action())
    assert result['archive_enumeration_complete'] is True
    assert result['target_results'][0]['outcome']=='no_disclosure_found_under_enumerated_archive'
    assert result['target_results'][0]['private_account_action'] is None
    assert '2022-03-28' in fetch.urls[0] and '2022-05-07' in fetch.urls[0]


@pytest.mark.parametrize('posts,total,pages', [
    ([post()],2,1), ([post()],1,0), ([post(date='')],1,1),
    ([{**post(),'content':{'rendered':'','protected':True}}],1,1),
    ([{**post(),'status':'draft'}],1,1),
])
def test_incomplete_or_unreadable_archive_cannot_be_negative(posts,total,pages):
    result=mod.wordpress_window(FakeFetcher([(posts,total,pages)]),mod.PANELS['kraken'],action())
    assert result['archive_enumeration_complete'] is False
    assert result['target_results'][0]['outcome'] in {'gap','partial'}


def test_empty_enumerated_archive_is_narrow_negative():
    result=mod.wordpress_window(FakeFetcher([([],0,0)]),mod.PANELS['kraken'],action())
    assert result['archive_enumeration_complete']
    assert result['target_results'][0]['outcome']=='no_disclosure_found_under_enumerated_archive'


def test_publication_window_and_visible_exact_name_are_required():
    docs=[{'url':'https://example.test','published_at_utc':'2022-05-06T00:00:00Z',
           'text':'Example Target','source_capture':'fixture'}]
    row=mod.evaluate_documents(action(),docs,False,'partial')[0]
    assert not row['matches'] and row['outcome']=='partial'
    docs[0]['published_at_utc']='2022-04-05T10:00:00Z'
    row=mod.evaluate_documents(action(),docs,False,'partial')[0]
    assert row['outcome']=='disclosure_found' and row['human_adjudication']=='pending'
    assert not mod.exact_matches('Example Targeting',action()['targets'][0]['lexical_queries'])
    assert 'Example Target' not in mod.body_text('<script>Example Target</script><main>News</main>')


def test_undated_match_never_becomes_dated_disclosure():
    docs=[{'url':'https://example.test','published_at_utc':None,'text':'Example Target','source_capture':'fixture'}]
    row=mod.evaluate_documents(action(),docs,True,'synthetic')[0]
    assert row['outcome']=='partial' and len(row['undated_matches'])==1


def test_fetch_errors_are_captured_twice_and_not_zero(tmp_path):
    calls=[]
    def request(url,panel,limits):
        calls.append(url)
        return {'http_status':403,'error':'Forbidden','headers':{},'final_url':url},b'Forbidden'
    fetch=mod.Fetcher(tmp_path,mod.PANELS['kraken'],mod.LIMITS,request)
    result=fetch.get('https://blog.kraken.com/wp-json/')
    assert result['status']=='gap' and len(calls)==2
    for record in result['attempts']:
        raw=(Path(record['capture_path'])/'response.body').read_bytes()
        assert record['response_body_sha256']==mod.sha(raw)
    assert fetch.get('https://blog.kraken.com/wp-json/') is result and len(calls)==2
    assert fetch.get('https://example.net/')['status']=='off_panel_refused'


def test_hash_mismatch_and_existing_output_stop_before_network(tmp_path):
    protocol=tmp_path/'protocol';protocol.mkdir()
    (protocol/'manifest.json').write_text('{}')
    mod.write_json(protocol/'freeze_hashes.json',{'files':{'manifest.json':'sha256:wrong'}})
    calls=[]
    with pytest.raises(ValueError,match='hash mismatch'):
        mod.run(protocol,tmp_path/'run',request=lambda *args:calls.append(args))
    assert not calls and not (tmp_path/'run').exists()
    with pytest.raises(ValueError,match='overwrite'):
        mod.run(protocol,protocol)


def test_source_aliases_include_address_but_no_person_surname_only():
    record={'entry_text':'GRIMM, Matthew Simon; Digital Currency Address - ETH 0x'+'a'*40,
            'target_entry_prefix_candidate':'GRIMM, Matthew Simon, Bristol, United Kingdom',
            'normalized_address':'0x'+'a'*40}
    queries={q['normalized_query'] for q in mod.aliases_from_record(record)}
    assert 'grimm matthew simon' in queries and 'matthew simon grimm' in queries
    assert 'grimm' not in queries and '0x'+'a'*40 in queries


def test_date_only_html_metadata_is_not_an_exact_utc_timestamp():
    row={'url':'https://example.test','body':b'<meta property="article:published_time" content="2022-04-05"><main>Example Target</main>',
         'attempts':[{'capture_path':'fixture'}]}
    assert mod.article_document(row)['published_at_utc'] is None


def test_scope_indices_and_exact_english_locale_precede_other_locales():
    urls=['https://www.binance.com/sitemap_Blog_ar_0.xml',
          'https://www.binance.com/sitemap_Blog_en-AU_0.xml',
          'https://www.binance.com/sitemap_Blog_en_0.xml',
          'https://www.binance.com/sitemap_SupportAndAnnouncement_index.xml',
          'https://www.binance.com/sitemap_Blog_index.xml']
    ordered=sorted(urls,key=mod.sitemap_priority)
    assert all(url.endswith('_index.xml') for url in ordered[:2])
    assert ordered[2].endswith('Blog_en_0.xml')
