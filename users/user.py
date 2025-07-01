from typing import Counter
from movie import Movie
from datetime import datetime, timedelta
from utils.file_handler import save_json, load_json
from movies_db import load_movies, save_movies

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
        if not self.watch_list:
            print("📭 Your watchlist is currently empty.")
            return False
        
        for movie in self.watch_list:
            movie.display_movie()
            
        return True

    def view_watched_movies(self):
        if not self.watched_movies:
            print("📭 Your watched movies is currently empty.")
            return False
        
        for movie in self.watched_movies:
            movie.display_movie()
            
        return True



    def remove_from_list(self, movie,list): #return bool
        
        for m in list:
            if m.title.lower() == movie.title.lower():
                list.remove(m)
                return True
        return False
    
    def mark_as_watched(self, movie):  # return bool
        for m in self.watch_list:
            if m.title.lower() == movie.title.lower():
                self.watch_list.remove(m)
                self.watched_movies.append(m)
                return True
        return False
    
    def remove_from_watched_movies(self, movie): #return bool
        for m in self.watched_movies:
            if m.title.lower() == movie.title.lower():
                self.watched_movies.remove(m)
                return True
        return False
    

    def rate_movie(self, movie, rate): #return bool
        if isinstance(movie, Movie) and movie not in self.rated_movies:
            movie.ratings.append(rate)
            self.rated_movies.append(movie)
             # Save updated ratings
            all_movies = load_movies()
            for m in all_movies:
                if m.title.lower() == movie.title.lower():
                    m.ratings = movie.ratings
                    break
            save_movies(all_movies)
            return True
        return False
    

    # not sure yet
    # def get_recommendation(self, movie_list): 
    #     if not self.watched_movies:
    #         return "❗ No watched movies found. Watch some movies to get recommendations."

    #     # Count watched genres
    #     genre_counts = Counter(m.genre.lower() for m in self.watched_movies)
    #     most_common = genre_counts.most_common(1)

    #     if not most_common:
    #         return "❗ No genre preferences found."

    #     top_genre = most_common[0][0]
    #     # Recommend movies of that genre not already watched
    #     recommendations = [m for m in movie_list if m.genre.lower() == top_genre and m not in self.watched_movies]

    #     if recommendations:
    #         return f"🎯 Based on your watched history, we recommend these {top_genre.title()} movies:\n" + \
    #             "\n".join(f"- {m.title}" for m in recommendations)
    #     else:
    #         return f"🎯 You have watched all movies in your favorite genre: {top_genre.title()}!"

    
    def save_watch_list(self):
        users = load_json("users.json")

        for user in users:
            if user["username"] == self.username:
                user["watch_list"] = [m.title for m in self.watch_list]
                
                break

        save_json("users.json", users)

    def is_exist_in_watchlist(self, movie):
        return any(m.title == movie.title for m in self.watch_list)
    
    def load_watch_list(self):
        all_movies = load_movies()  
        users = load_json("users.json")

        for user in users:
            if user["username"] == self.username:
                saved_titles = user.get("watch_list", [])
                self.watch_list = [m for m in all_movies if m.title in saved_titles]
                break


    def save_watched_movies(self):
        users = load_json("users.json")

        for user in users:
            if user["username"] == self.username:
                user["watched_movies"] = [m.title for m in self.watched_movies]
                break
                
                

        save_json("users.json", users)

    def load_watched_movies(self):
        all_movies = load_movies()  
        users = load_json("users.json")

        for user in users:
            if user["username"] == self.username:
                saved_titles = user.get("watched_movies", [])
                self.watched_movies = [m for m in all_movies if m.title in saved_titles]
                break

    def is_exist_in_watched_movies(self, movie):
        return any(m.title == movie.title for m in self.watched_movies)