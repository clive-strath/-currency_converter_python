import requests

API_KEY = "fca_live_Oip33UnkuiQ7qOEHCf212dadHhcwnHQuFH4ztfV6"
BASE_URL = "https://api.freecurrencyapi.com/v1/latest?apikey=" + API_KEY

CURRENCIES = ["USD", "EUR", "GBP", "JPY", "AUD", "CAD", "CHF", "CNY", "HKD", "NZD"]

def convert_currency(base):
    currencies = ",".join(CURRENCIES)
    url=f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    
    try:
        response = requests.get(url)
        data = response.json()
        return data["data"]
    except Exception as e:
        print("Error occurred:", e)
        return None

while True:

    base=input("Enter the base currency (q to quit): ").upper()
    if base == "Q":
        exit()
    if base not in CURRENCIES:
        print("Invalid base currency")
        continue

    data = convert_currency(base)
    del data[base]
    for ticker,value in data.items():
        print(f"{ticker}: {value}")
