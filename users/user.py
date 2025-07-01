import random
from typing import Counter
from movie import Movie
from datetime import datetime, timedelta
from utils.file_handler import save_json, load_json
from movies_db import load_movies, save_movies
from collections import Counter

class User:

    def __init__(self, username:str, password:str, name:str, role:str = "User"):
        self.username = username
        self.password = password
        self.name = name
        self.role = role
        self.watch_list = []
        self.watched_movies = []
        


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
        
        Movie.display_movies_table(self.watch_list)
            
        return True

    def view_watched_movies(self):
        all_movies = load_movies()
        users = load_json("users.json")
        for user in users:
            if user["username"] == self.username:
                saved_titles = user.get("watched_movies", [])
                self.watched_movies = [m for m in all_movies if m.title in saved_titles]
                break

        if not self.watched_movies:
            print("📭 Your watched movies is currently empty.")
            return False

        Movie.display_movies_table(self.watched_movies)
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
        if isinstance(movie, Movie):
            movie.ratings.append(rate)
            
            
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

    import random

    import random

    def get_recommendation(self):
        all_movies = load_movies()
        watched_titles = {movie.title.lower() for movie in self.watched_movies}

        # No watched movies -> suggest 6 random movies
        if not self.watched_movies:
            print("🎯 You haven’t watched any movies yet. Here are some suggestions:\n")
            suggestions = [m for m in all_movies if m.title.lower() not in watched_titles]
            Movie.display_movies_table(random.sample(suggestions, min(6, len(suggestions))))
            return ""

        # Count watched genres
        genre_counts = Counter(movie.genre.lower() for movie in self.watched_movies)
        if not genre_counts:
            
            suggestions = [m for m in all_movies if m.title.lower() not in watched_titles]
            print("🎯 No genre preference found. Here are some suggestions:\n")
            Movie.display_movies_table(random.sample(suggestions, min(6, len(suggestions))))
            return ""

        # Get all genres with max count
        max_count = max(genre_counts.values())
        top_genres = [genre for genre, count in genre_counts.items() if count == max_count]

        # Recommend movies from those genres (excluding watched)
        recommendations = [
            m for m in all_movies
            if m.genre.lower() in top_genres and m.title.lower() not in watched_titles
        ]

        if recommendations:
            genre_names = ", ".join(g.title() for g in top_genres)
            print(f"🎯 Based on your watched history, we recommend these {genre_names} movies:\n")
            Movie.display_movies_table(recommendations)

        else:
            # If no unwatched from top genres, fall back to random
            suggestions = [m for m in all_movies if m.title.lower() not in watched_titles]
            print("🎯 You've watched all movies in your favorite genres. Here are some random picks:\n")
            Movie.display_movies_table(random.sample(suggestions, min(6, len(suggestions))))

        return ""



    def plan_movie_night(self):
        print("\n🍿 Let's plan your movie night!")

        # Ask for available time
        try:
            time_limit = int(input("⏱️ How many minutes do you have for the movie night?: "))
        except ValueError:
            print("⚠️ Please enter a valid number.")
            return

        # Ask for preferred genre
        genre_pref = input("🎭 What genre are you in the mood for? (or type 'any'): ").lower()

        # Load all movies and filter
        all_movies = load_movies()
        suggestions = []

        for movie in all_movies:
            if movie.duration <= time_limit:
                if genre_pref == 'any' or genre_pref in movie.genre.lower():
                    if not self.is_exist_in_watched_movies(movie):
                        suggestions.append(movie)

        # Show results
        if suggestions:
            print("\n🎬 Here are some movies you can watch tonight:\n")
            Movie.display_movies_table(suggestions[:6])  # Show up to 6 suggestions
        else:
            print("❗ Sorry, no suitable movies found for your movie night.")




    
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