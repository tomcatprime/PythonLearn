import os
import csv
# import lxml

from bs4 import BeautifulSoup

#open website.html and hold content as string
with open('website.html', 'r') as file:
    file_content = file.read()

soup = BeautifulSoup(file_content, "html.parser")

print(soup.title)

print(soup.prettify())

print(soup.li)