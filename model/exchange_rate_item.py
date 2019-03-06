from sqlalchemy import Column, String, Date, Float

exchange_rate_item_table_name = 'exchange_rate_item'


def get_exchange_rate_item_db(base, table_name=exchange_rate_item_table_name):
    class ExchangeRateItem(base):
        __tablename__ = table_name
        date = Column(Date, primary_key=True)
        bkrp = Column(Float, nullable=False)
        cur_nm = Column(String, nullable=False)
        cur_unit = Column(String, primary_key=True)
        deal_bas_r = Column(Float, nullable=False)
        kftc_bkpr = Column(Float, nullable=False)
        kftc_deal_bas_r = Column(Float, nullable=False)
        result = Column(Float, nullable=False)
        ten_dd_efee_r = Column(Float, nullable=False)
        ttb = Column(Float, nullable=False)
        tts = Column(Float, nullable=False)
        yy_efee_r = Column(Float, nullable=False)

        def __init__(self, date, bkrp, cur_nm, cur_unit, deal_bas_r, kftc_bkpr, kftc_deal_bas_r, result, ten_dd_efee_r,
                     ttb, tts, yy_efee_r):
            self.date = date
            self.bkrp = bkrp
            self.cur_nm = cur_nm
            self.cur_unit = cur_unit
            self.deal_bas_r = deal_bas_r
            self.kftc_bkpr = kftc_bkpr
            self.kftc_deal_bas_r = kftc_deal_bas_r
            self.result = result
            self.ten_dd_efee_r = ten_dd_efee_r
            self.ttb = ttb
            self.tts = tts
            self.yy_efee_r = yy_efee_r

        def __repr__(self):
            return "<ExchangeRateItem date:{self.date}, bkrp:{self.bkrp}, cur_nm:{self.cur_nm}, " \
                   "cur_unit:{self.cur_unit}, deal_bas_r:{self.deal_bas_r}, kftc_bkpr:{self.kftc_bkpr}, " \
                   "kftc_deal_bas_r:{self.kftc_deal_bas_r}, result:{self.result}, ten_dd_efee_r:{self.ten_dd_efee_r}," \
                   " ttb:{self.ttb}, tts:{self.tts}, yy_efee_r:{self.yy_efee_r}>".format(self=self)
    return ExchangeRateItem
