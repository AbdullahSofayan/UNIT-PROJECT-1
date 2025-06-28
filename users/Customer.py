from users.user import User
from movie import Movie
class Customer(User):


    def __init__(self, username, password, name,age):
        super().__init__(username, password, name,age, role = "costumer")
        self.watch_list = []
        self.watched_movies = []
        self.rated_movies = [] #To prevent rating the same movie more than one


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


    
