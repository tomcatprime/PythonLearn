import os
import requests
from bs4 import BeautifulSoup

print("Welcome to Amazon Price tracker")

URL = "https://www.amazon.pl/Panasonic-eneloop-akumulatory-opakowaniu-sztucznych/dp/B09ZL9SSD5/ref=sr_1_9?_encoding=UTF8&content-id=amzn1.sym.1efa4f16-e6ed-4dba-96c6-2f14cba2ad54&dib=eyJ2IjoiMSJ9.GtKThdFv8U7fLvQwAQSZtwAHY3GFBf4T9uqAO9X7AWW7n0H9zIqBTosyQ5-rS_3733FGUF0Wpd5Tx26czokk3H-PM1xxpZkFYMuKt3SVEVtxyWVqDuAP5ivCsrJUfgY1u-ZKOfuX3LyZrHUdMMoqL2LBjREj42TLPB1L_-uZBg54sUUre993H_uDtMxXWVn7iIC7uMHSUyKxNiqPX1PCCJyGkwHZLr-r8VP9FaYzIsYjL2NblYPyjKuVBTOqmhe1ZZ9EyjxHfb06WhWgQSXpm2Ot-KNcPFuglIpWJ0xxZAY.pdLcmdQgLwlbEXwFhEdAi2yBLTAd2zOa_APoU67JMq4&dib_tag=se&pd_rd_r=e939c0cc-92db-44e3-b354-6e83771fe9e7&pd_rd_w=QvUdt&pd_rd_wg=yfjwf&pf_rd_p=1efa4f16-e6ed-4dba-96c6-2f14cba2ad54&pf_rd_r=DCVG9YP82EWPB04PZF5Q&qid=1725523400&s=electronics&sr=1-9"

website = requests.get(URL)

soup = BeautifulSoup(website.text, "lxml")

product_name = soup.find("span", id="productTitle")

print(product_name)