import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

# load environment variables
load_dotenv()

# spotify credentials
scope = 'playlist-modify-public user-read-recently-played'
username = 'qmatix'

# create the spotify object
token = SpotifyOAuth(scope=scope, username=username)
spotifyObject = spotipy.Spotify(auth_manager=token)

# create the playlist
playlist_name = input("What do you want to call your playlist? ")
playlist_description = input("What do you want to be your playlist description? ")

spotifyObject.user_playlist_create(user=username, name=playlist_name, public=True, description=playlist_description)

# get last played tracks
num_tracks_to_visualise = int(input("How many tracks do you want to visualise? "))
last_played_tracks = spotifyObject.current_user_recently_played(limit=num_tracks_to_visualise)
last_played_tracks = [track['track']['name'] for track in last_played_tracks['items']]

for index, track in enumerate(last_played_tracks):
    print(f"{index+1}- {track}")

# choose which tracks to use as a seed to generate a playlist
indexes = input("Enter a list of up to 5 tracks you want to use as seeds for the playlist, separated by space: ")
indexes = indexes.split(" ")
seed_tracks_names = [last_played_tracks[int(index)-1] for index in indexes]

seed_tracks = []
for name in seed_tracks_names:
    result = spotifyObject.search(q=name)
    seed_tracks.append(result['tracks']['items'][0]['uri'])

# get recommended tracks based off seed tracks
recommended_tracks = spotifyObject.recommendations(seed_tracks=seed_tracks, limit=50)['tracks']
print("Here are the recommended tracks which will be included in your new playlist:")
for index, track in enumerate(recommended_tracks):
    print(f"{index+1}- {track['name']}")

recommended_tracks_uris = [track['uri'] for track in recommended_tracks]

# find the new playlist    
prePlaylist = spotifyObject.user_playlists(user=username)
playlist = prePlaylist['items'][0]['id']

# add songs to playlist
spotifyObject.user_playlist_add_tracks(user=username, playlist_id=playlist,tracks=recommended_tracks_uris)

    