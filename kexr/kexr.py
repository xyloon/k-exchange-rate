import re
from decimal import Decimal

import requests

float_pattern = re.compile(r"([^0-9., ]+)")


def remove_comma_in_float_string(i_str):
    'converting number string to Decimal'
    return None if tuple(float_pattern.findall(i_str)) else Decimal(i_str.replace(",", "").strip())


def get_request_url(key, search_date):
    return "https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?" \
           "authkey=%s&searchdate=%s&data=AP01" % (key, search_date)


def request_exchange(key, search_date):
    resp = requests.get(get_request_url(key, search_date))

    if resp.status_code != 200:
        raise Exception("Error repsonse " + str(resp))
    else:
        return resp.json()


def resp_dict_converter(i_dict_list):
    'converting number string to Decimal in dict'

    'sample input'
    # {'bkpr': '290',
    #       'cur_nm': '아랍에미리트 디르함',
    #       'cur_unit': 'AED',
    #       'deal_bas_r': '290.95',
    #       'kftc_bkpr': '290',
    #       'kftc_deal_bas_r': '290.95',
    #       'result': 1,
    #       'ten_dd_efee_r': '0',
    #       'ttb': '288.04',
    #       'tts': '293.85',
    #       'yy_efee_r': '0'},
    key_to_process = ['bkpr', 'deal_bas_r', 'kftc_deal_bas_r', 'ten_dd_efee_r', 'ttb', 'tts', 'yy_efee_r']
    return [dict(one_line if one_line[0] not in key_to_process else (one_line[0], remove_comma_in_float_string(one_line[1]) ) for one_line in one_item.items()) for one_item in i_dict_list]



# todo collect data for one year
# date, currency, ratio is format
