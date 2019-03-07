import json

from kexr.lib import resp_dict_converter
from test.const import resp_json_exch


def test_resp_dict_converter():
    input = json.loads(resp_json_exch)
    # one item after processed
    # [{'bkpr': Decimal('290'),
    #   'cur_nm': '아랍에미리트 디르함',
    #   'cur_unit': 'AED',
    #   'deal_bas_r': Decimal('290.95'),
    #   'kftc_bkpr': '290',
    #   'kftc_deal_bas_r': Decimal('290.95'),
    #   'result': 1,
    #   'ten_dd_efee_r': Decimal('0'),
    #   'ttb': Decimal('288.04'),
    #   'tts': Decimal('293.85'),
    #   'yy_efee_r': Decimal('0')}]
    #
    assert float(
        [one_item['tts'] for one_item in resp_dict_converter(input) if one_item['cur_unit'] == 'AED'][0]) == 293.85
