# todo 1. 对于查询的持仓，空的也要推送空的，否则orderplit无法回调.  这对于http请求很容易实现，但是如果是websocket回调，也许空的不会回调？例如ibk

import pandas as pd
from datetime import datetime, timedelta
from ks_trade_api.base_fundamental_api import BaseFundamentalApi
from ks_trade_api.utility import extract_vt_symbol, generate_vt_symbol
from ks_trade_api.constant import Exchange
import sys
from decimal import Decimal
import uuid
from logging import DEBUG, WARNING, ERROR
from ks_utility.numbers import to_decimal
from enum import Enum

from .EmQuantAPI import c

class MyExchange(Enum):
    SH = 'SH'
    SZ = 'SZ'
    HK = 'HK'
    O = 'O'

EXCHANGE_KS2MY = {
    Exchange.SSE: MyExchange.SH,
    Exchange.SZSE: MyExchange.SZ,
    Exchange.SEHK: MyExchange.HK,
    Exchange.SMART: MyExchange.O
}
EXCHANGE_MY2KS = {v:k for k,v in EXCHANGE_KS2MY.items()}

PERCENT_COLUMNS = ['ROEWA', 'ROEAVG', 'DIVIDENDTTM', 'HKSDIVIDENDTTM']

def extract_my_symbol(my_symbol):
    items = my_symbol.split(".")
    return '.'.join(items[:-1]), MyExchange(items[-1])

def symbol_ks2my(vt_symbol: str):
    if not vt_symbol:
        return ''
    symbol, ks_exchange = extract_vt_symbol(vt_symbol)
    return generate_vt_symbol(symbol, EXCHANGE_KS2MY.get(ks_exchange))

def symbol_my2ks(my_symbol: str):
    if not my_symbol:
        return ''
    symbol, my_exchange = extract_my_symbol(my_symbol)
    return generate_vt_symbol(symbol, EXCHANGE_MY2KS.get(my_exchange))

class KsEastmoneyFundamentalApi(BaseFundamentalApi):
    gateway_name: str = "KS_EASTMONEY_FUNDAMENTAL"

    def __init__(self, setting: dict):
        dd_secret = setting.get('dd_secret')
        dd_token = setting.get('dd_token')
        gateway_name = setting.get('gateway_name', self.gateway_name)
        super().__init__(gateway_name=gateway_name, dd_secret=dd_secret, dd_token=dd_token)

        username = setting.get('username')
        password = setting.get('password')
        startoptions = "ForceLogin=1" + ",UserName=" + username + ",Password=" + password;
        loginResult = c.start(startoptions, '')
        self.log(loginResult, '登录结果')

    def css(self, vt_symbols: list[str], indicators: str = '', options: str = '') -> pd.DataFrame:
        if not 'IsPandas' in options:
            options += ',IsPandas=1'
        my_symbols = [symbol_ks2my(x) for x in vt_symbols]
        df = c.css(my_symbols, indicators=indicators, options=options)
        
        df.reset_index(drop=False, inplace=True)

        # 转换symbol
        df['CODES'] = df['CODES'].transform(symbol_my2ks)
        df.rename(columns={'CODES': 'vt_symbol'}, inplace=True)

        # 转换百分比
        for column in PERCENT_COLUMNS:
            if column in df.columns:
                df[column] = df[column] / 100

        # LIBILITYTOASSET: 港美的是百分号，A股是小数
        if 'LIBILITYTOASSET' in df.columns:
            is_hk = df.vt_symbol.str[-5:].isin(['.SEHK', 'SMART'])
            df.loc[is_hk, 'LIBILITYTOASSET'] = df[is_hk]['LIBILITYTOASSET'] / 100

        return df
        

    # 关闭上下文连接
    def close(self):
        pass
        # self.quote_ctx.close()
        # self.trd_ctx.close()


        