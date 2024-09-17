import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv

# If the .env file is outside of the repo, specify the path.
# dotenv_path = "/home/youruser/secure-config/.env"

# Load the .env file from the specified location
# load_dotenv(dotenv_path)

# Currently using default location.
load_dotenv(override=True)

client_id = os.getenv('client_id')
client_secret = os.getenv('client_secret')

auth_manager = SpotifyClientCredentials(client_id=client_id,client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)
artist = input(f"Enter artist: ")

# Search for Drake by artist name
results = sp.search(q={artist}, type='artist')

# Get Drake's artist ID
artist_id = results['artists']['items'][0]['id']

# Print the names of Artist's top tracks
tracks = sp.artist_top_tracks(artist_id)


# print(tracks)

def process_data(track):
    print(f"Song Name:", track)

for track in tracks['tracks'][:10]:
  process_data(track['name'])
   
