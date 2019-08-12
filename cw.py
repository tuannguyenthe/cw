import csv
from cw_product import CW


def main():
    with open('./data/cw.csv') as csvfile:
        read_masterfile(csvfile)

    with open('./data/raw_cw_price.csv') as csvfile:
        read_dailyprice(csvfile)


def read_masterfile(csvfile):
    csvreader = csv.DictReader(csvfile, delimiter=',')
    for row in csvreader:
        a = CW(name=row['symbol'], symbol=row['symbol'], issuer=row['issuer'],
               listed_shares=row['listed_shares'], first_trading=row['first_trading'],
               last_trading=row['last_trading'], cw_type=row['type'], conversion=row['conversion'],
               ipo_date=row['ipo_date'], ipo_price=row['ipo_price'], strike=row['strike'],
               maturity=row['maturity'])
        print(a.cw_remaining())

def read_dailyprice(csvfile):
    csvreader = csv.DictReader(csvfile, delimiter=';')
    for row in csvreader:
        print(row)


if __name__ == "__main__":
    main()
