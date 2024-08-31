from bs4 import BeautifulSoup
import requests

website = requests.get("https://news.ycombinator.com/news")

yc_web_page = website.text

soup = BeautifulSoup(yc_web_page, "html.parser")
article_texts = []
article_links = []

articles =soup.find_all(name="a", class_="storylink")
for article_tag in articles:
    article_text = article_tag.getText()
    article_texts.append(article_text)
    article_link = article_tag.get("href")
    article_links.append(article_link)  


article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]


largest_number = max(article_upvotes)

article_upvotes.index(largest_number)

article_text[largest_number]
article_link[largest_number]
