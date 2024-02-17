import requests as r
from bs4 import BeautifulSoup
import re

# import pprint

resp = r.get("https://books.toscrape.com/")
soup = BeautifulSoup(resp.content, "lxml")

# print(len(soup.find_all()))

book_tags = soup.find_all("article", attrs={"class": "product_pod"})
# print(len(book_tags))
# print(book_tags[0])


# def extract_book_data(book_tag):
# title = book_tag.find("h3").find("a")["title"]
# price = book_tag.find("p", attrs={"class": "price_color"}).get_text()
# rating = book_tag.find("p", attrs={"class": "star-rating"})["class"][
# -1
# ]  # first from the end

# return title, price, rating


# print(book_tags[0].prettify())
# b = extract_book_data(book_tags[6])


# def clean_price(price):
# return float("".join([char for char in price if char.isdigit() or char == "."]))


# print(clean_price(b[1]))


# regex
def clean_price(price):
    return float(re.sub("[^0-9.]", "", price))


# print(clean_price(b[1]))


def map_rating(rating):
    rating_map = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5,
    }

    return rating_map[rating]


def extract_book_data(book_tag):
    title = book_tag.find("h3").find("a")["title"]
    price = book_tag.find("p", attrs={"class": "price_color"}).get_text()
    rating = book_tag.find("p", attrs={"class": "star-rating"})["class"][-1]

    return {"title": title, "price": clean_price(price), "rating": map_rating(rating)}


book_tags = soup.find_all("article", attrs={"class": "product_pod"})

book_data = [extract_book_data(book_tag) for book_tag in book_tags]

print(book_data)
