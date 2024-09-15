import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv

# If the .env file is outside of the repo, specify the path.
# dotenv_path = "/home/youruser/secure-config/.env"

# Load the .env file from the specified location
# load_dotenv(dotenv_path)

# Currently using default location.
load_dotenv()

client_id = os.getenv('client_id')
client_secret = os.getenv('client_secret')

auth_manager = SpotifyClientCredentials(client_id=client_id,client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

drake_uri = 'spotify:artist:3TVXtAsR1Inumwj472S9r4'
results = sp.artist_top_tracks(drake_uri)
for track in results['tracks'][:10]:
    print('track    : ' + track['name'])
    # print('audio    : ' + track['preview_url'])
    print('cover art: ' + track['album']['images'][0]['url'])
    print()