# from flask import Flask, request

# app = Flask(__name__)

# @app.route('/')
# def index():
#     with open('index.html') as file:
#         return file.read()

def get_selected_songs(genres):
    # Replace this with your own logic to retrieve songs based on selected genres
    songs = {
        'rock': ['Song 1', 'Song 2', 'Song 3'],
        'pop': ['Song 4', 'Song 5'],
        'jazz': ['Song 6', 'Song 7', 'Song 8'],
        'hip-hop': ['Song 9'],
        'electronic': ['Song 10', 'Song 11'],
        'classical': ['Song 12'],
        'country': ['Song 13', 'Song 14']
    }

    selected_songs = []
    for genre in genres:
        if genre in songs:
            selected_songs.extend(songs[genre])

    return selected_songs