
from users.user import User
from movies_db import save_movies
class Admin (User):
    def __init__(self, username, password, name):
        super().__init__(username, password, name, role = "admin")
    
    def add_movie(self, movie, movie_list):
        movie_list.append(movie)
        save_movies(movie_list)
        print(f"✅ Movie '{movie.title}' added successfully.")

    def remove_movie(self, title, movie_list):
        for movie in movie_list:
            if movie.title == title:
                movie_list.remove(movie)
                save_movies(movie_list)
                print(f"🗑️ Movie '{title}' removed successfully.")
                return
        print(f"❌ Movie '{title}' not found.")

   
