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

# coding=utf-8
import inspect

from webullpaysdkcore.request import ApiRequest

class PlaceOrderRequest(ApiRequest):
    def __init__(self):
        ApiRequest.__init__(self, "/trade/order/place", version='v1', method="POST", body_params={})
        self._crypto_order = {}
        self.add_body_params("crypto_order", self._crypto_order)

    def add_crypto_order_params(self, k, v):
        self._crypto_order[k] = v

    def set_account_id(self, account_id):
        self.add_body_params("account_id", account_id)

    def set_request_id(self, request_id):
        self.add_crypto_order_params("request_id", request_id)

    def set_side(self, side):
        self.add_crypto_order_params("side", side)

    def set_tif(self, tif):
        self.add_crypto_order_params("tif", tif)

    def set_instrument_id(self, instrument_id):
        self.add_crypto_order_params("instrument_id", instrument_id)

    def set_order_type(self, order_type):
        self.add_crypto_order_params("order_type", order_type)

    def set_limit_price(self, limit_price):
        self.add_crypto_order_params("limit_price", limit_price)

    def set_stop_price(self, stop_price):
        self.add_crypto_order_params("stop_price", stop_price)

    def set_entrust_type(self, entrust_type):
        self.add_crypto_order_params("entrust_type", entrust_type)

    def set_qty(self, quantity):
        self.add_crypto_order_params("qty", quantity)

    def set_amt(self, amount):
        self.add_crypto_order_params("amt", amount)




    def set_crypto_order(self, request_id, instrument_id, side, tif, order_type,
                         entrust_type, qty, amt, limit_price, stop_price):
        self._crypto_order.update({k: v for k, v in locals().items() if v is not None and k != 'self'})








