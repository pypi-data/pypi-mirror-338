import json
import enum
import hashlib
import logging
import requests
import threading
import numpy as np
import pandas as pd
from collections import namedtuple
from datetime import time, datetime

from config.config import *
from tradehub.base_validation.checksum import *
from tradehub.base_validation.file_read import *
from tradehub.base_validation.timestamp import *
from tradehub.base_validation._orderValidation import *


logger = logging.getLogger(__name__)

Instrument = namedtuple('Instrument', ['exchange', 'token', 'symbol', 'trading_symbol', 'expiry', 'lot_size'])


"""Predefined Categories"""

class TransactionType(enum.Enum):
    Buy = "BUY"
    Sell = "SELL"
    B = "B"
    S = "S"

class PositionType(enum.Enum):
    posDAY = "DAY"
    posNET = "NET"
    posIOC = "IOC"

class OrderType(enum.Enum):
    Regular = 'Regular'
    AMO = 'AMO'
    Cover = 'Cover'
    Bracket = 'Bracket'
    CO = 'CO'
    BO = 'BO'

class OrderSource(enum.Enum):
    WEB = 'WEB'
    API = 'API'
    MOB = 'MOB'

class ProductType(enum.Enum):
    Intraday = 'MIS'
    Delivery = 'CNC'
    MTF = 'MTF'
    Normal = 'NRML'
    GTT = 'GTT'

class PriceType(enum.Enum):
    Limit = 'L'
    Market = 'MKT'
    stopLose = 'SL'
    StopLossMarket = 'SL-M'


