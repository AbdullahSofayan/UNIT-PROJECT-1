from utils.file_handler import load_json, save_json
from movie import Movie

MOVIE_FILE = "movies.json"

def load_movies():
    movie_dicts = load_json(MOVIE_FILE)
    return [Movie(**movie) for movie in movie_dicts]

def save_movies(movies):
    save_json(MOVIE_FILE, [m.__dict__ for m in movies])