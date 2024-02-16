import requests as r
from bs4 import BeautifulSoup
from bs4.element import NavigableString

resp = r.get("https://books.toscrape.com/")

resp.content

soup = BeautifulSoup(resp.content, "html.parser")  # lxml

# soup.ul
# soup.ul.li

# print(soup.ul.li.next_sibling.next_sibling)

print(soup.ul.li.next_sibling.next_sibling.previous_sibling.previous_sibling)
