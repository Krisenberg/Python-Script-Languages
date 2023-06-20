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

# get the genres
genres = spotifyObject.recommendation_genre_seeds()['genres']
print("What genres you want to include in your playlist?")
for i, genre in enumerate(genres):
    print(f"{i+1}. {genre}", end='\n')
    
# choose the genres
indexes = input("Enter a list up to 5 genres you want to include in your playlist, separated by space: ")
indexes = indexes.split(" ")
seed_genres = [genres[int(index)-1] for index in indexes]

# get recommended tracks based off seed tracks
recommended_tracks = spotifyObject.recommendations(seed_genres=seed_genres, limit=50)['tracks']
print("Here are the recommended tracks which will be included in your new playlist:")
for index, track in enumerate(recommended_tracks):
    print(f"{index+1}- {track['name']}")

recommended_tracks_uris = [track['uri'] for track in recommended_tracks]

# find the new playlist    
prePlaylist = spotifyObject.user_playlists(user=username)
playlist = prePlaylist['items'][0]['id']

# add songs to playlist
spotifyObject.user_playlist_add_tracks(user=username, playlist_id=playlist,tracks=recommended_tracks_uris)