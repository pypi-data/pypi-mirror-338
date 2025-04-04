class Props:
    # Mandatory for broker name for order also ["GoPocket"=001, "Jainam"=002, "TrustLine"=003, "AliceBlue"=004, "Goodwill"=005, "IIFL"=006]
    broker_name = "001"

    # setup.py ---------------------------------------------------------------------------------------------------------
    pip_name = "GoPocket-pytrade-tradehub-test"
    pip_version = "1.0.0"
    setup_author = "Codifi"
    setup_author_email = "periyasamy@codifi.in"
    setup_description = "Python SDK for integrating with Jainam trading platform."
    setup_license = "MIT"
    setup_url = "https://protrade.jainam.in/"
    setup_downloadable_url = "https://github.com/Periyasamy-Dev/jainam_sdk.git"
    setup_apidocs = "https://docs.gopocket.in/apidocs/"

    # tradify.py -------------------------------------------------------------------------------------------------------
    base_url = "https://web.gopocket.in/"
    api_name = "Codifi API Connect - Python Lib"
    base_url_c = "https://web.gopocket.in/contract/csv/"

    getSessionData = "am/sso/vendor/getUserDetails"

    ordExecute = "od-rest/orders/execute"
    ordModify = "od-rest/api/orders/modify"
    ordCancel = "od-rest/orders/cancel"
    ordGetMargin = "od-rest/orders/getmargin"
    getOrderbook = "od-rest/api/info/orderbook"
    getTradebook = "od-rest/api/info/tradebook"
    getOrdHistory = "od-rest/api/info/history"

    getHoldings = "ho-rest/api/holdings/"
    getPositions = "po-rest/positions/"
    posConversion = "po-rest/positions/conversion"

    getFunds = "funds-rest/api/funds/limits"

    getProfile = "client-rest/profile/getclientdetails"

    getChartHistory = "rest/ChartAPIService/chart/history"

    # # # setup.py ---------------------------------------------------------------------------------------------------------
    # pip_name = "jainam-pytrade-sdk-test"
    # pip_version = "1.0.6"
    # setup_author = "Codifi"
    # setup_author_email = "periyasamy@codifi.in"
    # setup_description = "Python SDK for integrating with Jainam trading platform."
    # setup_license = "MIT"
    # setup_url = "https://protrade.jainam.in/"
    # setup_downloadable_url = "https://github.com/Periyasamy-Dev/jainam_sdk.git"
    # setup_apidocs = "https://protrade.jainam.in/apidocs/"
    #
    #
    # # tradify.py -------------------------------------------------------------------------------------------------------
    # base_url = "https://protrade.jainam.in/"
    # api_name = "Codifi API Connect - Python Lib"
    # base_url_c = "https://protrade.jainam.in/contract/csv/"
    #
    # getSessionData = "omt/auth/sso/vendor/getUserDetails"
    #
    # ordExecute = "api/od-rest/orders/execute"
    # ordModify = "api/od-rest/orders/modify"
    # ordCancel = "api/od-rest/orders/cancel"
    # ordGetMargin = "api/od-rest/orders/getmargin"
    # getOrderbook = "api/od-rest/info/orderbook"
    # getTradebook = "api/od-rest/info/tradebook"
    # getOrdHistory = "api/od-rest/info/history"
    #
    # getHoldings = "api/ho-rest/holdings/"
    # getPositions = "api/po-rest/positions/"
    # posConversion = "api/po-rest/positions/conversion"
    #
    # getFunds = "api/funds-rest/funds/limits"
    #
    # getProfile = "api/client-rest/profile/getclientdetails"
    #
    # getChartHistory = ""
