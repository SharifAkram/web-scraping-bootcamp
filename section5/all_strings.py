import requests as r
from bs4 import BeautifulSoup


resp = r.get("https://books.toscrape.com/")

soup = BeautifulSoup(resp.content, "html.parser")  # lxml

# print(soup.stripped_strings)
all_strings = list(soup.stripped_strings)
print(len(all_strings))
print(len(list(soup.strings)))
print(list(soup.strings)[:10])
