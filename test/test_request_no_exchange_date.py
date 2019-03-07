import requests_mock

from kexr.lib import get_request_url, request_exchange
from test.const import resp_json_no_exch


def test_request_exchange():
    req_url = get_request_url(key="11", search_date="20180301")
    with requests_mock.mock() as m:
        m.get(req_url, text=resp_json_no_exch, status_code=200)
        r = request_exchange("11", "20180301")
    assert len(r) == 0
