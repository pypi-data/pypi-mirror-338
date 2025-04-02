# Copyright 2025 Webullpay
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# 	http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from webullpaysdkmdata.quotes.instrument import Instrument
from webullpaysdkmdata.quotes.market_data import MarketData
from webullpaysdktrade.trade.account_info import Account
from webullpaysdktrade.trade.order_operation import OrderOperation
from webullpaysdktrade.trade.trade_instrument import TradeInstrument


class API:
    def __init__(self, api_client):
        self.instrument = Instrument(api_client)
        self.market_data = MarketData(api_client)
        self.account = Account(api_client)
        self.order = OrderOperation(api_client)
        self.trade_instrument = TradeInstrument(api_client)
