import requests

url = "https://quotes.toscrape.com/"

# resp = requests.get(url)

# resp = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}) # get around bot detection

# print(type(resp))

# print(resp.headers["Content-Type"])

resp = requests.get("https://httpbin.org/headers")

# print(resp.json())

print(dict(resp.request.headers))
