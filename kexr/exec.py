import argparse
from pprint import pprint

from kexr.lib import request_exchange, resp_dict_converter
from kexr.utils import db_session_open, date_creater_from_string, EnvStore, db_session_tables, date_iterator, \
    db_session_string_definition, DBType, parameter_check_with_condition
from model.exchange_rate_item import exchange_rate_item_table_name, get_exchange_rate_item_db


def define_parser():
    parser = argparse.ArgumentParser(description='collect start date end date')
    parser.add_argument('--key', nargs='?', type=str, help='API key')
    parser.add_argument('--start-date', nargs='?', type=date_creater_from_string,
                        help='starting date. format : 2000-01-01')
    parser.add_argument('--end-date', nargs='?', type=date_creater_from_string,
                        help='starting date. format : 2000-01-01')
    # for memory DB
    parser.add_argument('--dbfile', nargs='?', type=str, help='DB file')
    return parser


def is_not_none(target):
    return target is not None


def main():
    parser = define_parser()
    args = parser.parse_args()
    parameter_check_with_condition(
        parser,
        ("key", args.key, is_not_none),
        ("start_date", args.start_date, is_not_none),
        ("end_date", args.end_date, is_not_none)
    )

    dbtype, dbfilename = (DBType.sqlite3, args.dbfile) if args.dbfile is not None else \
        (DBType.memory, None)

    db_session_open(
        db_session_string=db_session_string_definition(dbtype,file_path=dbfilename),
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
    if dbtype == DBType.memory:
        pprint(session.query(ExchangeRateItem).all())


if __name__ == "__main__":
    main()
