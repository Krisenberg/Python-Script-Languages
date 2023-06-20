import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import abc

class PlaylistGenerator(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self, scope, username):
        load_dotenv()
        self.username = username
        self.token = SpotifyOAuth(scope=scope, username=username)
        self.spotifyObject = spotipy.Spotify(auth_manager=self.token)
    
    @abc.abstractmethod
    def create_playlist(self, playlist_name, playlist_description):
        self.spotifyObject.user_playlist_create(user=self.username, name=playlist_name, public=True, description=playlist_description)

    @abc.abstractmethod
    def get_tracks(self):
        pass

    @abc.abstractmethod
    def add_tracks(self, track_uris):
        prePlaylist = self.spotifyObject.user_playlists(user=self.username)
        playlist = prePlaylist['items'][0]['id']
        self.spotifyObject.user_playlist_add_tracks(user=self.username, playlist_id=playlist,tracks=track_uris)
        
    @abc.abstractmethod
    def get_link(self):
        prePlaylist = self.spotifyObject.user_playlists(user=self.username)
        playlist = prePlaylist['items'][0]['id']
        return f"https://open.spotify.com/playlist/{playlist}"
        
class PlaylistGenres(PlaylistGenerator):
    def __init__(self, scope, username):
        super().__init__(scope, username)
    
    def create_playlist(self, playlist_name, playlist_description):
        super().create_playlist(playlist_name, playlist_description)
        
    def get_tracks(self, genre, limit):
        # # get the genres
        # genres = self.spotifyObject.recommendation_genre_seeds()['genres']
        # print("What genres you want to include in your playlist?")
        # for i, genre in enumerate(genres):
        #     print(f"{i+1}. {genre}", end='\n')
        
        seed_genres = [genre]

        # get recommended tracks based off seed tracks
        recommended_tracks = self.spotifyObject.recommendations(seed_genres=seed_genres, limit=50)['tracks']

        recommended_tracks_uris = [track['uri'] for track in recommended_tracks]
        return recommended_tracks_uris
    
    def get_link(self):
        return super().get_link()
        
    def add_tracks(self, track_uris):
        super().add_tracks(track_uris)
        
class PlaylistYears(PlaylistGenerator):
    def __init__(self, scope, username):
        super().__init__(scope, username)
    
    def create_playlist(self, playlist_name, playlist_description):
        super().create_playlist(playlist_name, playlist_description)
        
    def get_tracks(self, start, stop, limit):
        # add the tracks
        track_uris = []
        for year in range(int(start), int(stop)):
            results = self.spotifyObject.search(q=f'year:{year}', type='track', limit=int(limit))
            track_uris += [track['uri'] for track in results['tracks']['items']]
        return track_uris
    
    def get_link(self):
        return super().get_link()
        
    def add_tracks(self, track_uris):
        super().add_tracks(track_uris)
        
class PlaylistRecommendations(PlaylistGenerator):
    def __init__(self, scope, username):
        super().__init__(scope, username)
    
    def create_playlist(self, playlist_name, playlist_description):
        super().create_playlist(playlist_name, playlist_description)
        
    def get_tracks(self):
        # get last played tracks
        num_tracks_to_visualise = int(input("How many tracks do you want to visualise? "))
        last_played_tracks = self.spotifyObject.current_user_recently_played(limit=num_tracks_to_visualise)
        last_played_tracks = [track['track']['name'] for track in last_played_tracks['items']]

        for index, track in enumerate(last_played_tracks):
            print(f"{index+1}- {track}")

        # choose which tracks to use as a seed to generate a playlist
        indexes = input("Enter a list of up to 5 tracks you want to use as seeds for the playlist, separated by space: ")
        indexes = indexes.split(" ")
        seed_tracks_names = [last_played_tracks[int(index)-1] for index in indexes]

        seed_tracks = []
        for name in seed_tracks_names:
            result = self.spotifyObject.search(q=name)
            seed_tracks.append(result['tracks']['items'][0]['uri'])

        # get recommended tracks based off seed tracks
        recommended_tracks = self.spotifyObject.recommendations(seed_tracks=seed_tracks, limit=50)['tracks']
        print("Here are the recommended tracks which will be included in your new playlist:")
        for index, track in enumerate(recommended_tracks):
            print(f"{index+1}- {track['name']}")

        recommended_tracks_uris = [track['uri'] for track in recommended_tracks]
        return recommended_tracks_uris
        
    def get_link(self):
        return super().get_link()
        
    def add_tracks(self, track_uris):
        super().add_tracks(track_uris)
        
        
class PlaylistAdded(PlaylistGenerator):
    def __init__(self, scope, username):
        super().__init__(scope, username)
    
    def create_playlist(self, playlist_name, playlist_description):
        super().create_playlist(playlist_name, playlist_description)
        
    def get_tracks(self):
        user_input = input("What songs do you want to add to your playlist? ")
        list_of_songs = []

        while user_input != 'quit':
            result = self.spotifyObject.search(q=user_input)
            list_of_songs.append(result['tracks']['items'][0]['uri'])
            user_input = input("What songs do you want to add to your playlist? ")
            
        return list_of_songs

    def get_link(self):
        return super().get_link()

    def add_tracks(self, track_uris):
        super().add_tracks(track_uris)