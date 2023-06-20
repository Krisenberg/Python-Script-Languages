import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

# load environment variables
load_dotenv()

# spotify credentials
scope = 'playlist-modify-public'
username = 'qmatix'

# create the spotify object
token = SpotifyOAuth(scope=scope, username=username)
spotifyObject = spotipy.Spotify(auth_manager=token)

# create the playlist
playlist_name = input("What do you want to call your playlist? ")
playlist_description = input("What do you want to be your playlist description? ")

spotifyObject.user_playlist_create(user=username, name=playlist_name, public=True, description=playlist_description)

# get the years
print("From which years you want to make your playlist?")
start = input("Enter the start year: ")
stop = input("Enter the stop year: ")

# add the tracks
track_uris = []
for year in range(int(start), int(stop)):
    results = spotifyObject.search(q=f'year:{year}', type='track', limit=10)
    track_uris += [track['uri'] for track in results['tracks']['items']]
    
# find the new playlist    
prePlaylist = spotifyObject.user_playlists(user=username)
playlist = prePlaylist['items'][0]['id']

# add songs to playlist
spotifyObject.user_playlist_add_tracks(user=username, playlist_id=playlist,tracks=track_uris)