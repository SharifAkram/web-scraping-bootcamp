import requests as r
from bs4 import BeautifulSoup
from bs4.element import NavigableString

resp = r.get("https://books.toscrape.com/")

resp.content

soup = BeautifulSoup(resp.content, "html.parser")  # lxml

# print(soup.a)
# print(soup.a.get_text())
# print(soup.a.text)
# print(soup.a.string)

# print(soup.ul)
# print(soup.ul.get_text())
# print(soup.ul.text)
# print(soup.ul.string)

# print(soup.a.text, " of type ", type(soup.a.text))
# print(soup.a.get_text(), " of type ", type(soup.a.get_text()))
# print(soup.a.string, " of type ", type(soup.a.string))

print(soup.ul.get_text(separator=", ", strip=True))
