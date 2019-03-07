import argparse
from pprint import pprint

from kexr.lib import request_exchange, resp_dict_converter
from kexr.utils import db_session_open, date_creater_from_string, EnvStore, db_session_tables, date_iterator, \
    db_session_string_definition, DBType
from model.exchange_rate_item import exchange_rate_item_table_name, get_exchange_rate_item_db


def define_parser():
    parser = argparse.ArgumentParser(description='collect start date end date')
    parser.add_argument('--key', nargs='?', type=str, help='API key')
    parser.add_argument('--start-date', nargs='?', type=date_creater_from_string,
                        help='starting date. format : 2000-01-01')
    parser.add_argument('--end-date', nargs='?', type=date_creater_from_string,
                        help='starting date. format : 2000-01-01')
    return parser


def main():
    parser = define_parser()
    args = parser.parse_args()
    # todo 모든 argument가 없으면 error임.

    # 시작 날짜부터 끝 날짜까리 나열한다.
    # DB에 해당자료가 들어가 있는지 확인하고 있으면 skip 한다.
    db_session_open(
        db_session_string=db_session_string_definition(DBType.memory),  #todo have to change sqlite3
        db_definition_method_table={
            exchange_rate_item_table_name: get_exchange_rate_item_db
        }
    )
    session, table_definition = EnvStore.get_env(db_session_tables)
    ExchangeRateItem = table_definition[exchange_rate_item_table_name]
    for one_date in date_iterator(args.start_date, args.end_date):
        for item_to_save in resp_dict_converter(
                request_exchange(key=args.key,search_date=one_date.strftime("%Y%m%d"))):
            session.add(ExchangeRateItem(**item_to_save, date=one_date))
    session.commit()
    pprint(session.query(ExchangeRateItem).all())



if __name__ == "__main__":
    main()
