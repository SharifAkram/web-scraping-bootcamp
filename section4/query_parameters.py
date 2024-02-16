import requests as r

# url = "https://api.coinbase.com/v2/exchange-rates?currency=BTC"

# resp = r.get(url)

# print(resp.json()["data"]["rates"]["USD"])

# BTC price tracker

url = "https://api.coinbase.com/v2/exchange-rates"

params = {"currency": "BTC"}

resp = r.get(url, params=params)

# print(resp.json()["data"]["rates"]["USD"])

# Sunrise and sunset tracker

url = "https://api.sunrisesunset.io/json"

params = {"lat": 26.122438, "lng": -80.137314, "timezone": "EST", "date": "tomorrow"}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
}
resp = r.get(url, params=params, headers=headers)

# print(resp.status_code)

# print(resp.request.url)

data = resp.json()

for key, value in data["results"].items():
    print(f"{key}: {value}")
