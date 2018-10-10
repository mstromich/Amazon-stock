import datetime
import requests
import json
from time import sleep

#Total amounts of Crypto Currency owned
ownedstock = 27

#API calls
def amazonstock():
    url = 'https://api.iextrading.com/1.0/stock/AMZN/price'
    try:
        r = requests.get(url)
        price_float = float(json.loads(r.text))
        return price_float
    except requests.ConnectionError:
        print("Error querying Bitstamp API")

while True:
    print(datetime.datetime.now())
    print("Amazon stock is currently valued at: USD " + str(round(amazonstock(),2)))
    print("Your current stock of " + str(ownedstock) + " is worth USD " + str(round(amazonstock()*ownedstock,2)))
    print("")
    sleep(10)