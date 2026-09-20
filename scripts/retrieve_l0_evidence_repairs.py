#!/usr/bin/env python3
"""Bounded, read-only OONI/source retrieval for machine-proposed L0 repairs.

Never edits events or asserts a human review. Each response is stored unchanged
by content hash, including HTTP error bodies; failed requests are not zero probes.
"""
from __future__ import annotations
import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import urllib.error
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
API = 'https://api.ooni.io/api/v1/measurements'


def now():
    return datetime.now(timezone.utc).isoformat()


def capture(url, directory, timeout=25):
    record = {'requested_url': url, 'started_at_utc': now(), 'http_status': None,
              'body_path': None, 'body_hash': None, 'error': None}
    raw = b''
    try:
        request = urllib.request.Request(url, headers={'User-Agent': 'censorship-event-research/1.0 (public historical data retrieval)'})
        with urllib.request.urlopen(request, timeout=timeout) as response:
            raw = response.read()
            record.update(http_status=response.status, final_url=response.url,
                          content_type=response.headers.get('Content-Type', ''))
    except urllib.error.HTTPError as error:
        raw = error.read()
        record.update(http_status=error.code, final_url=error.url,
                      content_type=error.headers.get('Content-Type', ''), error=f'HTTP {error.code}')
    except (OSError, TimeoutError, urllib.error.URLError) as error:
        record['error'] = f'{type(error).__name__}: {error}'
    if raw:
        digest = hashlib.sha256(raw).hexdigest()
        directory.mkdir(parents=True, exist_ok=True)
        path = directory / f'{digest}.body'
        if path.exists() and path.read_bytes() != raw:
            raise ValueError('content-addressed artifact collision')
        path.write_bytes(raw)
        try:
            record['body_path'] = str(path.relative_to(ROOT))
        except ValueError:
            record['body_path'] = str(path)
        record['body_hash'] = 'sha256:' + digest
        record['bytes'] = len(raw)
    record['finished_at_utc'] = now()
    return record, raw


def default_queries(query_mode='domain', limit=500):
    if query_mode not in {'domain', 'exact_https'}:
        raise ValueError('query_mode must be domain or exact_https')
    queries = []
    for event_id, cc, domains, since, until in (
        ('ethiopia-nbe-exchange-website-block-2025-11', 'ET',
         ('binance.com', 'okx.com', 'bybit.com'), '2025-09-15', '2025-12-07'),
        ('thailand-sec-unlicensed-exchange-block-2025-06', 'TH',
         ('bybit.com', '1000x.live', 'coinex.com', 'okx.com', 'xt.com'), '2025-05-15', '2025-07-29'),
    ):
        for domain in domains:
            for host in (domain, 'www.' + domain):
                target = {'domain': host} if query_mode == 'domain' else {'input': f'https://{host}/'}
                queries.append({'event_id': event_id, **target, 'probe_cc': cc,
                                'since': since, 'until': until, 'test_name': 'web_connectivity',
                                'limit': limit})
    return queries


def summarize_measurements(results):
    unique = {}
    for index, row in enumerate(results):
        key = row.get('measurement_uid') or (row.get('report_id'), row.get('input'), row.get('measurement_start_time'))
        if (isinstance(key, tuple) and not any(key)) or not key:
            key = ('row_without_identity', index)
        unique.setdefault(key, row)
    rows = list(unique.values())
    return {
        'retrieved_rows': len(results), 'unique_measurements': len(rows),
        'measurement_ids': [r['measurement_uid'] for r in rows if r.get('measurement_uid')],
        'probe_countries': sorted({r['probe_cc'] for r in rows if r.get('probe_cc')}),
        'probe_asns': sorted({str(r['probe_asn']) for r in rows if r.get('probe_asn')}),
        'distinct_probes': None,
        'probe_count_limit': 'Public index identifies probe country/ASN, not distinct independent devices; ASN count is not probe count.',
        'flags': {flag: {'true': sum(r.get(flag) is True for r in rows),
                         'false': sum(r.get(flag) is False for r in rows),
                         'missing_or_other': sum(r.get(flag) is not True and r.get(flag) is not False for r in rows)}
                  for flag in ('anomaly', 'confirmed', 'failure')},
        'first_measurement': min((r.get('measurement_start_time') for r in rows if r.get('measurement_start_time')), default=None),
        'last_measurement': max((r.get('measurement_start_time') for r in rows if r.get('measurement_start_time')), default=None),
        'measurement_inputs': sorted({r['input'] for r in rows if r.get('input')}),
    }


