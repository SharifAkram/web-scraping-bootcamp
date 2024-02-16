# Authentication and Authorization

import requests as r

"""
API_KEY = "YOUR_API_KEY"

url = "https://api.exchange.coinbase.com/fills"

headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

r.get(url, headers=headers)
"""

# basic auth -> username, password

auth = ("user1", "pass2")

url = "https://www.httpbin.org/basic-auth/user1/pass2"

print(r.get(url, auth=auth))
