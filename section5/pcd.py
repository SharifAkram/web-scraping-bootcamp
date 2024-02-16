# Parents, Children, and Descendants

import requests as r
from bs4 import BeautifulSoup
from bs4.element import NavigableString

resp = r.get("https://books.toscrape.com/")

resp.content

soup = BeautifulSoup(resp.content, "html.parser")  # lxml

# print(soup.ul)
# print(soup.ul.prettify())
# print(list(soup.ul.children))

# print(list(filter(lambda x: type(x) != NavigableString, soup.ul.children)))


def no_nav_strings(iterable):
    return list(filter(lambda x: type(x) != NavigableString, iterable))


# print(no_nav_strings(soup.ul.children))

# print(list(soup.ul.descendants))

desc = no_nav_strings(soup.ul.descendants)
# desc[0]
print(desc[0].parent)
