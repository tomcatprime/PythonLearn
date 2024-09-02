import requests
from bs4 import BeautifulSoup

print("Welcome to the Spotify Playlist Generator")
user_date = input("Enter the date you want to travel to in the format YYYY-MM-DD: ")

print("Thank you. Processing your request...")
URL = f"https://www.billboard.com/charts/hot-100/{user_date}/"

website = requests.get(URL)

soup = BeautifulSoup(website.text, "lxml")
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
print("Here are the top 100 songs from that date: ")
print(song_names)