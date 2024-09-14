import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = '50416c5c4af24a108fc2b5d32b5941bd'
client_secret = '4280fe7a0db94c1cb75402f5f763a488'

auth_manager = SpotifyClientCredentials(client_id=client_id,client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

drake_uri = 'spotify:artist:3TVXtAsR1Inumwj472S9r4'
results = sp.artist_top_tracks(drake_uri)
for track in results['tracks'][:10]:
    print('track    : ' + track['name'])
    # print('audio    : ' + track['preview_url'])
    print('cover art: ' + track['album']['images'][0]['url'])
    print()