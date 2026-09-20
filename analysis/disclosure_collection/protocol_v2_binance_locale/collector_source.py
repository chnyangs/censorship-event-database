#!/usr/bin/env python3
"""Freeze and collect bounded official public disclosures; never private outcomes.

Current public archive enumeration is distinct from historical archive survival.
Names/addresses and UTC windows are frozen before any network collection.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta, timezone
import gzip
import hashlib
import html
import io
import json
from pathlib import Path
import re
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
PANELS = {
    'coinbase': {'indices': ['https://www.coinbase.com/blog'], 'robots': 'https://www.coinbase.com/robots.txt', 'domain': 'coinbase.com', 'article_paths': ['/blog/']},
    'kraken': {'indices': ['https://blog.kraken.com/'], 'robots': 'https://blog.kraken.com/robots.txt', 'domain': 'kraken.com', 'article_paths': ['/'], 'wp_api': 'https://blog.kraken.com/wp-json/', 'wp_documentation_capture': 'sources/measurement_panel/kraken_index/attempt_1/response.body'},
    'binance': {'indices': ['https://www.binance.com/en/support/announcement', 'https://www.binance.com/en/blog'], 'robots': 'https://www.binance.com/robots.txt', 'domain': 'binance.com', 'article_paths': ['/en/support/announcement/', '/en/blog/']},
}
LIMITS = {'max_endpoint_queries_per_operator': 40, 'max_attempts_per_endpoint': 2, 'timeout_seconds': 12,
          'max_response_bytes': 8_000_000, 'max_sitemap_documents': 8, 'max_article_documents': 16,
          'max_wp_pages_per_window': 3, 'wp_page_size': 100, 'operator_workers': 3}


def now():
    return datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')


def sha(raw):
    return 'sha256:' + hashlib.sha256(raw).hexdigest()


def canonical(obj):
    return json.dumps(obj, sort_keys=True, ensure_ascii=False, separators=(',', ':'))


def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False) + '\n')


def normalize(text):
    return ' '.join(re.sub(r'[^\w]+', ' ', unicodedata.normalize('NFKC', text).casefold()).split())


def exact_matches(text, queries):
    haystack = ' ' + normalize(text) + ' '
    return [q for q in queries if ' ' + q['normalized_query'] + ' ' in haystack]


def aliases_from_record(record):
    entry = record['entry_text']
    head = record['target_entry_prefix_candidate'].split(' (')[0]
    parts = [part.strip() for part in head.split(',')]
    names = [', '.join(parts[:2]) if len(parts) > 1 else head]
    for quoted, plain in re.findall(r'a\.k\.a\.\s*(?:"([^"]+)"|([^;)]+))', entry, re.I):
        names.append((quoted or plain).split(' (')[0].strip())
    terms = [(name, 'source_name_or_alias') for name in names]
    for name in names:
        bits = [part.strip() for part in name.split(',')]
        if len(bits) == 2 and bits[1].strip('.').upper() not in {'INC', 'LLC', 'LTD', 'OU'}:
            terms.append((bits[1] + ' ' + bits[0], 'source_name_reordered'))
    for website in re.findall(r'Website ([^;]+)', entry):
        host = urllib.parse.urlsplit(website if '://' in website else 'https://' + website).hostname
        if host:
            terms.append((host.removeprefix('www.'), 'source_website_host'))
            label = host.removeprefix('www.').split('.')[0]
            if len(label) >= 6:
                terms.append((label, 'source_website_label_machine_alias'))
    terms.append((record['normalized_address'], 'source_address'))
    return [{'query': value, 'normalized_query': normalize(value), 'derivation': kind}
            for value, kind in terms if len(normalize(value)) >= 4]


def freeze(candidate_dir, out, operators=None):
    if out.exists():
        raise ValueError('Refusing to overwrite frozen disclosure protocol')
    bundle_path = candidate_dir / 'bundle.sha256.json'
    bundle = json.loads(bundle_path.read_text())
    for name, expected in bundle['files'].items():
        if Path(name).name != name or sha((candidate_dir / name).read_bytes()) != expected:
            raise ValueError('Candidate bundle hash mismatch: ' + name)
    units = [json.loads(line) for line in (candidate_dir / 'measurement_units.jsonl').read_text().splitlines()]
    sources = {r['source_row_id']: r for r in map(json.loads, (candidate_dir / 'source_rows.jsonl').read_text().splitlines())}
    actions = defaultdict(list)
    for unit in units:
        terms = {}
        for row_id in unit['source_row_ids']:
            original = sources[row_id]
            if original['machine_disposition'] != 'machine_candidate':
                raise ValueError('Unit references a noncandidate source row')
            for term in aliases_from_record(original['source_record']):
                terms.setdefault(term['normalized_query'], term)
        actions[unit['action_url']].append({**unit, 'lexical_queries': sorted(terms.values(), key=lambda q:q['normalized_query'])})
    windows = []
    for url, members in sorted(actions.items()):
        times = {(u['window_start_inclusive_utc'], u['window_end_exclusive_utc']) for u in members}
        if len(times) != 1:
            raise ValueError('Inconsistent action window')
        start, end = next(iter(times))
        windows.append({'action_url': url, 'action_slug': members[0]['action_slug'], 'window_start_inclusive_utc': start,
                        'window_end_exclusive_utc': end, 'targets': members})
    selected=tuple(operators or PANELS)
    if len(set(selected))!=len(selected) or set(selected)-set(PANELS):
        raise ValueError('Unknown or duplicate operator selection')
    panels = json.loads(json.dumps({name:PANELS[name] for name in selected}))
    if 'kraken' in panels:
        documented = ROOT / panels['kraken']['wp_documentation_capture']
        soup = BeautifulSoup(documented.read_bytes(), 'html.parser')
        if not any(tag.get('href') == panels['kraken']['wp_api'] for tag in soup.find_all('link', rel='https://api.w.org/')):
            raise ValueError('WordPress discovery endpoint is not linked by captured official index')
        panels['kraken']['wp_documentation_capture_sha256'] = sha(documented.read_bytes())
    manifest = {'protocol_version': 'official-public-disclosure-v1.1-locale-order', 'status': 'frozen_before_collection_machine_not_human_adjudicated',
                'frozen_at_utc': now(), 'candidate_bundle_sha256': sha(bundle_path.read_bytes()),
                'candidate_directory': str(candidate_dir), 'collector_sha256': sha(Path(__file__).read_bytes()),
                'operators': panels, 'limits': LIMITS, 'actions': windows,
                'action_count': len(windows), 'candidate_target_units': len(units), 'operator_action_windows': len(windows)*len(panels),
                'query_semantics': 'Exact NFKC-casefolded word-sequence matching after punctuation-to-space normalization; no stemming, LLM matching, or outcome-derived synonyms. Addresses exact. Website labels are machine alias proposals, not adjudicated target identity.',
                'selection_rule': 'All actions and candidate target units in the frozen issuer manifest; no outcome-based target/operator/window selection.',
                'window_rule': 'Inherited UTC[d-7,d+31); retrieve WordPress date filters with one-day buffers then filter using date_gmt.',
                'enumeration_rule': 'Kraken documented WordPress posts REST route if discoverable, chronological100posts/page, maximum3pages/window with page-count checks. Otherwise official indices plus robots-declared sitemap traversal, max8documents/operator; prioritize blog/support/announcement root indices, then exact en locale, then remaining scope sitemaps, then lexical URL order. Fetch up to16 lexical URL/anchor matches sorted lexicographically. Sitemap lastmod is never publication time.',
                'negative_rule': 'No disclosure found only after complete current public WordPress archive enumeration, all pages/items accounted for and readable content/dates. Otherwise gap or partial. Current archive survival and lexical recall remain limitations.',
                'forbidden_inference': 'No private account action, service access, actual enforcement, causal reaction, or independent-human truth follows from disclosure matching.',
                'human_reference_complete': False, 'outcome_queries_executed': 0}
    out.mkdir(parents=True)
    write_json(out/'manifest.json', manifest)
    (out/'collector_source.py').write_bytes(Path(__file__).read_bytes())
    (out/'candidate_bundle_index.json').write_bytes(bundle_path.read_bytes())
    write_json(out/'freeze_hashes.json', {'files': {name:sha((out/name).read_bytes()) for name in ['manifest.json','collector_source.py','candidate_bundle_index.json']}})
    return manifest


def allowed(url, panel):
    parts = urllib.parse.urlsplit(url)
    return parts.scheme == 'https' and bool(parts.hostname) and (parts.hostname == panel['domain'] or parts.hostname.endswith('.'+panel['domain']))


class RestrictedRedirect(urllib.request.HTTPRedirectHandler):
    def __init__(self, panel): self.panel = panel
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        if not allowed(newurl, self.panel):
            raise urllib.error.HTTPError(req.full_url, code, 'Off-panel redirect refused', headers, fp)
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def transport(url, panel, limits):
    start = now()
    record = {'requested_url':url, 'started_at_utc':start, 'http_status':None, 'error':None, 'headers':{}, 'final_url':url}
    raw = b''
    try:
        request = urllib.request.Request(url, headers={'User-Agent':'PublicDisclosureResearch/1.0 (bounded read-only archive collection)'})
        with urllib.request.build_opener(RestrictedRedirect(panel)).open(request, timeout=limits['timeout_seconds']) as response:
            record.update(http_status=response.status, final_url=response.url, headers=dict(response.headers.items()))
            raw=response.read(limits['max_response_bytes']+1)
    except urllib.error.HTTPError as exc:
        raw=exc.read(limits['max_response_bytes']+1)
        record.update(http_status=exc.code, error=str(exc), headers=dict(exc.headers.items()))
    except (OSError, TimeoutError, urllib.error.URLError) as exc:
        record['error']=f'{type(exc).__name__}: {exc}'
    if len(raw)>limits['max_response_bytes']:
        record['error']='Response exceeded frozen byte limit; retained prefix is not a complete body'
        record['truncated']=True
    record['finished_at_utc']=now()
    return record,raw


class Fetcher:
    def __init__(self, root, panel, limits, request=transport):
        self.root,self.panel,self.limits,self.request=root,panel,limits,request
        self.queries=[];self.cache={}
    def get(self,url):
        if url in self.cache:return self.cache[url]
        if not allowed(url,self.panel):return {'url':url,'status':'off_panel_refused','body':None}
        if len(self.queries)>=self.limits['max_endpoint_queries_per_operator']:
            return {'url':url,'status':'frozen_query_budget_exhausted','body':None}
        key=hashlib.sha256(url.encode()).hexdigest()[:24]
        entry={'url':url,'query_id':key,'attempts':[],'status':'gap','body':None}
        self.queries.append(entry)
        for number in range(1,self.limits['max_attempts_per_endpoint']+1):
            record,raw=self.request(url,self.panel,self.limits)
            dest=self.root/key/f'attempt_{number}';dest.mkdir(parents=True,exist_ok=False)
            (dest/'response.body').write_bytes(raw)
            record.update(response_body_sha256=sha(raw),response_bytes=len(raw),capture_path=str(dest))
            write_json(dest/'capture.json',record)
            entry['attempts'].append(record)
            if record['http_status']==200 and not record['error'] and allowed(record['final_url'],self.panel):
                entry.update(status='retrieved',body=raw,headers=record['headers']);break
        self.cache[url]=entry
        return entry
    def ledger(self):
        return [{k:v for k,v in row.items() if k!='body'} for row in self.queries]


def json_body(row):
    if row['status']!='retrieved':return None
    try:return json.loads(row['body'])
    except (ValueError,UnicodeDecodeError):return None


def utc(value, naive_is_gmt=False):
    try:
        stamp=datetime.fromisoformat(value.replace('Z','+00:00'))
        if stamp.tzinfo is None:
            if not naive_is_gmt:return None
            stamp=stamp.replace(tzinfo=timezone.utc)
        return stamp.astimezone(timezone.utc)
    except (ValueError,TypeError,AttributeError):return None


def body_text(markup):
    soup=BeautifulSoup(markup,'html.parser')
    for tag in soup(['script','style','nav','header','footer','aside']):tag.decompose()
    main=soup.find('article') or soup.find('main') or soup
    return ' '.join(main.stripped_strings)


def evaluate_documents(action,documents,complete,archive_status):
    start,end=utc(action['window_start_inclusive_utc']),utc(action['window_end_exclusive_utc'])
    results=[]
    for target in action['targets']:
        hits=[];undated=[]
        for doc in documents:
            matches=exact_matches(doc['text'],target['lexical_queries'])
            if not matches:continue
            stamp=utc(doc.get('published_at_utc'))
            item={'url':doc['url'],'published_at_utc':doc.get('published_at_utc'),'matched_queries':matches,'source_capture':doc['source_capture']}
            if stamp is None:undated.append(item)
            elif start<=stamp<end:hits.append(item)
        outcome='disclosure_found' if hits else 'no_disclosure_found_under_enumerated_archive' if complete and not undated else 'partial' if documents else 'gap'
        results.append({'measurement_unit_id':target['measurement_unit_id'],'target_address':target['normalized_address'],
                        'outcome':outcome,'matches':hits,'undated_matches':undated,'archive_status':archive_status,
                        'archive_enumeration_complete':complete,'human_adjudication':'pending','private_account_action':None})
    return results


def wordpress_window(fetcher,panel,action):
    start=utc(action['window_start_inclusive_utc'])-timedelta(days=1)
    end=utc(action['window_end_exclusive_utc'])+timedelta(days=1)
    documents=[];page_rows=[];seen_ids=set();complete=False;reason='page_limit';expected_total=None;expected_pages=None
    for page in range(1,fetcher.limits['max_wp_pages_per_window']+1):
        params={'after':start.isoformat().replace('+00:00','Z'),'before':end.isoformat().replace('+00:00','Z'),
                'orderby':'date','order':'asc','per_page':fetcher.limits['wp_page_size'],'page':page}
        url=panel['wp_api']+'wp/v2/posts?'+urllib.parse.urlencode(params)
        response=fetcher.get(url);posts=json_body(response)
        headers={k.lower():v for k,v in response.get('headers',{}).items()}
        page_rows.append({'url':url,'status':response['status'],'headers':headers})
        if not isinstance(posts,list):reason='archive_request_failed_or_nonlist';break
        try:total,pages=int(headers['x-wp-total']),int(headers['x-wp-totalpages'])
        except (KeyError,ValueError,TypeError):reason='pagination_metadata_missing';break
        if expected_total is None:expected_total,expected_pages=total,pages
        if (total,pages)!=(expected_total,expected_pages) or total<0 or pages<0:reason='pagination_counts_changed';break
        size=fetcher.limits['wp_page_size']
        if pages!=(total+size-1)//size or len(posts)!=max(0,min(size,total-(page-1)*size)):
            reason='pagination_item_count_mismatch';break
        invalid=False
        for post in posts:
            if not isinstance(post,dict) or post.get('id') in seen_ids or post.get('id') is None:
                invalid=True;continue
            seen_ids.add(post['id'])
            date=utc(post.get('date_gmt'),naive_is_gmt=True)
            content=post.get('content') or {};title=post.get('title') or {};link=post.get('link','')
            if (date is None or post.get('status')!='publish' or not isinstance(title,dict)
                    or not isinstance(content,dict) or content.get('protected') is True
                    or not isinstance(content.get('rendered'),str) or not allowed(link,panel)):
                invalid=True;continue
            documents.append({'url':link,'published_at_utc':date.isoformat().replace('+00:00','Z'),
                              'text':body_text(str(title.get('rendered',''))+' '+content['rendered']),
                              'source_capture':response['attempts'][-1]['capture_path']})
        if invalid:reason='duplicate_or_unreadable_or_undated_archive_item';break
        if page>=pages:
            complete=len(seen_ids)==total
            reason='complete_current_public_posts_archive' if complete else 'pagination_item_count_mismatch'
            break
    return {'archive_status':reason,'archive_enumeration_complete':complete,'pagination':page_rows,
            'retrieved_article_count':len(documents),'target_results':evaluate_documents(action,documents,complete,reason)}


def article_document(row):
    soup=BeautifulSoup(row['body'],'html.parser');dates=[]
    for tag in soup.find_all('meta'):
        if (tag.get('property') or tag.get('name')) in {'article:published_time','datePublished'}:
            dates.append(tag.get('content'))
    def walk(value):
        if isinstance(value,dict):
            types=value.get('@type',[]);types=[types] if isinstance(types,str) else types
            if any(t in {'Article','BlogPosting','NewsArticle'} for t in types):dates.append(value.get('datePublished'))
            for v in value.values():walk(v)
        elif isinstance(value,list):
            for v in value:walk(v)
    for script in soup.find_all('script',type='application/ld+json'):
        try:walk(json.loads(script.string or script.get_text()))
        except (ValueError,TypeError):pass
    valid={utc(d).isoformat().replace('+00:00','Z') for d in dates if utc(d)}
    return {'url':row['url'],'published_at_utc':next(iter(valid)) if len(valid)==1 else None,
            'text':body_text(row['body']),'source_capture':row['attempts'][-1]['capture_path']}


def sitemap_fallback(fetcher,panel,actions):
    all_queries={q['normalized_query']:q for a in actions for t in a['targets'] for q in t['lexical_queries']}
    urls=set();matched_links=set();index_records=[];queue=[];seen=set();sitemap_records=[]
    for url in panel['indices']:
        row=fetcher.get(url);index_records.append({'url':url,'status':row['status']})
        if row['status']=='retrieved':
            soup=BeautifulSoup(row['body'],'html.parser')
            for tag in soup.find_all('a',href=True):
                link=urllib.parse.urljoin(url,tag['href'])
                if allowed(link,panel) and any(urllib.parse.urlsplit(link).path.startswith(p) for p in panel['article_paths']):
                    urls.add(link)
                    if exact_matches(link+' '+tag.get_text(' ',strip=True),list(all_queries.values())):matched_links.add(link)
    robots=fetcher.get(panel['robots'])
    if robots['status']=='retrieved':
        queue=sorted(set(re.findall(r'(?im)^sitemap:\s*(https://\S+)',robots['body'].decode('utf-8','replace'))),key=sitemap_priority)
    while queue and len(seen)<fetcher.limits['max_sitemap_documents']:
        url=queue.pop(0)
        if url in seen:continue
        seen.add(url);row=fetcher.get(url);item={'url':url,'status':row['status']};sitemap_records.append(item)
        if row['status']!='retrieved':continue
        try:
            raw=row['body']
            if raw[:2]==b'\x1f\x8b':raw=gzip.GzipFile(fileobj=io.BytesIO(raw)).read(fetcher.limits['max_response_bytes']+1)
            if len(raw)>fetcher.limits['max_response_bytes']:raise ValueError('Expanded sitemap exceeds limit')
            tree=ET.fromstring(raw)
            locations=[e.text.strip() for e in tree.iter() if e.tag.rsplit('}',1)[-1]=='loc' and e.text]
            kind=tree.tag.rsplit('}',1)[-1];item.update(kind=kind,locations=len(locations))
            if kind=='sitemapindex':queue=sorted(set(queue)|{u for u in locations if allowed(u,panel) and u not in seen},key=sitemap_priority)
            elif kind=='urlset':urls.update(u for u in locations if allowed(u,panel) and any(urllib.parse.urlsplit(u).path.startswith(p) for p in panel['article_paths']))
            else:item['parse_error']='Unrecognized sitemap root'
        except (ET.ParseError,ValueError,OSError) as exc:item['parse_error']=str(exc)
    matched_links.update(u for u in urls if exact_matches(u,list(all_queries.values())))
    candidates=sorted(matched_links);documents=[];article_requests=[]
    for url in candidates[:fetcher.limits['max_article_documents']]:
        row=fetcher.get(url);article_requests.append({'url':url,'status':row['status']})
        if row['status']=='retrieved':documents.append(article_document(row))
    reason='partial_official_index_and_lexical_url_screen' if urls or documents else 'official_archive_unavailable'
    # Even exhaustive sitemap traversal cannot prove body-only mentions absent.
    return {'archive_status':reason,'archive_enumeration_complete':False,'index_requests':index_records,
            'robots_request':{'url':panel['robots'],'status':robots['status']},'sitemap_requests':sitemap_records,
            'sitemap_queue_remaining':len(queue),'enumerated_article_urls':len(urls),'lexically_selected_urls':len(candidates),
            'article_requests':article_requests,'retrieved_article_count':len(documents),
            'actions':[{'action_url':a['action_url'],'target_results':evaluate_documents(a,documents,False,reason)} for a in actions]}


def sitemap_priority(url):
    scope=any(term in url.casefold() for term in ('blog','support','announcement'))
    index=url.casefold().endswith('_index.xml')
    english=bool(re.search(r'_en(?:_|\.xml)',url,re.I))
    return (0 if scope and index else 1 if scope and english else 2 if scope else 3,url)


def collect_operator(name,panel,actions,limits,out,request=transport):
    fetcher=Fetcher(out/'captures'/name,panel,limits,request)
    result={'operator':name,'actions':[],'human_reference_complete':False,'private_account_action_measured':False}
    api_available=False
    if panel.get('wp_api'):
        index=fetcher.get(panel['wp_api']);data=json_body(index)
        routes=data.get('routes',{}) if isinstance(data,dict) else {}
        route=routes.get('/wp/v2/posts') or {}
        args={key for endpoint in route.get('endpoints',[]) if isinstance(endpoint,dict) for key in endpoint.get('args',{})}
        api_available=all(k in args for k in ('after','before','page','per_page','orderby','order'))
        result['api_discovery']={'url':panel['wp_api'],'status':index['status'],'documented_date_and_pagination_route_found':api_available}
    if api_available:
        for action in actions:
            result['actions'].append({'action_url':action['action_url'],**wordpress_window(fetcher,panel,action)})
    else:
        fallback=sitemap_fallback(fetcher,panel,actions);result.update(fallback)
    result['query_ledger']=fetcher.ledger()
    write_json(out/f'{name}_results.json',result)
    return result


def run(protocol,out,request=transport):
    if out.exists():raise ValueError('Refusing to overwrite disclosure collection run')
    freeze_index=json.loads((protocol/'freeze_hashes.json').read_text())
    for name,expected in freeze_index['files'].items():
        if Path(name).name!=name or sha((protocol/name).read_bytes())!=expected:raise ValueError('Frozen protocol hash mismatch')
    manifest=json.loads((protocol/'manifest.json').read_text())
    if manifest['collector_sha256']!=sha(Path(__file__).read_bytes()):raise ValueError('Collector differs from frozen source; create a new protocol version')
    out.mkdir(parents=True)
    write_json(out/'execution_manifest.json',{'created_before_requests_at_utc':now(),'protocol_manifest_sha256':sha((protocol/'manifest.json').read_bytes()),'freeze_hashes_sha256':sha((protocol/'freeze_hashes.json').read_bytes()),'status':'machine_collection_not_human_adjudication'})
    with ThreadPoolExecutor(max_workers=manifest['limits']['operator_workers']) as pool:
        results=list(pool.map(lambda item:collect_operator(item[0],item[1],manifest['actions'],manifest['limits'],out,request),manifest['operators'].items()))
    rows=[]
    for operator in results:
        for action in operator['actions']:
            for target in action['target_results']:rows.append({'operator':operator['operator'],'action_url':action['action_url'],**target})
    counts=defaultdict(int)
    for row in rows:counts[row['outcome']]+=1
    summary={'finished_at_utc':now(),'operator_action_windows':manifest['operator_action_windows'],'candidate_target_operator_units':len(rows),'outcome_counts':dict(counts),'human_reference_complete':False,'private_account_action_measured':False,'historical_archive_survival_complete':False,'interpretation':'Lexical target-naming public disclosure under frozen aliases and publication windows. API archive negatives, if any, concern the currently enumerable official archive only; deletions, lexical false negatives and identity ambiguity remain.'}
    write_json(out/'target_results.json',rows);write_json(out/'summary.json',summary)
    return summary


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    sub=parser.add_subparsers(dest='command',required=True)
    freeze_parser=sub.add_parser('freeze');freeze_parser.add_argument('--candidate-dir',type=Path,default=ROOT/'analysis/issuer_candidate_manifest');freeze_parser.add_argument('--out-dir',type=Path,required=True)
    freeze_parser.add_argument('--operators',nargs='+',choices=list(PANELS),default=list(PANELS))
    run_parser=sub.add_parser('run');run_parser.add_argument('--protocol',type=Path,required=True);run_parser.add_argument('--out-dir',type=Path,required=True)
    args=parser.parse_args()
    result=freeze(args.candidate_dir,args.out_dir,args.operators) if args.command=='freeze' else run(args.protocol,args.out_dir)
    print(json.dumps({k:v for k,v in result.items() if k not in {'actions','operators'}},indent=2))


if __name__=='__main__':main()
