from flask import Blueprint, request, render_template
from Model import test

# app = Flask(__name__)

example_blueprint = Blueprint('example_blueprint', __name__)

@example_blueprint.route('/')
def index():
    return render_template('layout.html', css_path='Styling\\main_page.css', player='Model\\test.py')

@example_blueprint.route('/play', methods=['POST'])
def play_music():
    selected_genres = request.form.getlist('genre')

    # Perform some logic to get the selected songs
    selected_songs = test.get_selected_songs(selected_genres)

    return render_template('result.html', songs=selected_songs)
