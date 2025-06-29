from typing import Counter
from movie import Movie
from datetime import datetime, timedelta

from movies_db import load_movies

class User:

    def __init__(self, username:str, password:str, name:str, role:str = "User"):
        self.username = username
        self.password = password
        self.name = name
        self.role = role
        self.watch_list = []
        self.watched_movies = []
        self.rated_movies = [] #To prevent rating the same movie more than one
        self.current_plan = None


    def find_movie_by_title(self, title):
        movies = load_movies()
        for movie in movies:
            if title.lower() == movie.title.lower():
                return movie

    def add_to_watchlist(self, movie):
        if isinstance(movie, Movie):
            self.watch_list.append(movie)
            

    def view_watchlist(self):
        print("-" * 40)
        for movie in self.watch_list:
            print(f"🎞️  Title: {movie.title}")
            print(f"📚 Genre: {movie.genre}")
            print(f"⏱ Duration: {movie.duration} minutes")
            print(f"🔞 Age: {movie.age_classification}+")
            print(f"📺 Where to Watch: {movie.where_to_watch}")
            print(f"📆 Production Date: {movie.production_date}")
            print("-" * 40)




    def remove_from_watchlist(self, movie): #return bool
        if movie in self.watchlist:
            self.watch_list.remove(movie)
            return True
        
        return False
    
    def  mark_as_watched(self, movie): #return bool
        if movie in self.watch_list:
            self.watch_list.remove(movie)
            self.watched_movies.append(movie)
            return True
        
        return False
    
    

    def rate_movie(self, movie, rate): #return bool
        if isinstance(movie, Movie) and movie not in self.rated_movies:
            movie.ratings.append(rate)
            self.rated_movies.append(movie)
            return True
        return False
    
    def get_recommendation(self, movie_list):
        if not self.watched_movies:
            return "❗ No watched movies found. Watch some movies to get recommendations."

        # Count watched genres
        genre_counts = Counter(m.genre.lower() for m in self.watched_movies)
        most_common = genre_counts.most_common(1)

        if not most_common:
            return "❗ No genre preferences found."

        top_genre = most_common[0][0]
        # Recommend movies of that genre not already watched
        recommendations = [m for m in movie_list if m.genre.lower() == top_genre and m not in self.watched_movies]

        if recommendations:
            return f"🎯 Based on your watched history, we recommend these {top_genre.title()} movies:\n" + \
                "\n".join(f"- {m.title}" for m in recommendations)
        else:
            return f"🎯 You have watched all movies in your favorite genre: {top_genre.title()}!"

    


    