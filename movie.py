

class Movie:
    def __init__(self, title, genre, duration, age_classification, where_to_watch, production_date):
        self.title = title
        self.genre = genre
        self.duration = duration
        self.age_classification = age_classification
        self.where_to_watch = where_to_watch
        self.production_date = production_date
        self.ratings = []

    def display_movie(self):
        print("-" * 40)
        print(f"🎞️  Title: {self.title}")
        print(f"📚 Genre: {self.genre}")
        print(f"⏱ Duration: {self.duration} minutes")
        print(f"🔞 Age: {self.age_classification}+")
        print(f"📺 Where to Watch: {self.where_to_watch}")
        print(f"📆 Production Date: {self.production_date}")
        print("-" * 40)

