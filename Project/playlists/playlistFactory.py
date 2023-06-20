import abc
from playlistGenerator import PlaylistGenres, PlaylistYears, PlaylistRecommendations, PlaylistAdded

class PlaylistFactory(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create_playlist_generator(self, scope, username):
        pass
    
class PlayistFactoryGenres(PlaylistFactory):
    def create_playlist_generator(self, scope, username):
        return PlaylistGenres(scope, username)
    
class PlaylistFactoryYears(PlaylistFactory):
    def create_playlist_generator(self, scope, username):
        return PlaylistYears(scope, username)
    
class PlaylistFactoryRecommendations(PlaylistFactory):
    def create_playlist_generator(self, scope, username):
        return PlaylistRecommendations(scope, username)
    
class PlaylistFactoryAdded(PlaylistFactory):
    def create_playlist_generator(self, scope, username):
        return PlaylistAdded(scope, username)
    
class PlaylistFactoryManager:
    @staticmethod
    def create_playlist_generator(scope, username):
        creator = PlaylistFactoryManager.get_creator()
        return creator.create_playlist_generator(scope, username)
    
    @staticmethod
    def get_creator():
        type = input("What type of playlist do you want to create? ")
        creator_dict = PlaylistFactoryManager.get_creator_dict()
        for key, value in creator_dict.items():
            if key == type:
                return value
        return PlaylistFactoryAdded()
    
    @staticmethod
    def get_creator_dict():
        types = ['genres', 'years', 'recommendations', 'added']
        creators = [PlayistFactoryGenres(), PlaylistFactoryYears(), PlaylistFactoryRecommendations(), PlaylistFactoryAdded()]
        return dict(zip(types, creators))
