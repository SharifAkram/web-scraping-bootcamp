import requests as r
from bs4 import BeautifulSoup
import re
import pandas as pd

resp = r.get("https://books.toscrape.com/")
soup = BeautifulSoup(resp.content, "lxml")

book_tags = soup.find_all("article", attrs={"class": "product_pod"})


# regex
def clean_price(price):
    return float(re.sub("[^0-9.]", "", price))


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

# average price of all books
# print(sum([book["price"] for book in book_data]) / len(book_data))

# find titles < 20:
# print([book["title"] for book in book_data if book["price"] < 20])

df = pd.DataFrame(book_data)

# print(df)
# print(df.price.mean())
# print(df[df.price < 20])

df.to_csv("books.csv")
# df.to_json("books.csv")
# df.to_excel("books.csv")
# df.to_sql("books.csv")
