import os
import requests
from bs4 import BeautifulSoup

print("Welcome to Amazon Price tracker")

normal_price = float(input("Enter the normal price of the product: "))
URL = input("Enter the URL of the product: ")

website = requests.get(URL)

soup = BeautifulSoup(website.text, "lxml")

product_name = soup.find("span", id="productTitle").getText().strip()
last_price = ""
price_whole = soup.find("span", class_="a-price-whole").getText().strip(",")
print(price_whole)
price_fraction = soup.find("span", class_="a-price-fraction").getText()
print(price_fraction)
price_symbol = soup.find("span", class_="a-price-symbol").getText()
print(price_symbol)
full_price = float(f"{price_whole}.{price_fraction}")

if full_price < normal_price:
    print(f"The price of {product_name} has dropped to {full_price}{price_symbol}.")
    print("Buy it now!")
else:
    print(f"The price of {product_name} is still {full_price}{price_symbol}.")
    print("No deals available")

