import requests as r
from bs4 import BeautifulSoup

resp = r.get("https://books.toscrape.com/")

soup = BeautifulSoup(resp.content, "html.parser")  # lxml

# print(soup.title)

# print(soup.prettify())

# print(soup.name)

# print(soup.title)
# print(soup.h1)
# print(soup.div)

first_div = soup.div

# print(type(first_div))

# print(first_div.div.div.attrs)

first_div.attrs["class"].append("some-other-class")  # mutate soup object

print(first_div)
print(soup.div)
