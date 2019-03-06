from datetime import date

from kexr.utils import db_session_open, DBType, db_session_string_definition, EnvStore, db_session_tables
from model.exchange_rate_item import exchange_rate_item_table_name, get_exchange_rate_item_db


def test_db_session_open():
    db_session_open(
        db_session_string=db_session_string_definition(DBType.memory),
        db_definition_method_table={
            exchange_rate_item_table_name: get_exchange_rate_item_db
        }
    )
    session, table_definition = EnvStore.get_env(db_session_tables)
    ExchangeRateItem = table_definition[exchange_rate_item_table_name]
    session.add(
        ExchangeRateItem(
            date=date(2018, 1, 1),
            bkrp=10.1,
            cur_nm="1111",
            cur_unit="ABCD",
            deal_bas_r=10.2,
            kftc_bkpr=10.3,
            kftc_deal_bas_r=10.4,
            result=1,
            ten_dd_efee_r=10.5,
            ttb=10.6,
            tts=10.7,
            yy_efee_r=10.8
        )
    )
    session.commit()
    assert session.query(ExchangeRateItem).first().bkrp == 10.1

