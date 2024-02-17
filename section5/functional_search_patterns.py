import requests as r
from bs4 import BeautifulSoup
import re

resp = r.get("https://books.toscrape.com/")
soup = BeautifulSoup(resp.content, "lxml")

# print(soup.find_all(id="messages"))
# print(soup.find_all(attrs={"id": "messages"}))

print(len(soup.find_all(attrs={"id": lambda x: x is not None})))
print(len(soup.find_all(id=lambda x: x is not None)))
print(soup.find_all(lambda x: x is not None))
