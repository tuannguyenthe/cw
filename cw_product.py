from dataclasses import dataclass
from datetime import date


@dataclass(init=False)
class Equity:
    symbol: str
    name: str
    issuer: str
    listed_shares: int
    first_trading: str
    last_trading: str


@dataclass
class CW(Equity):
    cw_type: str
    underlying: str
    conversion: float
    strike: float
    ipo_price: float
    ipo_date: str
    maturity: str

    def __init__(self, name: str, symbol: str, issuer: str,
                 listed_shares: int, first_trading: str, last_trading: str,
                 cw_type: str, conversion: str, strike: float,
                 ipo_price: float, ipo_date: str, maturity: str) -> None:
        self.name = name
        self.first_trading = date.fromisoformat(first_trading)
        self.issuer = issuer
        self.last_trading = date.fromisoformat(first_trading)
        self.symbol = symbol
        self.listed_shares = listed_shares
        self.listed_shares = listed_shares
        self.cw_type = cw_type
        self.underlying = symbol[1:4]
        self.conversion = conversion
        self.strike = strike
        self.ipo_price = ipo_price
        self.ipo_date = date.fromisoformat(ipo_date)
        self.maturity = date.fromisoformat(maturity)
    
@dataclass
class Stock(Equity):
    pass



