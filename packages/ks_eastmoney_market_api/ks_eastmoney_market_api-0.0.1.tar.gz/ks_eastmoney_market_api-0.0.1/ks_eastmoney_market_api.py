from pandas import DataFrame
from ks_trade_api.base_market_api import BaseMarketApi
from ks_trade_api.utility import extract_vt_symbol, generate_vt_symbol, CN_SYMBOL_START2EXCHANGE
from ks_trade_api.constant import (
    CHINA_TZ, US_EASTERN_TZ,
    Exchange as KsExchange, Product as KsProduct, SubscribeType as KsSubscribeType,
    RetCode as KsRetCode, RET_OK as KS_RET_OK, RET_ERROR as KS_RET_ERROR, ErrorCode as KsErrorCode,
    Interval as KsInterval, Adjustment as KsAdjustment
)
from ks_trade_api.object import (
    ErrorData, ContractData, MyTickData, MyBookData, MyRawTickData, QuoteData, BarData
)
from ks_utility import datetimes
from decimal import Decimal
from dateutil.parser import parse
from ks_trade_api.base_market_api import BaseMarketApi
from typing import Optional, Union, List
from logging import DEBUG, INFO, WARNING, ERROR

import akshare as ak

class KsEastmoneyMarketApi(BaseMarketApi):
    gateway_name: str = 'KS_EASTMONEY'

    def __init__(self, setting: dict = {}):
        gateway_name = setting.get('gateway_name', self.gateway_name)
        dd_secret = setting.get('dd_secret')
        dd_token = setting.get('dd_token')
        super().__init__(gateway_name=gateway_name, dd_secret=dd_secret, dd_token=dd_token)

        self.init_handlers()

    # 初始化行回调和订单回调
    def init_handlers(self):
       pass

    # 获取静态信息 # todo! ks_trader_wrapper中使用到df=False要修正那边
    def query_contracts(
            self,
            vt_symbols: Optional[List[str]] = None,
            exchanges: Optional[list[KsExchange]] = None,
            products: Optional[List[KsProduct]] = None,
            df: bool = True
        ) -> tuple[KsRetCode, Union[list[ContractData], DataFrame]]:
        
        stock_df = ak.stock_zh_a_spot_em()
        stock_df['exchange'] = stock_df['代码'].str[:2].map(lambda x: CN_SYMBOL_START2EXCHANGE[x].value)
        stock_df['vt_symbol'] = stock_df['代码'] + '.' + stock_df['exchange']
        stock_df['name'] = stock_df['名称']
        stock_df['product'] = KsProduct.EQUITY.value
        stock_df['size'] = '1'
        stock_df['sub_exchange'] = ''
        stock_df['gateway'] = self.gateway_name
        stock_df['min_volume'] = '100'
        return KS_RET_OK, stock_df[['vt_symbol', 'name', 'product', 'size', 'min_volume', 'sub_exchange', 'gateway']]

    # 关闭上下文连接
    def close(self):
        pass


        