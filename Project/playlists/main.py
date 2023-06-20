from playlistFactory import PlaylistFactoryManager

if __name__ == "__main__":
    scope = 'playlist-modify-public user-read-recently-played'
    username = 'qmatix'
    playlist_name = 'test'
    playlist_description = 'test'
    
    playlist_generator = PlaylistFactoryManager.create_playlist_generator(scope, username)
    playlist_generator.create_playlist(playlist_name, playlist_description)
    playlist_generator.add_tracks(playlist_generator.get_tracks())