import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os

load_dotenv()
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
token = spotipy.prompt_for_user_token(client_id, client_secret)
# sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp = spotipy.Spotify(auth=token)


def get_top_data(year, type, limit, market):
    # Use the Spotify Charts endpoint to get the top tracks for the year
    chart_data = sp.search(q='year:' + str(year), type=type, limit=limit, market=market)
    return chart_data

def create_playlist_from_top_tracks(year_start, year_end, limit, market):
    tracks = []
    for year in range(year_start, year_end+1):
        tracks.append(get_top_data(year, 'track', limit, market))

    tracks_uris = []
    for track_list in tracks:
        if 'items' in track_list:
            for track in track_list['items']:
                if 'uri' in track:
                    tracks_uris.append(track['uri'])
    playlist = sp.user_playlist_create(user=sp.current_user()['id'], name=f'Top Tracks Playlist({year_start, year_end})', public=True)

    sp.playlist_add_items(playlist_id=playlist['id'], items=tracks_uris)
    playlist_link = playlist['external_urls']['spotify']

    return playlist_link

# # Example usage
# for year in range(2021, 2022):
#     print('Top tracks of', year)
#     get_top_tracks(year)
#     print()