"""
Expects the user to specify as a command-line argument the number of Bitcoins, n, that they would like to buy. If that argument cannot be converted to a float, the program exits via sys.exit with an error message.
Queries the API for the CoinDesk Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json, which returns a JSON object, among whose nested keys is the current price of Bitcoin as a float.
Outputs the current cost of n Bitcoins in USD to four decimal places, using ',' as a thousands separator.
"""
import requests
import sys
import json

#Expects the user to specify as a command-line argument the number of Bitcoins, sys.argv[1], that they would like to buy
if len(sys.argv) != 2:
    sys.exit("Inavalid Input")

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    p = response.json()
    usdRate = float(p["bpi"]["USD"]["rate"].replace(",", ""))
except requests.RequestException:
    sys.exit()

amount = float(sys.argv[1]) * usdRate
print(f"${amount:,.4f}")