class Trading:
    base_url = Props.base_url
    api_name = Props.api_name
    version = Props.pip_version
    base_url_c = Props.base_url_c

    _sub_urls = {
        # Authorization
        "getSessionData": Props.getSessionData,

        # OrderManagement
        "ordExecute": Props.ordExecute,
        "ordModify": Props.ordModify,
        "ordCancel": Props.ordCancel,
        "ordGetMargin": Props.ordGetMargin,
        "getOrderbook": Props.getOrderbook,
        "getTradebook": Props.getTradebook,
        "getOrdHistory": Props.getOrdHistory,

        # Portfolio
        "getHoldings": Props.getHoldings,
        "getPositions": Props.getPositions,
        "posConversion": Props.posConversion,

        # Funds
        "getFunds": Props.getFunds,

        # Profile
        "getProfile": Props.getProfile,

        # Chart History
        "getChartHistory": Props.getChartHistory

    }

    # Common Method
    def __init__(self,
                 user_id,
                 auth_Code,
                 secret_key,
                 base=None,
                 session_id=None):

        self.user_id = user_id.upper()
        self.auth_Code = auth_Code
        self.secret_key = secret_key
        self.session_id = session_id
        self.base = base or self.base_url

    """API Request Module for POST and GET method"""

    def _request(self, url, req_type, data=None):
        _headers = {
            "Authorization": self.sessionAuthorization()
        }

        if req_type == "POST":
            try:
                response = requests.post(url, json=data, headers=_headers, )
            except (requests.ConnectionError, requests.Timeout) as exception:
                return {'stat': 'Not_ok', 'emsg': exception, 'encKey': None}
            if response.status_code == 200:
                return json.loads(response.text)
            else:
                emsg = str(response.status_code) + ' - ' + response.reason
                return {'stat': 'Not_ok', 'emsg': emsg, 'encKey': None}

        elif req_type == "GET":
            try:
                response = requests.get(url, json=data, headers=_headers)
            except (requests.ConnectionError, requests.Timeout) as exception:
                return {'stat': 'Not_ok', 'emsg': exception, 'encKey': None}
            if response.status_code == 200:
                return json.loads(response.text)
            else:
                emsg = str(response.status_code) + ' - ' + response.reason
                return {'stat': 'Not_ok', 'emsg': emsg, 'encKey': None}
        elif req_type == "GET" and data == "QueryParams":
            try:
                response = requests.get(url, json=data, headers=_headers)
            except (requests.ConnectionError, requests.Timeout) as exception:
                return {'stat': 'Not_ok', 'emsg': exception, 'encKey': None}
            if response.status_code == 200:
                return json.loads(response.text)
            else:
                emsg = str(response.status_code) + ' - ' + response.reason
                return {'stat': 'Not_ok', 'emsg': emsg, 'encKey': None}

    def _errorResponse(self, message):
        return {"stat": "Not_ok", "emsg": message}

    """API Methods declaration"""

    def _get(self, sub_url, data=None):
        """Get method declaration"""
        url = self.base + self._sub_urls[sub_url]
        return self._request(url, "GET", data=data)

    def _get_QueryParams(self, sub_url, data=None):
        """Get method declaration"""
        url = self.base + self._sub_urls[sub_url] + data
        return self._request(url, "GET", data="QueryParams")

    def _post(self, sub_url, data=None):
        """Post method declaration"""
        url = self.base + self._sub_urls[sub_url]
        return self._request(url, "POST", data=data)

    """API User Authorization Part"""

    def get_session_id(self, data=None):
        data = generate_checksum(self.user_id, self.auth_Code, self.secret_key)
        data = {'checkSum': data}

        response = self._post("getSessionData", data)

        """
        Extract accessToken from the response if status is 'Ok'.
        """

        # Extract accessToken or userSession dynamically
        if response.get('status') == 'Ok' and 'result' in response and len(response['result']) > 0:
            access_token = response['result'][0].get('accessToken')
            self.session_id = access_token
        elif response.get('stat') == 'Ok' and response.get('userSession'):
            self.session_id = response.get('userSession')
        else:
            self.session_id = None

        return response

    def sessionAuthorization(self):
        if self.session_id:
            return "Bearer " + self.session_id
        else:
            return ""

    """User & Portfolio Management Part"""

    def get_profile(self):
        profile = self._get("getProfile")
        return profile

    def get_funds(self):
        funds = self._get("getFunds")
        return funds

    def get_holdings(self):
        Holdings = self._get("getHoldings")
        return Holdings

    def get_positions(self):
        Positions = self._get("getPositions")
        return Positions

    """Position & Margin Management Part"""

    def positionsConversion(self, exchange=None, tradingSymbol=None, quantity=None, product=None, prevProduct=None,
                            transType=None, posType=None, instrument=None, token=None, orderSource=None):

        # Validate instrument or token
        if instrument is not None:
            if not isinstance(instrument, Instrument):
                raise TypeError("Instrument must be of type Instrument")
            exchange = exchange or instrument.exchange
            tradingSymbol = tradingSymbol or instrument.trading_symbol
            token = token or instrument.token

            if token is None or token == '':
                raise TypeError("Token is required and cannot be None or empty.")

        # # Validate types
        # if not tradingSymbol or not isinstance(tradingSymbol, str) or tradingSymbol.strip() == '':
        #     raise TypeError("Trading Symbol must be a non-empty string and cannot be None")
        # if not exchange or not isinstance(exchange, str) or exchange.strip() == '':
        #     raise TypeError("Exchange must be a non-empty string and cannot be None")
        # if not isinstance(quantity, int):
        #     raise TypeError("Quantity must be an integer")

        # Handle Both Enum and String
        product = getattr(product, 'value', product)
        prevProduct = getattr(prevProduct, 'value', prevProduct)
        transType = getattr(transType, 'value', transType)
        posType = getattr(posType, 'value', posType)

        orderSource = getattr(orderSource, 'value', orderSource) if orderSource else None

        # if transType not in ("BUY", "SELL", "B", "S"):
        #     raise TypeError("Transaction Type must be one of the following: 'BUY', 'SELL', 'B', or 'S'.")
        #
        # # Validate required parameters
        # missing_params = [name for param, name in zip([product, prevProduct, transType, posType],
        #                                               ["product", "prevProduct", "transType", "posType"]) if
        #                   param is None]
        # if missing_params:
        #     raise TypeError(f"Missing or None parameters: {', '.join(missing_params)}")

        validate_posConvertion(tradingSymbol, exchange, product, prevProduct, transType, posType, quantity)

        # Build data based on the format
        data = {
            "exchange": exchange.upper(),
            "tradingSymbol": tradingSymbol.upper(),
            "qty": quantity,
            "product": product,
            "prevProduct": prevProduct,
            "transType": transType,
            "posType": posType,
        }

        if orderSource:
            data["orderSource"] = orderSource
        else:
            data["token"] = token

        # API call
        posConversionResp = self._post("posConversion", data)
        return posConversionResp

    def get_margin(self, orderFlag, product, transType, priceType, orderType, price,
                   triggerPrice, stopLoss, quantity, instrument=None,
                   token=None, exchange=None, tradingSymbol=None, openOrderQty=None):

        # Validate instrument or token and exchange and tradingSymbol
        if instrument is None and not (token and exchange and tradingSymbol):
            raise TypeError(
                "Token, exchange, and tradingSymbol are required when the instrument is not provided. "
                "Please ensure all necessary values are included.")

        if instrument is not None:
            exchange = instrument.exchange
            token = instrument.token
            tradingSymbol = instrument.trading_symbol

        # # Validate types
        # if not isinstance(tradingSymbol, str):
        #     raise TypeError("Trading Symbol must be a string")
        # if not (isinstance(exchange, str)):
        #     raise TypeError("Exchange must be a string")

        # Handle Both Enum and String
        product = (getattr(product, 'value', product))
        transType = (getattr(transType, 'value', transType))
        priceType = getattr(priceType, 'value', priceType)
        orderType = getattr(orderType, 'value', orderType)

        # if transType not in ("BUY", "SELL", "B", "S"):
        #     raise TypeError("Transaction Type must be one of the following: 'BUY', 'SELL', 'B', or 'S'.")
        #
        # # Validate required parameters
        # missing_params = [name for param, name in zip([orderFlag, product, transType, priceType, orderType],
        #                                               ["orderFlag", "product", "transType", "priceType", "orderType"])
        #                   if param is None]
        # if missing_params:
        #     raise TypeError(f"Missing or None parameters: {', '.join(missing_params)}")

        validate_get_margin(tradingSymbol, exchange, orderFlag, product, transType, priceType, orderType)

        # Build data
        data = {
            "orderFlag": orderFlag,
            "transType": transType,
            "exchange": exchange,
            "token": token,
            "qty": quantity,
            "price": price,
            "tradingSymbol": tradingSymbol,
            "product": product,
            "priceType": priceType,
            "triggerPrice": triggerPrice,
            "orderType": orderType,
            "stopLoss": stopLoss
        }

        if openOrderQty is not None:
            data["openOrderQty"] = openOrderQty

        # API call
        ordGetMarginResp = self._post("ordGetMargin", data)
        return ordGetMarginResp

    """Order & Trade Management Part"""

    def placeOrder(self, quantity, price, triggerPrice, disclosedQty, mktProtection, target, stopLoss, product,
                   transType, priceType, orderType, positionType, exchange=None, tradingSymbol=None, token=None,
                   instrument=None, trailingPrice=None, source=None, remarks=None):

        # Validate instrument or token
        if instrument is not None:
            if not isinstance(instrument, Instrument):
                raise TypeError("Instrument must be of type Instrument")
            exchange = exchange or instrument.exchange
            tradingSymbol = tradingSymbol or instrument.trading_symbol
            token = token or instrument.token

            if not token or token == '':
                raise TypeError("Token is required and cannot be None or empty.")

        # Handle Both Enum and String
        product = getattr(product, 'value', product)
        transType = getattr(transType, 'value', transType)
        priceType = getattr(priceType, 'value', priceType)
        orderType = getattr(orderType, 'value', orderType)
        positionType = getattr(positionType, 'value', positionType)

        # missing_params = [
        #     name for param, name in zip(
        #         [product, transType, priceType, orderType, positionType],
        #         ["product", "transType", "priceType", "orderType", "positionType"]
        #     )
        #     if param is None or param == ''
        # ]
        #
        # if missing_params:
        #     raise TypeError(f"Missing or None parameters: {', '.join(missing_params)}")

        # # Validate types
        # if not tradingSymbol or not isinstance(tradingSymbol, str) or tradingSymbol.strip() == '':
        #     raise TypeError("Trading Symbol must be a non-empty string and cannot be None")
        # if not exchange or not isinstance(exchange, str) or exchange.strip() == '':
        #     raise TypeError("Exchange must be a non-empty string and cannot be None")
        # if not quantity:
        #     raise TypeError("Quantity is required and cannot be None or empty.")

        validate_place_order(exchange=exchange, tradingSymbol=tradingSymbol, transType=transType, orderType=orderType,
                       priceType=priceType, product=product, positionType=positionType, quantity=quantity, price=price,
                       triggerPrice=triggerPrice, stopLoss=stopLoss, target=target)

        # Build data based on the format
        data = [
            {
                "exchange": exchange.upper(),
                "tradingSymbol": tradingSymbol.upper(),
                "qty": quantity,
                "price": price,
                "product": product.upper(),
                "transType": transType.upper(),
                "priceType": priceType.upper(),
                "orderType": orderType.upper(),
                "ret": positionType.upper(),
                "triggerPrice": triggerPrice,
                "disclosedQty": disclosedQty,
                "mktProtection": mktProtection,
                "target": target,
                "stopLoss": stopLoss
            }
        ]

        if trailingPrice is not None:
            data[0]["trailingPrice"] = trailingPrice
        if source is not None:
            data[0]["source"] = source
        if remarks is not None:
            data[0]["remarks"] = remarks
        if token is not None:
            data[0]["token"] = token

        # API call
        ordExecuteResp = self._post("ordExecute", data)
        return ordExecuteResp

    def modifyOrder(self, orderNo, quantity, positionType, priceType,
                    transType, price, triggerPrice, disclosedQty,
                    mktProtection, target, stopLoss,
                    exchange=None, tradingSymbol=None, token=None, instrument=None,
                    tradedQty=None, filledQty=None,
                    trailingPrice=None, product=None, orderType=None):

        # Validate instrument or token
        if instrument is not None:
            if not isinstance(instrument, Instrument):
                raise TypeError("Instrument must be of type Instrument")
            exchange = exchange or instrument.exchange
            tradingSymbol = tradingSymbol or instrument.trading_symbol
            token = token or instrument.token

            if not token or token == '':
                raise TypeError("Token is required and cannot be None or empty.")

        # Handle Both Enum and String
        product = getattr(product, 'value', product) if product is not None else None
        orderType = getattr(orderType, 'value', orderType) if orderType is not None else None
        transType = getattr(transType, 'value', transType)
        priceType = getattr(priceType, 'value', priceType)
        positionType = getattr(positionType, 'value', positionType)

        # # Validate types
        # if not tradingSymbol or not isinstance(tradingSymbol, str) or tradingSymbol.strip() == '':
        #     raise TypeError("Trading Symbol must be a non-empty string and cannot be None")
        # if not exchange or not isinstance(exchange, str) or exchange.strip() == '':
        #     raise TypeError("Exchange must be a non-empty string and cannot be None")
        # if not orderNo or not isinstance(orderNo, str) or orderNo.strip() == '':
        #     raise TypeError("Order Number must be a non-empty string and cannot be None")
        # if not positionType or not isinstance(positionType, str) or positionType.strip() == '':
        #     raise TypeError("Position Type must be a non-empty string and cannot be None")
        # if not transType or not isinstance(transType, str) or transType.strip() == '':
        #     raise TypeError("Trans Type must be a non-empty string and cannot be None")
        # if not priceType or not isinstance(priceType, str) or priceType.strip() == '':
        #     raise TypeError("Trans Type must be a non-empty string and cannot be None")
        # if not quantity:
        #     raise TypeError("Quantity is required and cannot be None or empty.")
        # if not price:
        #     raise TypeError("Price is required and cannot be None or empty.")

        # missing_params = [
        #     name for param, name in zip(
        #         [triggerPrice, disclosedQty, mktProtection, target, stopLoss],
        #         ["triggerPrice", "disclosedQty", "mktProtection", "target", "stopLoss"]
        #     )
        #     if param is None
        # ]
        #
        # if missing_params:
        #     raise TypeError(f"Missing or None parameters: {', '.join(missing_params)}")

        validate_modify_order(tradingSymbol, exchange, orderNo, quantity, price, triggerPrice, disclosedQty,
                         mktProtection, target, stopLoss, positionType, transType, priceType)

        # Build data based on the format
        data = {
            "exchange": exchange.upper(),
            "tradingSymbol": tradingSymbol.upper(),
            "orderNo": orderNo,
            "qty": quantity,
            "ret": positionType.upper(),
            "priceType": priceType.upper(),
            "transType": transType.upper(),
            "price": price,
            "triggerPrice": triggerPrice,
            "disclosedQty": disclosedQty,
            "mktProtection": mktProtection,
            "target": target,
            "stopLoss": stopLoss
        }

        if trailingPrice is not None:
            data["trailingPrice"] = trailingPrice
        if tradedQty is not None:
            data["tradedQty"] = tradedQty
        if filledQty is not None:
            data["filledQty"] = filledQty
        if product is not None:
            data["product"] = product
        if orderType is not None:
            data["orderType"] = orderType
        if token is not None:
            data["token"] = token

        # API call
        ordModifyResp = self._post("ordModify", data)
        return ordModifyResp

    def get_cancelOrder(self, orderNo, exchange=None, orderType=None):
        # # Validate exchange, orderNo, orderType
        # if orderNo is None or orderNo == '':
        #     raise TypeError("Order number is required and cannot be empty.")

        validate_cancel_order(orderNo)

        # Handle Both Enum and String
        orderType = (getattr(orderType, 'value', orderType)) if orderType else None

        data = [
            {k: v for k, v in {"exchange": exchange, "orderNo": orderNo, "orderType": orderType}.items() if v}
        ]

        # API call
        ordCancelResp = self._post("ordCancel", data)
        return ordCancelResp

    def get_orderHistory(self, orderNo):
        # Validate orderNo
        if not orderNo or not isinstance(orderNo, str) or orderNo.strip() == '':
            raise TypeError("Order Number must be a non-empty string and cannot be None")

        # Build data
        data = {
            "orderNo": orderNo
        }

        # API call
        getOrdHistoryResp = self._post("getOrdHistory", data)
        return getOrdHistoryResp

    def get_orderbook(self):
        Orderbook = self._get("getOrderbook")
        return Orderbook

    def get_tradebook(self):
        Tradebook = self._get("getTradebook")
        return Tradebook

    """Chart & Historical Data"""

    def get_ChartHistory(self, resolution, from_datetime, to_datetime, user, instrument=None, exchange=None,
                         token=None):

        # Validate instrument or token
        if instrument is not None:
            if not isinstance(instrument, Instrument):
                raise TypeError("Instrument must be of type Instrument")
            exchange = exchange or instrument.exchange
            token = token or instrument.token

        # if not token or token == '':
        #     raise TypeError("Token is required and cannot be None or empty.")
        # if not exchange or not isinstance(exchange, str) or exchange.strip() == '':
        #     raise TypeError("Exchange must be a non-empty string and cannot be None")
        # if not user or not isinstance(user, str) or user.strip() == '':
        #     raise TypeError("User must be a non-empty string and cannot be None")
        # if not resolution or not isinstance(resolution, str) or resolution.strip() == '':
        #     raise TypeError("Resolution must be a non-empty string and cannot be None")

        validate_chart_history(token, exchange, user, resolution)

        # Convert to epoch
        from_timestamp = to_epoch(from_datetime, is_start=True)
        to_timestamp = to_epoch(to_datetime, is_start=False)

        query_param = f'?symbol={token}&resolution={resolution}&from={from_timestamp}&to={to_timestamp}&exchange={exchange}&user={user}'

        # API call
        getOrdHistoryResp = self._get_QueryParams("getChartHistory", query_param)
        return getOrdHistoryResp

    """Contract Master Management Part"""

    def get_contract_master(self, exchange):
        if len(exchange) == 3 or exchange == 'INDICES':
            print(
                "Reminder: The contract master file is updated daily after 08:00 AM. Before this time, the previous day's contract file will be available for download.")
            if time(8, 00) <= datetime.now().time() or True:
                url = self.base_url_c + exchange.lower()
                response = requests.get(url)
                with open("%s.csv" % exchange.upper(), "w") as f:
                    f.write(response.text)
                return self._errorResponse("Today contract File Downloaded")
            else:
                return self._errorResponse("Previous day contract file saved")
        elif exchange is None:
            return self._errorResponse("Invalid Exchange parameter")
        else:
            return self._errorResponse("Invalid Exchange parameter")

    def get_instrument_by_symbol(self, exchange, symbol):

        try:
            contract = contract_read(exchange)
        except OSError as e:
            if e.errno == 2:
                self.get_contract_master(exchange)
                contract = contract_read(exchange)
            else:
                return self._errorResponse(e)

        if exchange == 'INDICES':
            filter_contract = contract[contract['symbol'] == symbol.upper()]
            if len(filter_contract) == 0:
                return self._errorResponse("The symbol is not available in this exchange")
            else:
                filter_contract = filter_contract.reset_index()
                inst = Instrument(filter_contract['exch'][0], filter_contract['token'][0], filter_contract['symbol'][0],
                                  '', '', '')
                return inst

        else:
            filter_contract = contract[
                (contract['Symbol'] == symbol.upper()) | (contract['Trading Symbol'] == symbol.upper())]

            if len(filter_contract) == 0:
                return self._errorResponse("The symbol is not available in this exchange")
            else:
                filter_contract = filter_contract.reset_index()
                if 'expiry_date' in filter_contract:
                    inst = Instrument(filter_contract['Exch'][0], filter_contract['Token'][0],
                                      filter_contract['Symbol'][0], filter_contract['Trading Symbol'][0],
                                      filter_contract['Expiry Date'][0], filter_contract['Lot Size'][0])
                else:
                    inst = Instrument(filter_contract['Exch'][0], filter_contract['Token'][0],
                                      filter_contract['Symbol'][0], filter_contract['Trading Symbol'][0], '',
                                      filter_contract['Lot Size'][0])
                return inst

    def get_instrument_by_token(self, exchange, token):

        try:
            contract = contract_read(exchange)
        except OSError as e:
            if e.errno == 2:
                self.get_contract_master(exchange)
                contract = contract_read(exchange)
            else:
                return self._errorResponse(e)

        if exchange == 'INDICES':
            filter_contract = contract[contract['token'] == token].reset_index(drop=False)
            inst = Instrument(filter_contract['exch'][0], filter_contract['token'][0], filter_contract['symbol'][0], '',
                              '', '')
            return inst

        else:
            filter_contract = contract[contract['Token'] == token]
            if len(filter_contract) == 0:
                return self._errorResponse("The symbol is not available in this exchange")
            else:
                filter_contract = filter_contract.reset_index()
                if 'expiry_date' in filter_contract:
                    inst = Instrument(filter_contract['Exch'][0], filter_contract['Token'][0],
                                      filter_contract['Symbol'][0],
                                      filter_contract['Trading Symbol'][0], filter_contract['Expiry Date'][0],
                                      filter_contract['Lot Size'][0])
                else:
                    inst = Instrument(filter_contract['Exch'][0], filter_contract['Token'][0],
                                      filter_contract['Symbol'][0],
                                      filter_contract['Trading Symbol'][0], '', filter_contract['Lot Size'][0])
                return inst

    def get_instrument_for_fno(self, exch, symbol, expiry_date, is_fut=True, strike=None, is_CE=False):

        if exch in ['NFO', 'CDS', 'MCX', 'BFO', 'BCD']:
            if exch == 'CDS':
                edate_format = '%d-%m-%Y'
            else:
                edate_format = '%Y-%m-%d'
        else:
            return self._errorResponse("Invalid exchange")

        if not symbol:
            return self._errorResponse("Symbol is Null")

        try:
            expiry_date = datetime.strptime(expiry_date, "%Y-%m-%d").date()
        except ValueError as e:
            return self._errorResponse(e)

        if type(is_CE) is bool:
            if is_CE == True:
                option_type = "CE"
            else:
                option_type = "PE"
        else:
            return self._errorResponse("is_fut is not boolean value")

        try:
            contract = contract_read(exch)
        except OSError as e:
            if e.errno == 2:
                self.get_contract_master(exch)
                contract = contract_read(exch)
            else:
                return self._errorResponse(e)

        if is_fut == False:
            if strike:
                filter_contract = contract[(contract['Exch'] == exch) & (
                        (contract['Symbol'] == symbol) | (contract['Trading Symbol'] == symbol)) & (
                                                   contract['Option Type'] == option_type) & (
                                                   (contract['Strike Price'] == int(strike)) | (
                                                   contract['Strike Price'] == strike)) & (
                                                   contract['Expiry Date'] == expiry_date.strftime(edate_format))]
            else:
                filter_contract = contract[(contract['Exch'] == exch) & (
                        (contract['Symbol'] == symbol) | (contract['Trading Symbol'] == symbol)) & (
                                                   contract['Option Type'] == option_type) & (
                                                   contract['Expiry Date'] == expiry_date.strftime(edate_format))]

        if is_fut == True:
            if strike == None:
                filter_contract = contract[(contract['Exch'] == exch) & (
                        (contract['Symbol'] == symbol) | (contract['Trading Symbol'] == symbol)) & (
                                                   contract['Option Type'] == 'XX') & (
                                                   contract['Expiry Date'] == expiry_date.strftime(edate_format))]
            else:
                return self._errorResponse("No strike price for future")

        if len(filter_contract) == 0:
            return self._errorResponse("No Data")

        else:
            inst = []
            token = []
            filter_contract = filter_contract.reset_index()

            for i in range(len(filter_contract)):

                token_value = filter_contract.at[i, 'Token']
                if pd.notnull(token_value):
                    token_value = int(token_value) if isinstance(token_value,
                                                                 (np.int64, np.float64, float)) else token_value

                lotSize_value = filter_contract.at[i, 'Lot Size']
                if pd.notnull(lotSize_value):
                    lotSize_value = int(lotSize_value) if isinstance(lotSize_value,
                                                                     (np.int64, np.float64, float)) else lotSize_value

                if token_value not in token:
                    token.append(token_value)
                    inst.append(Instrument(filter_contract['Exch'][i], token_value,
                                           filter_contract['Symbol'][i], filter_contract['Trading Symbol'][i],
                                           filter_contract['Expiry Date'][i], lotSize_value))

            if len(inst) == 1:
                return inst[0]
            else:
                return inst
