import requests as r
from bs4 import BeautifulSoup

resp = r.get("https://books.toscrape.com/")

resp.content

soup = BeautifulSoup(resp.content, "html.parser")  # lxml

# print(soup.title)

print(soup.prettify())

# print(soup.name)
