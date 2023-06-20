import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

# load the environment variables
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

user_input = input("What songs do you want to add to your playlist? ")
list_of_songs = []

while user_input != 'quit':
    result = spotifyObject.search(q=user_input)
    list_of_songs.append(result['tracks']['items'][0]['uri'])
    user_input = input("What songs do you want to add to your playlist? ")

# find the new playlist    
prePlaylist = spotifyObject.user_playlists(user=username)
playlist = prePlaylist['items'][0]['id']

# add songs to playlist
spotifyObject.user_playlist_add_tracks(user=username, playlist_id=playlist,tracks=list_of_songs)

    