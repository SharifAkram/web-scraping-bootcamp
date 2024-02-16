from urllib.request import urlopen

url = "https://quotes.toscrape.com/"

resp = urlopen(url)

print(resp.status)

content = resp.read()

# print(content)

print(content.decode("utf-8"))

# with open("quotes.txt", "w", encoding="utf-8") as file:
# file.write(content.decode("utf-8"))

# with open("quotes.txt", "r", encoding="utf-8") as file:
# quotes_content = file.read()

# print(quotes_content)
