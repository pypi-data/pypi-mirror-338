## GoPocket API - The Official Python SDK for Smart Trading  

The GoPocket Python SDK provides a streamlined interface for secure and efficient communication with the GoPocket API. It offers extensive features to manage trading operations, monitor market data, and handle account management seamlessly.  

* __Author: [CodiFi](https://github.com/Periyasamy-Dev)__
* **Current Version: 1.0.0**


### Installation

To install the GoPocket SDK using pip, run the following command: 

```
pip install gopocket-tradehub
```

Ensure that Python 3.8 or higher is installed on your system

```
python --version
```

#### Update pip 
To force update pip to the latest version, you can run the following command:
```
python -m pip install --upgrade --force-reinstall pip
```

---

### REST Documentation

For detailed information on the underlying REST API, refer to the official GoPocket API documentation:  
[GoPocket API Documentation](https://docs.gopocket.in/apidocs/v1/)

---

### Getting Started with API

The GoPocket SDK has primary classes: `Trading`.  
- **Trading Class**: This class handles direct interactions with the GoPocket API, including managing sessions, placing orders, and retrieving market data.

#### Session Management
The `get_session_id` method is used to retrieve a Session ID from the GoPocket server. A Session ID remains valid until you log out from your trading account. It is recommended to generate the Session ID once during login and store it securely for reuse.

#### 1. Import the Library
Import the required class from the SDK:
```python
from tradehub.tradify import *
```

#### 2. Create a Trading Object
Initialize a Trading object using your user_id, auth_Code, and secret_key
```python
trade = Trading(user_id="YOUR_USER_ID", auth_Code="YOUR_AUTH_CODE", secret_key="YOUR_SECRET_KEY")
```

#### 3. Get Session
Run the following command.
```python
print(trade.get_session_id()) # Get Session ID
```

#### 4. Download the contract master
Master contracts simplify the process of finding instruments using their symbol names and placing orders. These contracts are saved locally as CSV files, organized by token number and symbol name.

By default, master contracts for all enabled exchanges in your profile are downloaded. To download contracts for specific enabled exchanges, such as ['NSE', 'CDS', 'BSE', 'BFO', 'MCX', 'NFO', 'INDICES'], replace "EXCHANGE" with the relevant exchange names in the following command:
```python
trade.get_contract_master("EXCHANGE")
```

#### 5. Retrieve Available Instruments for Trading
Instruments can be fetched based on their symbol, token, or Futures & Options (FNO) from the downloaded contract master as shown below:
```python
# Fetching instrument by symbol (TCS) or trading symbol (TCS-EQ) for any exchange
print(trade.get_instrument_by_symbol('NSE', 'TCS'))

# Fetching instrument by token for any exchange
print(trade.get_instrument_by_token('MCX', '433355'))

# Fetching Futures & Options instrument with expiry and strike details
print(trade.get_instrument_for_fno(exch='MCX', symbol='SILVER', expiry_date='2025-04-24', strike='91000', is_fut=False, is_CE=True))
```

---

### Predefined Categories

The following predefined categories are used for order placement or modify and data retrieval. You can use these categories or, if you already know their corresponding values, you can pass them directly.

1. **TransactionType**: Specifies the type of transaction.

   * `TransactionType.Buy`: **BUY**
   * `TransactionType.Sell`: **SELL**
   * `TransactionType.B`: **B**
   * `TransactionType.S`: **S**


2. **OrderType**: Specifies the type of order.

   * `OrderType.Regular`: **Regular**
   * `OrderType.AMO`: **AMO** (After Market Order)
   * `OrderType.Cover`: **Cover**
   * `OrderType.Bracket`: **Bracket**
   * `OrderType.CO`: **CO** (Cover Order)
   * `OrderType.BO`: **BO** (Bracket Order)


3. **PriceType**: Specifies the pricing mechanism.
    
    * `PriceType.Limit`: **L** (Limit Order)
    * `PriceType.Market`: **MKT** (Market Order)
    * `PriceType.stopLose`: **SL** (Stop Loss Limit Order)
    * `PriceType.StopLossMarket`: **SL-M** (Stop Loss Market Order)


4. **ProductType**: Defines the product category.

   * `ProductType.Intraday`: **MIS** (Margin Intraday Square-off)
   * `ProductType.Delivery`: **CNC** (Cash and Carry)
   * `ProductType.MTF`: **MTF** (Margin Trading Facility)
   * `ProductType.Normal`: **NRML** (Normal order)
   * `ProductType.GTT`: **GTT** (Good Till Triggered)


5. **PositionType**: Defines how the position is managed.

    * `posDAY`: **DAY** (Intraday position)
    * `posNET`: **NET** (Carry forward position)
    * `posIOC`: **IOC** (Immediate or Cancel)

---

### Order & Trade Management

#### Place Order

```python
placeOrder = trade.placeOrder(exchange='NSE', tradingSymbol='IDEA-EQ',
                              quantity='1', price='10',
                              product=ProductType.Intraday,
                              transType=TransactionType.Buy,
                              priceType=PriceType.stopLose,
                              orderType=OrderType.Regular,
                              positionType=PositionType.posDAY,
                              triggerPrice='9',
                              disclosedQty='',
                              mktProtection='',
                              target='',
                              stopLoss='',
                              source='API',
                              trailingPrice='',
                              remarks='regular')

print("User placeOrder :", placeOrder)
```

#### Modify Order

```python
            modifyOrder = trade.modifyOrder(exchange='NSE',
                                            tradingSymbol="SBIN-EQ",
                                            orderNo="25040100008462",
                                            quantity='1',
                                            positionType=PositionType.posDAY,
                                            priceType=PriceType.Market,
                                            transType=TransactionType.Buy,
                                            price='0',
                                            triggerPrice='',
                                            disclosedQty='',
                                            mktProtection='',
                                            target='5',
                                            stopLoss='5',
                                            trailingPrice='')
            
            print("User Modify_Order :", modifyOrder)
```

#### Cancel Order

```python
print(trade.get_cancelOrder(orderNo='25033100000020'))
```

#### Retrieving order and trade history

#### Retrieve order history

```python
print(trade.get_orderHistory(orderNo="OEBUC0005814"))
```

#### Retrieve order book

```python
print(trade.get_orderbook())
```

#### Retrieve trade book

```python
print(trade.get_Tradebook())
```

### User & Portfolio Management

#### Retrieve profile
```python
print(trade.get_profile())
```

#### Retrieve funds
```python
print(trade.get_funds())
```

#### Retrieve holdings
```python
print(trade.get_holdings())
```

#### Retrieve positions
```python
print(trade.get_positions())
```
### Position & Margin Management

#### Position Conversion
```python
            posCon = trade.positionsConversion(exchange='NSE',
                                                tradingSymbol="JIOFIN-EQ",
                                                quantity=1,
                                                product=ProductType.Intraday,
                                                prevProduct=ProductType.Delivery,
                                                transType=TransactionType.Buy,
                                                posType=PositionType.posDAY,
                                                orderSource=OrderSource.WEB)

            print("User posConversion :", posCon)
```

#### Retrieve margin
```python
            get_margin = trade.get_margin(orderFlag="NEW", product=ProductType.Intraday,
                                   priceType=PriceType.Limit,
                                   orderType=OrderType.Regular,
                                   transType=TransactionType.Buy,
                                   price='3500',
                                   triggerPrice='0',
                                   stopLoss='0',
                                   quantity='1',
                                   instrument=trade.get_instrument_by_symbol(exchange='NSE', symbol='TCS-EQ'))

            print("User get_margin :", get_margin)
```

### Chart & Historical Data

```python
            getChartHistory = trade.get_ChartHistory(instrument=trade.get_instrument_by_symbol(exchange='NSE', symbol='ABB-EQ'),
                                                     resolution='1D',
                                                     from_datetime='2025-03-24',
                                                     to_datetime='2025-03-31 10:10:00',
                                                     user='AB0698')
            print("User getChartHistory :", getChartHistory)
```

---

### General instruction

* Quantity must be greater than zero for all order types

#### Regular and AMO Orders:
1. ##### Limit Orders:
   * Price must be greater than zero. All other (stoploss, trigger price, target) fields can remain empty.

2. ##### Market Orders:
   * Price should be zero. Other (stoploss, trigger price, target) fields can remain empty.

3. ##### Stop Loss Limit Orders:
   * Both Price and Trigger Price must be greater than zero.
   * For SL Buy orders, Trigger Price should either equal Price or be less than Price.
   * For SL Sell orders, Trigger Price should either equal Price or be grater than Price.

4. ##### Stop Loss Market Orders:
   * Price should be zero. 
   * Trigger Price must be greater than zero. Other (stoploss, target) fields can remain empty.

#### Cover Orders:
1. ##### Limit Orders:
   * Both Price and Stoploss must be greater than zero. Other (stoploss, trigger price, target) fields can remain empty.

2. ##### Market Orders:
   * Price should be zero.
   * Stoploss must be greater than zero, with a typical example being Price as 100 and Stoploss as 5. Other (trigger price, target) fields can remain empty.

3. ##### Stop Loss Limit Orders:
   * Price and Trigger Price and must be greater than zero.
   * Stoploss must be greater than zero, with a typical example being Price as 100 and Stoploss as 5. Other (target) fields can remain empty.

#### Bracket Orders:
   * Target must be greater than zero, and other validations can follow similar rules to Cover Orders.

---

## Read this before creating an issue
Before creating an issue in this library, please follow the following steps.

1. Search the problem you are facing is already asked by someone else. There might be some issues already there, either solved/unsolved related to your problem. Go to [issues](https://github.com/jerokpradeep/pya3/issues)
2. If you feel your problem is not asked by anyone or no issues are related to your problem, then create a new issue.
3. Describe your problem in detail while creating the issue. If you don't have time to detail/describe the problem you are facing, assume that I also won't be having time to respond to your problem.
4. Post a sample code of the problem you are facing. If I copy paste the code directly from issue, I should be able to reproduce the problem you are facing.
5. Before posting the sample code, test your sample code yourself once. Only sample code should be tested, no other addition should be there while you are testing.
6. Have some print() function calls to display the values of some variables related to your problem.
7. Post the results of print() functions also in the issue.
8. Use the insert code feature of github to inset code and print outputs, so that the code is displayed neat. ![image](https://user-images.githubusercontent.com/38440742/85207234-4dc96f80-b2f5-11ea-990c-df013dd69cf2.png)
9. If you have multiple lines of code, use triple grave accent ( ``` ) to insert multiple lines of code. [Example:](https://docs.github.com/en/github/writing-on-github/creating-and-highlighting-code-blocks) ![image](https://user-images.githubusercontent.com/38440742/89105781-343a3e00-d3f2-11ea-9f86-92dda88aa5bf.png)

---

## Order Validation Logic

### Regular and AMO Orders

#### Limit Orders
- `priceType` in {"LIMIT", "L"}
- `price` must be greater than zero.
- `Trigger Price`, `Stop Loss`, and `Target` must be empty.

#### Market Orders
- `priceType` in {"MARKET", "M", "MKT"}
- `price` must be zero.
- `Trigger Price`, `Stop Loss`, and `Target` must be empty.

#### Stop Loss Limit Orders
- `priceType` in {"SL", "STOPLOSS"}
- `price` and `triggerPrice` must be greater than zero.
- For `BUY` orders, `triggerPrice` must be ≤ `price`.
- For `SELL` orders, `triggerPrice` must be ≥ `price`.
- `Stop Loss` and `Target` must be empty.

#### Stop Loss Market Orders
- `priceType` in {"SL-M", "STOPLOSS-MARKET"}
- `price` must be zero.
- `triggerPrice` must be greater than zero.
- `Stop Loss` and `Target` must be empty.

---

### Cover and Bracket Orders

#### Bracket Orders
- `orderType` in {"BRACKET", "BO"}
- `target` must be greater than zero.

#### Cover or Bracket Limit Orders
- `priceType` in {"LIMIT", "L"}
- `price` and `stopLoss` must be greater than zero.
- `Trigger Price` must be empty.

#### Cover or Bracket Market Orders
- `priceType` in {"MARKET", "M", "MKT"}
- `price` must be zero.
- `stopLoss` must be greater than zero.
- `Trigger Price` must be empty.

#### Cover or Bracket Stop Loss Limit Orders
- `priceType` in {"SL", "STOPLOSS"}
- `price`, `triggerPrice`, and `stopLoss` must be greater than zero.
- For `BUY` orders, `triggerPrice` must be ≤ `price`.
- For `SELL` orders, `triggerPrice` must be ≥ `price`.

----