import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import *
import os
import pprint

load_dotenv()

YOUR_APP_CLIENT_ID = os.getenv("YOUR_APP_CLIENT_ID")
YOUR_APP_CLIENT_SECRET = os.getenv("YOUR_APP_CLIENT_SECRET")
YOUR_APP_REDIRECT_URI = os.getenv("YOUR_APP_REDIRECT_URI")

print("Welcome to the Spotify Playlist Generator")
user_date = input("Enter the date you want to travel to in the format YYYY-MM-DD: ")

print("Thank you. Processing your request...")
URL = f"https://www.billboard.com/charts/hot-100/{user_date}/"

website = requests.get(URL)

# Scraping the website

soup = BeautifulSoup(website.text, "lxml")

# Extracting the song names and artist names

song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

artist_all = soup.find_all("span", class_="a-no-trucate")
artist_name = [artist.getText().strip() for artist in artist_all]

playlist = [f"{song_names} by {artist_name}" for song_names, artist_name in zip(song_names, artist_name)]

playlist_tracks = playlist
#Spotify Authentication

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=YOUR_APP_CLIENT_ID,
                                               client_secret=YOUR_APP_CLIENT_SECRET,
                                               redirect_uri=YOUR_APP_REDIRECT_URI,
                                               scope="playlist-modify-private"))

USER_ID = sp.current_user()["id"] # type: ignore

#Searching Spotify for songs by title
#Adding the song URIs to a new playlist
playlist = sp.user_playlist_create(user=USER_ID, name=f"Billboard Hot 100 from {user_date}.", public=False)
PLAYLIST_ID = playlist["id"]
print(f"Playlist has been created. {PLAYLIST_ID} /nAdding songs to the playlist...")
SONG_URI = []
for song in playlist_tracks:
    print(song)
    song_search = sp.search(q=song, type="track", market="PL", limit=1)
    # print("Found")
    song_uri = song_search["tracks"]["items"][0]["uri"] # type: ignore
    # print(song_uri)
    # print("Adding to playlist...")
    SONG_URI.append(song_uri)
    print("Done")

sp.playlist_add_items(playlist_id=PLAYLIST_ID, items=SONG_URI)

print("Playlist created successfully!")
