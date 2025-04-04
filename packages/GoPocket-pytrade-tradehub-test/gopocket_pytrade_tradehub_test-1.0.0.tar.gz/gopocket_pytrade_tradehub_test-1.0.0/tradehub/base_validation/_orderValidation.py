"""
All Types and Orders validation
"""

#-----------------------------------------------------------------------------------------------------------------------


class Validator:
    """A powerful universal validation class."""

    ## === Single Value Validations === ##

    @staticmethod
    def is_empty(value, field_name="Value"):
        """Check if a value is empty string."""
        if isinstance(value, str) and value.strip() == "":
            raise ValueError(f"{field_name} cannot be empty string.")

    @staticmethod
    def is_notEmpty(value, field_name="Value"):
        """Check if a value is empty string."""
        if value != "":
            print("value", value)
            raise ValueError(f"{field_name} must be empty string.")

    @staticmethod
    def is_none(value, field_name="Value"):
        """Check if a value is None."""
        if value is None:
            raise ValueError(f"{field_name} is required and cannot be None.")

    @staticmethod
    def is_pos_num(value, field_name="Value"):
        """Check if a value is a positive number (greater than zero)."""
        # If value is not an int or float, try converting it
        if not isinstance(value, (int, float)):
            try:
                value = float(value)  # Convert string numbers like "5.5" or "10" to float
            except ValueError:
                raise TypeError(f"{field_name} must be a valid number greater than zero.")

        # Ensure the number is greater than zero
        if value <= 0:
            raise ValueError(f"{field_name} must be greater than zero.")

    ## === Dict Value Validations === ##

    @staticmethod
    def validate_empty(fields: dict):
        """Validate that all required string fields are non-empty."""
        for field_name, value in fields.items():
            Validator.is_empty(value, field_name)  # Ensure it's not empty string

    @staticmethod
    def validate_notEmpty(fields: dict):
        """Validate that all required string fields are empty."""
        for field_name, value in fields.items():
            Validator.is_notEmpty(value, field_name)  # Ensure it's empty string

    @staticmethod
    def validate_none(fields: dict):
        """Validate that all required fields are not None."""
        for field_name, value in fields.items():
            Validator.is_none(value, field_name)  # Ensure it's not None

    @staticmethod
    def validate_pos_num(fields: dict):
        """Validate that all required numeric fields are positive numbers."""
        for field_name, value in fields.items():
            Validator.is_none(value, field_name)  # Ensure it's not None
            Validator.is_pos_num(value, field_name)  # Ensure it's a valid positive number


#-----------------------------------------------------------------------------------------------------------------------


def validate_place_order(exchange, tradingSymbol, transType, orderType, priceType, product, positionType, quantity,
                         price, triggerPrice=None, stopLoss=None, target=None):

    ## === Validator Start === ##

    # Validate empty string or none types
    check_empty = {
        "Trading Symbol": tradingSymbol,
        "Exchange": exchange,
        "Position Type": positionType,
        "Trans Type": transType,
        "Price Type": priceType,
        "Order Type": orderType,
        "Product": product
    }

    Validator.validate_none(check_empty)
    Validator.validate_empty(check_empty)

    # Convert inputs to float
    try:
        def to_float(value):
            return float(value) if value not in [None, ""] and not (
                        isinstance(value, str) and value.strip() == "") else value

        quantity, price, triggerPrice, stopLoss, target = map(to_float,
                                                              [quantity, price, triggerPrice, stopLoss, target])
    except Exception as e:
        raise ValueError(f"Error converting input values: {e}")

    # Validate numeric types
    Validator.is_pos_num(quantity, "Quantity")

    ## === Validator End === ##

    transType = str(transType).upper()
    orderType = str(orderType).upper()
    priceType = str(priceType).upper()

    # Regular and AMO Orders
    if orderType in {"REGULAR", "AMO"}:

        if priceType in {"LIMIT", "L"}:
            if price in {None, "", 0, "0"} or price <= 0:
                raise ValueError("Price must be greater than zero for Limit Orders.")

            check_notEmpty = {
                "Trigger Price": triggerPrice,
                "Stop Loss": stopLoss,
                "Target": target
            }

            Validator.validate_notEmpty(check_notEmpty)

        if priceType in {"MARKET", "M", "MKT"}:
            if price not in {0, "0"}:
                raise ValueError("Price must be zero for Market Orders.")

            check_notEmpty = {
                "Trigger Price": triggerPrice,
                "Stop Loss": stopLoss,
                "Target": target
            }

            Validator.validate_notEmpty(check_notEmpty)

        if priceType in {"SL", "STOPLOSS"}:
            if any(value in {None, "", 0, "0"} or value <= 0 for value in {price, triggerPrice}):
                raise ValueError("Both Price and Trigger Price must be greater than zero for Stop Loss Limit Orders.")

            if transType in {"BUY", "B"} and triggerPrice >= price:
                raise ValueError("For SL Buy Orders, Trigger Price must be less than or equal to Price.")

            if transType in {"SELL", "S"} and triggerPrice <= price:
                raise ValueError("For SL Sell Orders, Trigger Price must be greater than or equal to Price.")

            check_notEmpty = {
                "Stop Loss": stopLoss,
                "Target": target
            }

            Validator.validate_notEmpty(check_notEmpty)

        if priceType in {"SL-M", "STOPLOSS-MARKET"}:
            if price not in {0, "0"}:
                raise ValueError("Price must be zero for Stop Loss Market Orders.")

            if not triggerPrice or triggerPrice <= 0:
                raise ValueError("Trigger Price must be greater than zero for Stop Loss Market Orders.")

            check_notEmpty = {
                "Stop Loss": stopLoss,
                "Target": target
            }

            Validator.validate_notEmpty(check_notEmpty)

    # Cover and Bracket Orders
    if orderType in {"COVER", "CO", "BRACKET", "BO"}:

        if orderType in {"BRACKET", "BO"}:
            if any(value in {None, "", 0, "0"} or value <= 0 for value in {target}):
                raise ValueError("Target must be greater than zero for Bracket Orders.")

        if priceType in {"LIMIT", "L"}:
            if any(value in {None, "", 0, "0"} or value <= 0 for value in {price, stopLoss}):
                raise ValueError(
                    "Both Price and Stop Loss must be greater than zero for Cover or Bracket Limit Orders.")

            check_notEmpty = {
                "Trigger Price": triggerPrice
            }

            Validator.validate_notEmpty(check_notEmpty)

        if priceType in {"MARKET", "M", "MKT"}:
            if price not in {0, "0"}:
                raise ValueError("Price must be zero for Market Orders.")

            if any(value in {None, "", 0, "0"} or value <= 0 for value in {stopLoss}):
                raise ValueError("Stop Loss must be greater than zero for Cover or Bracket Market Orders.")

            check_notEmpty = {
                "Trigger Price": triggerPrice
            }

            Validator.validate_notEmpty(check_notEmpty)

        if priceType in {"SL", "STOPLOSS"}:
            if any(value in {None, "", 0, "0"} or value <= 0 for value in {price, triggerPrice, stopLoss}):
                raise ValueError(
                    "Price, Trigger Price, and Stop Loss must be greater than zero for Cover or Bracket Stop Loss Limit Orders.")

            if transType in {"BUY", "B"} and triggerPrice >= price:
                raise ValueError("For SL Buy Orders, Trigger Price must be less than or equal to Price.")

            if transType in {"SELL", "S"} and triggerPrice <= price:
                raise ValueError("For SL Sell Orders, Trigger Price must be greater than or equal to Price.")

    return "Place order validation successful"

