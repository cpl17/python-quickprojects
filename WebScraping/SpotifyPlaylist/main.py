from datetime import datetime as dt
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint

SPOTID ="8524ce42464e40c48eb0d6bc681496eb"
SPOTSCRT = "459d94c5f6604eed8b67f97dfcb21be1"
REDIRECT_URI = "http://example.com"

BBURL = "https://www.billboard.com/charts/hot-100/"



# TODO -> change prompt after incorrect date entry

def get_date():
    dformat = "%Y-%m-%d"
    date_string = input("What year would you like to travel? Enter in YYYY-MM-DD: ")
    try: 
        date = dt.strptime(date_string,dformat)
    except ValueError:
        print("This is an incorrect value for data. Please type YYYY-MM-DD")
        get_date()
    return dt.strftime(date,dformat)
    

date = get_date()

# Get Top 100 

url = BBURL + date

print(url)

response = requests.get(url)
mov_page = response.text
soup = BeautifulSoup(mov_page, "html.parser")

top100 = [song.text for song in soup.find_all(name="span",class_="chart-element__information__song text--truncate color--primary")]



# Authentication 

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTID,
        client_secret= SPOTSCRT,
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]


# Create list of uri's 


top100_uris = []
year = date.split("-")[0]

for track in top100:

    result = sp.search(q = f"track:{track}  year:{year}", type='track', limit = 1)

    try:
        
        top100_uris.append(result['tracks']['items'][0]['uri'])

    except IndexError:

        print(f"{track} doesn't exist in Spotify. Skipped.")


# Create Playlist 

playlist = sp.user_playlist_create(user_id, name = f"Top Tracks from {date}", public = False)

sp.user_playlist_add_tracks(user = user_id, playlist_id = playlist['id'], tracks = top100_uris)


        
        





























