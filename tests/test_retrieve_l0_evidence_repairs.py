"""Protect evidence-gap semantics; fixtures are synthetic, never evidence."""
import json

import pytest

from retrieve_l0_evidence_repairs import default_queries, retrieve_query, summarize_measurements


def fetch_pages(*pages):
    remaining = iter(pages)

    def fetch(url, directory):
        payload = next(remaining)
        if payload is None:
            return {'http_status': None, 'error': 'TimeoutError'}, b''
        return {'http_status': 200, 'error': None}, json.dumps(payload).encode()

    return fetch


def test_timeout_is_unknown_denominator_not_a_zero(tmp_path):
    result = retrieve_query(default_queries()[0], tmp_path, fetch=fetch_pages(None))
    assert result['retrieval_status'] == 'request_failed'
    assert result['historical_measurement_denominator'] is None
    assert result['denominator_status'] == 'retrieval_unresolved'
    assert result['censorship_rate'] is None


def test_successful_empty_query_is_not_a_no_censorship_claim(tmp_path):
    result = retrieve_query(default_queries()[0], tmp_path,
                            fetch=fetch_pages({'metadata': {'count': 0}, 'results': []}))
    assert result['historical_measurement_denominator'] == 0
    assert result['denominator_status'] == 'no_measurements_returned_for_query'
    assert result['censorship_rate'] is None
    assert result['human_review_status'] == 'not_reviewed'


def test_bounded_pagination_keeps_complete_denominator_unknown(tmp_path):
    page = {'metadata': {'next_url': '?offset=1'},
            'results': [{'measurement_uid': 'synthetic-one', 'anomaly': True}]}
    result = retrieve_query(default_queries()[0], tmp_path, max_pages=1, fetch=fetch_pages(page))
    assert result['metrics']['unique_measurements'] == 1
    assert result['historical_measurement_denominator'] is None
    assert result['retrieval_status'] == 'page_limit'
    assert result['censorship_rate'] is None


@pytest.mark.parametrize('page', [
    {'results': [None]}, {'results': [], 'metadata': []}, {'error': 'service unavailable'},
])
def test_malformed_response_is_unknown(tmp_path, page):
    # Empty metadata is tolerated by the upstream API; use a nonempty wrong type.
    if page.get('metadata') == []:
        page['metadata'] = ['invalid']
    result = retrieve_query(default_queries()[0], tmp_path, fetch=fetch_pages(page))
    assert result['retrieval_status'] == 'invalid_response'
    assert result['historical_measurement_denominator'] is None


def test_count_without_next_page_cannot_claim_completion(tmp_path):
    result = retrieve_query(default_queries()[0], tmp_path,
                            fetch=fetch_pages({'metadata': {'count': 5}, 'results': []}))
    assert result['retrieval_status'] == 'inconsistent_pagination_count'
    assert result['historical_measurement_denominator'] is None


def test_aggregate_flags_do_not_invent_probe_identity():
    row = {'measurement_uid': 'synthetic-one', 'probe_cc': 'TH', 'probe_asn': 'AS1',
           'anomaly': True, 'failure': False}
    result = summarize_measurements([row, row, {'measurement_uid': 'synthetic-two',
                                                'probe_cc': 'TH', 'probe_asn': 'AS1'}])
    assert result['unique_measurements'] == 2
    assert result['probe_asns'] == ['AS1']
    assert result['distinct_probes'] is None
    assert result['flags']['anomaly'] == {'true': 1, 'false': 0, 'missing_or_other': 1}
    assert result['flags']['confirmed']['missing_or_other'] == 2


def test_queries_preserve_countries_windows_and_host_variants():
    queries = default_queries()
    assert len(queries) == 16
    assert {q['probe_cc'] for q in queries} == {'ET', 'TH'}
    assert all(q['test_name'] == 'web_connectivity' and 'input' not in q for q in queries)
    assert sum(q['probe_cc'] == 'ET' for q in queries) == 6
    assert sum(q['probe_cc'] == 'TH' for q in queries) == 10


def test_exact_url_fallback_is_explicit_about_scheme_and_input():
    queries = default_queries('exact_https', limit=100)
    assert len(queries) == 16
    assert all(q['input'].startswith('https://') and q['input'].endswith('/') for q in queries)
    assert all('domain' not in q and q['limit'] == 100 for q in queries)
