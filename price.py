import numpy as np
from scipy.stats import norm

class BsmModel:
    def __init__(self, option_type, price, strike, interest_rate,
                 expiry, volatility, dividend_yield=0):
        self.s = price  # Underlying asset price
        self.k = strike  # Option strike K
        self.r = interest_rate  # Continuous risk fee rate
        self.q = dividend_yield  # Dividend continuous rate
        self.T = expiry  # time to expiry (year)
        self.sigma = volatility  # Underlying volatility
        self.type = option_type  # option type "p" put option "c" call option

    def n(self, d):
        # cumulative probability distribution function of
        # standard normal distribution
        return norm.cdf(d)

    def dn(self, d):
        # the first order derivative of n(d)
        return norm.pdf(d)

    def d1(self):
        d1 = (np.log(self.s / self.k) + (self.r - self.q + self.sigma ** 2 * 0.5)
             * self.T) / (self.sigma * np.sqrt(self.T))
        return d1

    def d2(self):
        d2 = (np.log(self.s / self.k) + (self.r - self.q - self.sigma ** 2 * 0.5)
             * self.T) / (self.sigma * np.sqrt(self.T))
        return d2

    def bsm_price(self):
        d1 = self.d1()
        d2 = d1 - self.sigma * np.sqrt(self.T)
        if self.type == 'c':
            price = np.exp(-self.r*self.T) * (self.s * np.exp((self.r - self.q)*self.T) * self.n(d1) - self.k * self.n(d2))
            return price
        elif self.type == 'p':
            price = np.exp(-self.r*self.T) * (self.k * self.n(-d2) - (self.s * np.exp((self.r - self.q)*self.T) * self.n(-d1)))
            return price
        else:
            return "option type can only be c or p"

a = BsmModel(option_type='c', price=42, strike=35, interest_rate=0.1,
             expiry=90.0/365, volatility=0.2)

print(a.bsm_price())
