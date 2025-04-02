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
import uuid
from webullpaysdktrade.common.order_side import OrderSide
from webullpaysdktrade.common.order_tif import OrderTIF
from webullpaysdktrade.common.order_type import OrderType
from webullpaysdktrade.request.cancel_order_request import CancelOrderRequest
from webullpaysdktrade.request.get_open_orders_request import OpenOrdersListRequest
from webullpaysdktrade.request.get_order_detail_request import OrderDetailRequest
from webullpaysdktrade.request.get_today_orders_request import TodayOrdersListRequest
from webullpaysdktrade.request.palce_order_request import PlaceOrderRequest


class OrderOperation:
    def __init__(self, api_client):
        self.client = api_client

    def place_order(self, account_id, request_id, instrument_id,
                    order_type, tif, side, entrust_type, qty=None, amt=None,
                    limit_price=None, stop_price=None):
        """
        This interface supports placing crypto orders
        :param account_id: Account ID.
        :param request_id: ID of each request, must be unique.
        :param instrument_id: The caller obtains the symbol ID by calling get_tradable_instruments.
        :param order_type: Order Type.
        :param tif: Order validity period.
        :param side: BUY and SELL direction.
        :param entrust_type: Order by QTY(quantity) or CASH(amount).
        :param qty: Order quantity.
        :param amt: Order amount.
        :param limit_price: When Order_type is LMT(limit order), STP_LMT(stop-loss limit order), needs to be passed.
        :param stop_price: When order_type is STP_LMT(stop-loss limit order), needs to be passed,
        it needs to pass.
        """
        place_order_request = PlaceOrderRequest()
        place_order_request.set_account_id(account_id)
        place_order_request.set_crypto_order(request_id=request_id, instrument_id=instrument_id,
                                             side=side, tif=tif, order_type=order_type, entrust_type=entrust_type,
                                             amt=amt, qty=qty, limit_price=limit_price, stop_price=stop_price)
        response = self.client.get_response(place_order_request)
        return response

    def cancel_order(self, account_id, client_order_id):
        """
        Cancel order.

        :param account_id: Account ID
        :param client_order_id: Third-party order ID from 'place_order' response.
        """
        cancel_order_request = CancelOrderRequest()
        cancel_order_request.set_account_id(account_id)
        cancel_order_request.set_client_order_id(client_order_id)
        response = self.client.get_response(cancel_order_request)
        return response

    def list_today_orders(self, account_id, page_size=10, last_client_order_id=None):
        """
        Paging query all orders of the day, the number of data returned each time can be specified,
        the maximum value is 100.

        :param account_id: Account ID
        :param page_size: For the number of entries per page, the default value is 10,
        and the maximum value is 100. Integers can be filled.

        :param last_client_order_id: The 3rd party order ID is not passed,
         and the default check is conducted on the first page.
        """
        today_orders_list_request = TodayOrdersListRequest()
        today_orders_list_request.set_account_id(account_id)
        today_orders_list_request.set_page_size(page_size)
        if last_client_order_id is not None:
            today_orders_list_request.set_last_client_order_id(last_client_order_id)
        response = self.client.get_response(today_orders_list_request)
        return response

    def list_open_orders(self, account_id, page_size=10, last_client_order_id=None):
        """
        Paging query pending orders.

        :param account_id: Account ID
        :param page_size: For the number of entries per page, the default value is 10, and the maximum value is 100.
         Integers can be filled.
        :param last_client_order_id: The 3rd party order ID is not passed,
        and the default check is conducted on the first page.
        """
        open_orders_list_request = OpenOrdersListRequest()
        open_orders_list_request.set_account_id(account_id)
        open_orders_list_request.set_page_size(page_size)
        if last_client_order_id is not None:
            open_orders_list_request.set_last_client_order_id(last_client_order_id)
        response = self.client.get_response(open_orders_list_request)
        return response

    def query_order_detail(self, account_id, client_order_id):
        """
        Paging query pending orders.

        :param account_id: Account ID
        :param client_order_id: The 3rd party order ID.
        """
        order_detail_request = OrderDetailRequest()
        order_detail_request.set_account_id(account_id)
        order_detail_request.set_client_order_id(client_order_id)
        response = self.client.get_response(order_detail_request)
        return response
