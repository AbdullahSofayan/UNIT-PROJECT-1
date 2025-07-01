
from tabulate import tabulate
from colorama import Fore, Style
import datetime

class Movie:
    def __init__(self, title, genre, duration, age_classification, where_to_watch, production_date, ratings = None):
        self.title = title
        self.genre = genre
        self.duration = duration
        self.age_classification = age_classification
        self.where_to_watch = where_to_watch
        self.production_date = production_date
        self.ratings = ratings if ratings is not None else []

    @staticmethod
    def display_movies_table(movie_list):
        if not movie_list:
            print("📭 No movies to display.")
            return

        headers = ["#", "Title", "Genre", "Duration", "Age", "Platform", "Release", "Avg Rating", "Votes"]
        table_data = []

        for i, movie in enumerate(movie_list, 1):
            avg_rating = round(sum(movie.ratings) / len(movie.ratings), 1) if movie.ratings else "N/A"
            votes = len(movie.ratings)
            table_data.append([
                i,
                movie.title,
                movie.genre,
                f"{movie.duration} min",
                f"{movie.age_classification}+",
                movie.where_to_watch,
                movie.production_date,
                avg_rating,
                votes
            ])

        # Print table in green, then restore cyan
        print(Fore.LIGHTGREEN_EX + tabulate(table_data, headers=headers, tablefmt="fancy_grid"))
        print(Fore.CYAN + Style.BRIGHT, end="")  # Reset to cyan for following output


    def display_genre(self):
        print(self.genre+"\t")

    def to_dict(self):
        return {
            "title": self.title,
            "genre": self.genre,
            "duration": self.duration,
            "age_classification": self.age_classification,
            "where_to_watch": self.where_to_watch,
            "production_date": self.production_date,
            "ratings": self.ratings
        }

    @staticmethod
    def from_dict(data):
        return Movie(
            data["title"],
            data["genre"],
            data["duration"],
            data["age_classification"],
            data["where_to_watch"],
            data["production_date"],
            data.get("ratings", [])
        )

    @staticmethod
    def is_duplicate_title(title, movie_list):
        return title.strip().lower() in [m.title.lower() for m in movie_list]

    @staticmethod
    def is_valid_genre(genre, movie_list):
        return genre.lower() in {m.genre.lower() for m in movie_list}

    @staticmethod
    def input_duration():
        try:
            duration = int(input("\nEnter duration (minutes): "))
            if duration <= 0:
                raise ValueError
            return duration
        except ValueError:
            print("❌ Duration must be a positive integer.")
            return None

    @staticmethod
    def input_age_classification():
        try:
            age = int(input("\nEnter age classification: "))
            if age < 0:
                raise ValueError
            return age
        except ValueError:
            print("❌ Age classification must be a non-negative integer.")
            return None

    @staticmethod
    def input_production_date():
        date_str = input("\nProduction date (YYYY-MM-DD): ").strip()
        try:
            date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            return str(date)
        except ValueError:
            print("❌ Invalid date format. Please use YYYY-MM-DD.")
            return None

    @staticmethod
    def available_genres(movie_list):
        return sorted(set(m.genre for m in movie_list))