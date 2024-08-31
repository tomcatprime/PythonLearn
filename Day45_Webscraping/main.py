import os
import csv
# import lxml

from bs4 import BeautifulSoup

#open website.html and hold content as string
with open('./website.html', 'r') as file:
    file_content = file.read()

soup = BeautifulSoup(file_content, "html.parser")

print(soup.title)

print(soup.prettify())

print(soup.li)
print(soup.p)

all_anchor_tag = soup.find_all(name="a")


for tag in all_anchor_tag:
    print(tag.getText())
    print(tag.get("href"))


heading = soup.find(name="h1", id="name")
print(heading)

seaction_heading = soup.find(name="h3", class_="heading")
print(seaction_heading)

company_url = soup.select_one(selector="p a")
print(company_url)

heading = soup.select(".heading")
print(heading)
