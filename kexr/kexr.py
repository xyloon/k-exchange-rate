import requests


def get_request_url(key, search_date):
    return "https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?" \
           "authkey=%s&searchdate=%s&data=AP01" % (key, search_date)


def request_exchange(key, search_date):
    resp = requests.get(get_request_url(key, search_date))

    if resp.status_code != 200:
        raise Exception("Error repsonse " + str(resp))
    else:
        return resp.json()


