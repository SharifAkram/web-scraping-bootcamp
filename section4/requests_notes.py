import requests

url = "https://quotes.toscrape.com/"

resp = requests.get(url)

print(resp)

print(resp.status_code)

# print(resp.content.decode("utf-8"))

# print(resp.text)

print(resp.headers)
