import requests_mock

from kexr.lib import get_request_url, request_exchange
from test.const import resp_json_exch


def test_get_request_url():
    assert ("https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey=11&searchdate=20180103&data=AP01"
            == get_request_url(key="11", search_date="20180103"))


def test_request_exchange():
    req_url = get_request_url(key="11", search_date="20180103")
    with requests_mock.mock() as m:
        m.get(req_url, text=resp_json_exch, status_code=200)
        r = request_exchange("11", "20180103")
    assert '1,326' == [i['kftc_bkpr'] for i in r if i['cur_unit'] == "EUR"][0]
