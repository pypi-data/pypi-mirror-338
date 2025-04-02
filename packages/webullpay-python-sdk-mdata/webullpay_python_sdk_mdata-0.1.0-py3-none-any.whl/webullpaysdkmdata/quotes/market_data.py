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

from webullpaysdkmdata.request.get_historical_bars_request import GetHistoricalBarsRequest
from webullpaysdkmdata.request.get_quotes_request import GetQuotesRequest
from webullpaysdkmdata.request.get_snapshot_request import GetSnapshotRequest



class MarketData:
    def __init__(self, api_client):
        self.client = api_client

    def get_history_bar(self, symbol, category, timespan, count='200'):
        """
        Returns to Instrument in the window aggregated data.
        According to the last N K-lines of the crypto code, it supports various granularity K-lines such as m1 and m5.
        Currently, only the K-line with the previous weight is provided for the daily K-line and above,
        and only the un-weighted K-line is provided for the minute K.

        :param symbols: Securities code
        :param category: Security type, enumeration.
        :param timespan: K-line time granularity
        :param count: The number of lines: the default is 200, and the maximum limit is 1200
        """
        history_bar_request = GetHistoricalBarsRequest()
        history_bar_request.set_symbol(symbol)
        history_bar_request.set_category(category)
        history_bar_request.set_timespan(timespan)
        history_bar_request.set_count(count)
        response = self.client.get_response(history_bar_request)
        return response

    def get_quote(self, symbol, category):
        """
        Query the latest crypto market quote according to the crypto symbol code.

        :param symbol:  symbol code; for example: BTCUSD
        :param category: CRYPTO
        """
        quote_request = GetQuotesRequest()
        quote_request.set_symbol(symbol)
        quote_request.set_category(category)
        response = self.client.get_response(quote_request)
        return response

    def get_snapshot(self, symbols, category):
        """
        Query the latest crypto market symbol quote according to the crypto symbol.

        :param symbols: List of symbol codes; for example: single: BTCUSD multiple: BTCUSD,PEPEUSD;
        For each request,up to 100 symbols;
        :param category: CRYPTO
        """
        quote_request = GetSnapshotRequest()
        quote_request.set_symbols(symbols)
        quote_request.set_category(category)
        response = self.client.get_response(quote_request)
        return response


