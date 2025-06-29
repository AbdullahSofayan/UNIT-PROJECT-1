from typing import Counter
from users.user import User
from movie import Movie
from datetime import datetime, timedelta
class Customer(User):


    def __init__(self, username, password, name):
        super().__init__(username, password, name, role = "costumer")
        self.watch_list = []
        self.watched_movies = []
        self.rated_movies = [] #To prevent rating the same movie more than one
        self.current_plan = None


    def add_to_watchlist(self, movie):
        if isinstance(movie, Movie):
            self.watch_list.append(movie)
            

    def remove_from_watchlist(self, movie): #return bool
        if movie in self.watchList:
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
    
    # def plan_night(self, movie, start_time_str):
    #     if self.current_plan:
    #         now = datetime.now()
    #         if now < self.current_plan["end_time"]:
    #             return f"❌ You already have a movie planned: {self.current_plan['movie'].title} ending at {self.current_plan['end_time'].strftime('%H:%M')}"

    #     try:
    #         start_time = datetime.strptime(start_time_str, "%H:%M")
    #     except ValueError:
    #         return "❌ Invalid time format. Use HH:MM."

    #     end_time = start_time + timedelta(minutes=movie._duration)
    #     self.current_plan = {"movie": movie, "start_time": start_time, "end_time": end_time}

    #     return (f"✅ Movie planned successfully!\n"
    #             f"🎬 Movie: {movie.title}\n"
    #             f"🕗 Starts at: {start_time.strftime('%H:%M')}\n"
    #             f"🕙 Ends at: {end_time.strftime('%H:%M')}\n"
    #             f"🍿 Snack Suggestion: Popcorn")
    
    # def search(self, movie_list, title):
    #     return [m for m in movie_list if title.lower() in m.title.lower()]

    # def search_by_genre(self, movie_list, genre):
    #     return [m for m in movie_list if genre.lower() in m.genre.lower()]

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
    
