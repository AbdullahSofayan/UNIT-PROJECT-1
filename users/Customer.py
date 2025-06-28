from users.user import User

class Customer(User):


    def __init__(self, username, password, name,age):
        super().__init__(username, password, name,age, role = "costumer")
        self.watchList = []
        self.watchedMovies = []

    def add_to_watchlist(self, movie):
        self.watchList.append(movie)