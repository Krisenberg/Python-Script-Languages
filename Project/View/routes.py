from flask import Blueprint, request, render_template, url_for
from model import test
from controller import spotify_controller2

# app = Flask(__name__)

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def home():
    return render_template('home.html', css_path='static\\css\\main_page.css', player='model\\test.py')

@main.route('/about')
def about():
    return render_template('about.html', css_path='static\\css\\main_page.css')

@main.route('/contact')
def contact():
    return render_template('contact.html', css_path='static\\css\\main_page.css')

@main.route('/spotify_playlist', methods=['POST'])
def spotify_playlist():
    return render_template('playlist_creator_menu.html', css_path='static\\css\\main_page.css')

@main.route('/strategy_picker', methods=['POST'])
def strategy_picker():
    strategy_func_dict = {
            'strategy1' : strategy1,
            'strategy2' : None
        }

    # selected_option = strategy_func_dict[request.form.get('options')]
    input = request.form.get('options')
    return render_template(f'{input}.html', css_path='static\\css\\main_page.css')

@main.route('/strategy1', methods=['POST'])
def strategy1():

    start_year = request.form.get('start_year')
    end_year = request.form.get('end_year')
    limit = request.form.get('limit')
    market = request.form.getlist('market')

    playlist = spotify_controller2.create_playlist_from_top_tracks(int(start_year), int(end_year), int(limit), market)
    
    # Return a response or redirect as needed
    return render_template('contact.html', playlist_link=playlist, css_path='static\\css\\main_page.css')

# @main.route('/play', methods=['POST'])
# def play_music():
#     selected_genres = request.form.getlist('genre')

#     # Perform some logic to get the selected songs
#     selected_songs = test.get_selected_songs(selected_genres)

#     return render_template('result.html', songs=selected_songs)
