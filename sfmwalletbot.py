from bscscan import BscScan
from pycoingecko import CoinGeckoAPI
import json
import decimal
cg = CoinGeckoAPI()

bsc = BscScan("ABZ3YV2I961GK1HJDPXN7GUQB6WIPEWUWU") # key in quotation marks

address = input("Which address do you want to convert? ")
currencyvs = input("Which currency do you want to convert to? ")
example = int(bsc.get_acc_balance_by_token_contract_address(contract_address="0x8076c74c5e3f5852037f31ff0093eeb8c8add8d3", address=address))
example2 = example * 0.000000001
print("SFM Wallet Balance:", example2,"SFM")

example4 = cg.get_price(ids="safemoon", vs_currencies=currencyvs)
nokprice = (example4["safemoon"][currencyvs])
nokpriceformat = format(nokprice, 'f')
sfmwalletbalanceinnokfinal = int(float(nokprice) * example2) - (float(nokprice) * example2 / 10)
print ("SFM Wallet in NOK:", (int(sfmwalletbalanceinnokfinal)), currencyvs)