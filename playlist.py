import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Initialize Spotify client
def initialize_spotify_client():
    client_id = os.getenv('client_id')
    client_secret = os.getenv('client_secret')
    
    if not client_id or not client_secret:
        raise Exception("Missing client_id or client_secret in environment variables.")
    
    auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    return spotipy.Spotify(auth_manager=auth_manager)

# Search for artist by name
def search_artist(sp, artist_name):
    results = sp.search(q=artist_name, type='artist')
    
    if not results['artists']['items']:
        raise Exception(f"Artist '{artist_name}' not found.")
    
    return results['artists']['items'][0]['id']

# Fetch top tracks for the artist
def get_top_tracks(sp, artist_id):
    try:
        return sp.artist_top_tracks(artist_id)
    except Exception as e:
        raise Exception("Error fetching top tracks:", e)

# Process and display track data
def process_track_data(track):
    track_name = track.get('name', 'Unknown Track')
    album_name = track.get('album', {}).get('name', 'Unknown Album')
    release_date = track.get('album', {}).get('release_date', 'Unknown Date')
    
    print(f"Song Name: {track_name}\nAlbum: {album_name}\nRelease Date: {release_date}\n")

# Main function to tie everything together
def main(artist_name='Drake'):
    try:
        sp = initialize_spotify_client()
        artist_id = search_artist(sp, artist_name)
        tracks = get_top_tracks(sp, artist_id)
        
        print(f"Top 10 tracks for {artist_name}:\n")
        for track in tracks['tracks'][:10]:
            process_track_data(track)
    
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    # You can pass a different artist name here
    main('drake')
