from flask import Blueprint, request, render_template, url_for
from playlists import playlistFactory

scope = 'playlist-modify-public user-read-recently-played'
username = 'qmatix'

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
    # strategy_func_dict = {
    #         'strategy1' : strategy1,
    #         'strategy2' : None
    #     }

    # selected_option = strategy_func_dict[request.form.get('options')]
    input = request.form.get('options')
    return render_template(f'{input}.html', css_path='static\\css\\main_page.css')

@main.route('/strategy1', methods=['GET','POST'])
def strategy1():

    start_year = request.form.get('start_year')
    end_year = request.form.get('end_year')
    limit = request.form.get('limit')
    market = request.form.getlist('market')
    playlist_name = request.form.get('playlist_name')
    playlist_description = request.form.get('playlist_description')

    if not start_year or not end_year or not limit or not market:
        error_message = 'Please provide required data.'
        return render_template('strategy1.html', start_year=start_year, end_year=end_year,
                           limit=limit, market=market, error_message=error_message, css_path='static\\css\\main_page.css')

    if int(start_year) > int(end_year):
        error_message = 'Start year cannot be larger than end year.'
        return render_template('strategy1.html', start_year=start_year, end_year=end_year,
                           limit=limit, market=market, error_message=error_message, css_path='static\\css\\main_page.css')
    
    if int(limit)<=0:
        error_message = 'Limit must be a positive integer.'
        return render_template('strategy1.html', start_year=start_year, end_year=end_year,
                           limit=limit, market=market, error_message=error_message, css_path='static\\css\\main_page.css')

    #playlist = spotify_controller2.create_playlist_from_top_tracks(int(start_year), int(end_year), int(limit), market)

    playlist_generator = playlistFactory.PlaylistFactoryManager.create_playlist_generator(scope, username, type='years')
    playlist_generator.create_playlist(playlist_name, playlist_description)
    playlist_generator.add_tracks(playlist_generator.get_tracks(start_year, end_year, limit))
    
    return render_template(f'strategy1.html', playlist=str(playlist_generator.get_link()), start_year=start_year, end_year=end_year,
                           limit=limit, market=market, css_path='static\\css\\main_page.css')
    
    # Return a response or redirect as needed
    # return render_template('contact.html', playlist_link=playlist, css_path='static\\css\\main_page.css')

@main.route('/strategy2', methods=['GET','POST'])
def strategy2():

    genre = request.form.get('genre')
    limit = request.form.get('limit')
    market = request.form.getlist('market')
    playlist_name = request.form.get('playlist_name')
    playlist_description = request.form.get('playlist_description')

    #playlist = spotify_controller2.create_playlist_from_top_tracks(int(start_year), int(end_year), int(limit), market)

    playlist_generator = playlistFactory.PlaylistFactoryManager.create_playlist_generator(scope, username, type='genres')
    playlist_generator.create_playlist(playlist_name, playlist_description)
    playlist_generator.add_tracks(playlist_generator.get_tracks(genre, limit))
    
    return render_template(f'strategy2.html', playlist=str(playlist_generator.get_link()), genre=genre, 
                           limit=limit, market=market, css_path='static\\css\\main_page.css')
    

# @main.route('/play', methods=['POST'])
# def play_music():
#     selected_genres = request.form.getlist('genre')

#     # Perform some logic to get the selected songs
#     selected_songs = test.get_selected_songs(selected_genres)

#     return render_template('result.html', songs=selected_songs)