def retrieve_query(query, directory, max_pages=2, fetch=capture):
    params = {k: v for k, v in query.items() if k != 'event_id'}
    url = API + '?' + urllib.parse.urlencode(params)
    pages, results = [], []
    complete, reason = False, 'page_limit'
    for _ in range(max_pages):
        record, raw = fetch(url, directory)
        pages.append(record)
        if record.get('error') or record.get('http_status') != 200:
            reason = 'request_failed'
            break
        try:
            data = json.loads(raw)
            if (not isinstance(data, dict) or not isinstance(data.get('results'), list)
                    or any(not isinstance(row, dict) for row in data['results'])):
                raise ValueError('not an OONI result page')
            if not isinstance(data.get('metadata') or {}, dict):
                raise ValueError('invalid OONI pagination metadata')
        except (ValueError, TypeError) as error:
            record['parse_error'] = str(error)
            reason = 'invalid_response'
            break
        results.extend(data['results'])
        metadata = data.get('metadata') or {}
        record['api_metadata'] = metadata
        next_url = metadata.get('next_url') or data.get('next_url')
        if not next_url:
            count = metadata.get('count')
            if isinstance(count, int) and count > len(results):
                reason = 'inconsistent_pagination_count'
                break
            complete, reason = True, 'pagination_complete'
            break
        url = urllib.parse.urljoin(API, next_url)
        if urllib.parse.urlsplit(url).hostname != 'api.ooni.io':
            reason = 'unexpected_pagination_host'
            break
    metrics = summarize_measurements(results)
    return {'query': query, 'request_pages': pages, 'pagination_complete': complete,
            'retrieval_status': reason, 'metrics': metrics,
            'historical_measurement_denominator': metrics['unique_measurements'] if complete else None,
            'denominator_status': ('retrieved_measurements_require_measurement_review' if results else
                                   'no_measurements_returned_for_query' if complete else 'retrieval_unresolved'),
            'censorship_rate': None, 'human_review_status': 'not_reviewed', 'results': results}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out-dir', type=Path, default=ROOT/'sources/evidence_repairs/l0_followup')
    parser.add_argument('--max-pages', type=int, default=2)
    parser.add_argument('--workers', type=int, default=4)
    parser.add_argument('--timeout', type=float, default=25)
    parser.add_argument('--limit', type=int, default=500)
    parser.add_argument('--query-mode', choices=('domain', 'exact_https'), default='domain')
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--sources-only', action='store_true')
    mode.add_argument('--queries-only', action='store_true')
    args = parser.parse_args(argv)
    if args.max_pages < 1 or args.workers < 1 or not (0 < args.timeout <= 60) or not (1 <= args.limit <= 500):
        parser.error('positive page/worker limits, timeout <=60 seconds, and limit 1..500 required')
    args.out_dir.mkdir(parents=True, exist_ok=True)
    run_id = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    sources = [
        'https://www.sec.or.th/EN/Pages/News_Detail.aspx?SECID=12047',
        'https://www.sec.or.th/EN/Pages/News_Detail.aspx?SECID=12048',
        'https://www.sec.or.th/TH/Pages/News_Detail.aspx?SECID=11796',
        'https://addisinsight.net/2025/11/06/binance-confirms-talks-with-ethiopian-regulators-as-website-access-gets-restricted/',
        'https://api.ooni.io/apidocs.json',
    ]
    fetch = lambda url, directory: capture(url, directory, timeout=args.timeout)
    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        source_results = [] if args.queries_only else list(executor.map(lambda url: fetch(url, args.out_dir/'responses')[0], sources))
        queries = [] if args.sources_only else default_queries(args.query_mode, args.limit)
        query_results = list(executor.map(lambda query: retrieve_query(query, args.out_dir/'responses', args.max_pages, fetch=fetch), queries))
    manifest = {'run_id': run_id, 'execution_type': 'automated_public_read_only_retrieval',
                'finished_at_utc': now(), 'human_review_status': 'not_reviewed',
                'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                'source_captures': source_results, 'queries': query_results,
                'query_mode': args.query_mode,
                'limits': {'queries': len(queries), 'max_pages_each': args.max_pages, 'page_limit': args.limit,
                           'workers': args.workers, 'timeout_seconds': args.timeout},
                'interpretation': 'No query failure or empty result is evidence of no censorship. Anomaly flags require raw-measurement/control review.'}
    path = args.out_dir/f'retrieval_{run_id}.json'
    if path.exists():
        raise FileExistsError(path)
    path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + '\n')
    print(path)
    for query in query_results:
        q=query['query']; m=query['metrics']
        print(q['probe_cc'], q.get('domain') or q.get('input'), query['retrieval_status'],
              query['historical_measurement_denominator'], m['probe_asns'], m['flags'])
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
