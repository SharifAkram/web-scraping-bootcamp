# find()
# find_all()

import requests as r
from bs4 import BeautifulSoup
import pprint


resp = r.get("https://books.toscrape.com/")

soup = BeautifulSoup(resp.content, "html.parser")  # lxml

# print(soup.find_all())
# print(len(soup.find_all()))
# pprint.pprint(soup.find_all("a"))
# print(len(soup.find_all("a")))
# print(len(soup.find_all(["a", "p"])))

# tag_name: p
# attr: class=price_color

# price_tags = soup.find_all("p", attrs={"class": "price_color"})
# price_tags = soup.find_all("p", class_="price_color")
# pprint.pprint([price.get_text() for price in price_tags])

# add_buttons = soup.find_all("button", attrs={"data-loading-text": "Adding..."})
# print(len(add_buttons))

add_buttons = soup.find_all(
    "button",
    attrs={"data-loading-text": lambda x: "add" in x.lower() or "remove" in x.lower()},
)
print(len(add_buttons))
