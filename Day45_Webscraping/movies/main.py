import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇


website = requests.get(URL)
text_web = website.text

soup = BeautifulSoup(text_web, "html.parser")


articles =soup.find_all(name="h3", class_="title")




for title in articles:
    file = open("./Day45_Webscraping/file.txt", "a")
    article_no = title.getText()
    file.write(f"{article_no}\n") 
    file.close()
print("Done")


# list comprehension
movie_titles = [ movie.getText() for movie in articles]

movies = movie_titles[::-1]

with open("./Day45_Webscraping/movies/movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")

print("Done")