def validate_modify_order(tradingSymbol, exchange, orderNo, quantity, price, triggerPrice, disclosedQty,
                          mktProtection, target, stopLoss, positionType, transType, priceType):
    ## === Validator Start === ##

    # Validate empty string types
    check_empty = {
        "Trading Symbol": tradingSymbol,
        "Exchange": exchange,
        "Order Number": orderNo,
        "Position Type": positionType,
        "Trans Type": transType,
        "Price Type": priceType,
    }

    Validator.validate_none(check_empty)
    Validator.validate_empty(check_empty)

    # Validate none types
    check_none = {
        "Trigger Price": triggerPrice,
        "Disclosed Qty": disclosedQty,
        "MKT Protection": mktProtection,
        "Target": target,
        "Stop Loss": stopLoss,
    }

    Validator.validate_none(check_none)

    # Validate numeric types
    check_pos_num = {
        "Quantity": quantity,
        "Price": price,
    }

    Validator.validate_pos_num(check_pos_num)

    ## === Validator End === ##

    raise "Modify order validation successful"


def validate_cancel_order(orderNo):
    ## === Validator Start === ##

    # Validate none types
    Validator.is_none(orderNo, "Order Number")

    # Numeric validation
    Validator.is_empty(orderNo, "Order Number")

    ## === Validator End === ##

    raise "Cancel order validation successful."


def validate_chart_history(token, exchange, user, resolution):
    ## === Validator Start === ##

    # Validate empty string types
    check_empty = {
        "Token": token,
        "Exchange": exchange,
        "User": user,
        "Resolution": resolution
    }

    Validator.validate_none(check_empty)
    Validator.validate_empty(check_empty)

    ## === Validator End === ##

    raise "Chart history validation successful."


def validate_get_margin(tradingSymbol, exchange, orderFlag, product, transType, priceType, orderType):
    ## === Validator Start === ##

    # Validate empty string types
    check_empty = {
        "Trading Symbol": tradingSymbol,
        "Exchange": exchange,
        "Order Flag": orderFlag,
        "Product": product,
        "Trans Type": transType,
        "Price Type": priceType,
        "Order Type": orderType,
    }

    Validator.validate_none(check_empty)
    Validator.validate_empty(check_empty)

    ## === Validator End === ##

    # Validate Transaction Type
    if transType not in {"BUY", "SELL", "B", "S"}:
        raise TypeError("Transaction Type must be one of the following: 'BUY', 'SELL', 'B', or 'S'.")

    raise "Get margin validation successful."


def validate_posConvertion(tradingSymbol, exchange, product, prevProduct, transType, posType, quantity):
    ## === Validator Start === ##

    # Validate empty string types
    check_empty = {
        "Trading Symbol": tradingSymbol,
        "Exchange": exchange,
        "Product": product,
        "Prev Product": prevProduct,
        "Trans Type": transType,
        "pos Type": posType,
    }

    Validator.validate_none(check_empty)
    Validator.validate_empty(check_empty)

    # Validate Transaction Type
    if transType not in {"BUY", "SELL", "B", "S"}:
        raise TypeError("Transaction Type must be one of the following: 'BUY', 'SELL', 'B', or 'S'.")

    # Validate numeric types
    check_pos_num = {
        "Quantity": quantity
    }

    Validator.validate_pos_num(check_pos_num)

    ## === Validator End === ##

    raise "Position convertion validation successful."


#-----------------------------------------------------------------------------------------------------------------------