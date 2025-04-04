# todo 1. 对于查询的持仓，空的也要推送空的，否则orderplit无法回调.  这对于http请求很容易实现，但是如果是websocket回调，也许空的不会回调？例如ibk

import pandas as pd
from pandas import DataFrame
from datetime import datetime, timedelta
from ks_trade_api.base_fundamental_api import BaseFundamentalApi
from ks_trade_api.utility import extract_vt_symbol, generate_vt_symbol
from ks_trade_api.constant import Exchange, SubExchange, RET_OK, Product
from ks_utility.datetimes import get_date_str
import sys
from decimal import Decimal
import uuid
from logging import DEBUG, WARNING, ERROR
from ks_utility.numbers import to_decimal
from enum import Enum

from .EmQuantAPI import c

class MyCurrency(Enum):
    CNY = 2
    USD = 3
    HKD = 4

class MyExchange(Enum):
    SH = 'SH'
    SZ = 'SZ'
    HK = 'HK'
    BJ = 'BJ'
    O = 'O'

EXCHANGE2MY_CURRENCY = {
    Exchange.SSE: MyCurrency.CNY,
    Exchange.SZSE: MyCurrency.CNY,
    Exchange.SEHK: MyCurrency.HKD,
    Exchange.SMART: MyCurrency.USD
}

EXCHANGE_KS2MY = {
    Exchange.SSE: MyExchange.SH,
    Exchange.SZSE: MyExchange.SZ,
    Exchange.SEHK: MyExchange.HK,
    Exchange.BSE: MyExchange.BJ
}
EXCHANGE_MY2KS = {v:k for k,v in EXCHANGE_KS2MY.items()}

class MySubExchange(Enum):
    N = 'N'
    O = 'O'
    A = 'A'

SUB_EXCHANGE_KS2MY = {
    SubExchange.US_AMEX: MySubExchange.A,
    SubExchange.US_NASDAQ: MySubExchange.O,
    SubExchange.US_NYSE: MySubExchange.N
}

PERCENT_COLUMNS = ['ROEWA', 'ROEAVG', 'ROETTM', 'DIVIDENDTTM', 'HKSDIVIDENDTTM', 'DIVIDENDYIELDY']

# 标准字段映射
INDICATORS_KS2MY = {
    'ROE.SSE': 'ROEWA',
    'ROE.SZSE': 'ROEWA',
    'ROE.SEHK': 'ROEAVG',
    'ROE.SMART': 'ROEAVG',

    'DIVIDENDTTM.SSE': 'DIVIDENDTTM',
    'DIVIDENDTTM.SZSE': 'DIVIDENDTTM',
    'DIVIDENDTTM.SEHK': 'HKSDIVIDENDTTM',
    'DIVIDENDTTM.SMART': 'HKSDIVIDENDTTM'
}

INDICATORS_MY2KS = {v:'.'.join(k.split('.')[:-1]) for k,v in INDICATORS_KS2MY.items()}

EXCHANGE_PRODUCT2PUKEYCODE = {
    'CNSE.EQUITY': '001071',
    'SEHK.EQUITY': '401001',
    'SMART.EQUITY': '202001004',

    'CNSE.ETF': '507001',
    'SEHK.ETF': '404004',
    'SMART.ETF': '202003009'
}

def extract_my_symbol(my_symbol):
    items = my_symbol.split(".")
    return '.'.join(items[:-1]), MyExchange(items[-1])

def symbol_ks2my(vt_symbol: str, sub_exchange: SubExchange = None):
    if not vt_symbol:
        return ''
    symbol, ks_exchange = extract_vt_symbol(vt_symbol)
    if not sub_exchange:
        my_symbol = generate_vt_symbol(symbol, EXCHANGE_KS2MY.get(ks_exchange))
    else:
        my_symbol = generate_vt_symbol(symbol, SUB_EXCHANGE_KS2MY.get(sub_exchange))
    return my_symbol

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

    def _normalization_indicators_input(self, indicators: str, exchange: Exchange):
        indicators_list = indicators.split(',')
        indicators_new = [INDICATORS_KS2MY.get(f'{x}.{exchange.value}', x) for x in indicators_list]
        return ','.join(indicators_new)
    
    def _normalization_indicators_output(self, df: DataFrame):
        rename_columns = {x:INDICATORS_MY2KS[x] for x in df.columns if x in INDICATORS_MY2KS}
        return df.rename(columns=rename_columns)

    # 暂时不支持跨市场多标的，使用第一个表的市场来决定所有标的的市场
    # sub_exchange是用来做美股区分，东财
    def css(self, vt_symbols: list[str], indicators: str = '', options: str = '', sub_exchanges: list[str] = []) -> pd.DataFrame:
        if not vt_symbols:
            return None
        
        symbol, exchange = extract_vt_symbol(vt_symbols[0])
        
        indicators = self._normalization_indicators_input(indicators, exchange)

        # 默认pandas返回
        if not 'IsPandas' in options:
            options += ',IsPandas=1'

        if 'ROETTM' in indicators:
            options += ',TtmType=2'

        if 'BPS' in indicators:
            options += f',CurType={EXCHANGE2MY_CURRENCY.get(exchange).value}'

        my_symbols = [symbol_ks2my(x, SubExchange(sub_exchanges[i]) if len(sub_exchanges) and sub_exchanges[i] else None) for i,x in enumerate(vt_symbols)]
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

        df = self._normalization_indicators_output(df)

        return RET_OK, df
    
    def sector(self, exchange: Exchange, products: list[Product], tradedate: str = None):
        if not tradedate:
            tradedate = get_date_str()
        # 默认pandas返回
        options = 'IsPandas=1'

        all_df = pd.DataFrame()
        for product in products:
            pukeycode = EXCHANGE_PRODUCT2PUKEYCODE.get(f'{exchange.name}.{product.name}')
            df = c.sector(pukeycode, tradedate, options)
            df['vt_symbol'] = df['SECUCODE'].transform(symbol_my2ks)
            df['name'] = df['SECURITYSHORTNAME']

            all_df = pd.concat([all_df, df], ignore_index=True)
        return RET_OK, all_df

    # 关闭上下文连接
    def close(self):
        pass
        # self.quote_ctx.close()
        # self.trd_ctx.close()


        