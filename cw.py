import csv
from cw_product import CW

def main():

    with open('./data/cw.csv') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=',')
        for row in csvreader:
            a = CW(name=row['symbol'], symbol = row['symbol'], issuer=row['issuer'], listed_shares = row['listed_shares'], first_trading =row['first_trading'], last_trading = row['last_trading'], cw_type = row['type'], conversion = row['conversion'], ipo_date=row['ipo_date'], ipo_price = row['ipo_price'], strike = row['strike'], maturity=row['maturity'])
            print(a)


if __name__ == "__main__":
    main()
