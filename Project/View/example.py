from flask import Blueprint, request, render_template
from model import test

# app = Flask(__name__)

example_blueprint = Blueprint('example_blueprint', __name__)

@example_blueprint.route('/')
def index():
    return render_template('index.html', css_path='static\\css\\main_page.css', player='model\\test.py')

@example_blueprint.route('/play', methods=['POST'])
def play_music():
    selected_genres = request.form.getlist('genre')

    # Perform some logic to get the selected songs
    selected_songs = test.get_selected_songs(selected_genres)

    return render_template('result.html', songs=selected_songs)
