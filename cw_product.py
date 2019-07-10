from dataclasses import dataclass


@dataclass
class Product:
    symbol: str
    issuer: str
    listed_shares: int = 0
    first_trading: str
    last_trading: str

@dataclass
class CW_Product(Product):
    cw_type: str
    underlying: str
    conversion: float
    strike: float
    ipo_price: float
    ipo_date: str
    maturity: str

@dataclass
class Stock:
    symbol: str
    name: str
    issuer: str
    listed_shares: str
    first_trading: str
    last_trading: str
    
    
"""
class CW_Product:
    def __init__(self, symbol, ipo_price, first_trading, last_trading, strike):
        self.symbol = symbol
        self.first_trading = first_trading
        self.last_trading = last_trading
        self.strike = strike
        self.ipo_price = ipo_price
"""

x = CW_Product(symbol="CFPT1091", cw_type="haha", cw_issuer="sds", underlying="sdsd", conversion=1.0, listed_shares=2000000, first_trading="osdiosdi", last_trading="skdsidu", strike=30.2, ipo_price=45.2, ipo_date="hiih", ex_date="skdjk")
print(x)
