from colorama import Fore, Style
from art import tprint
from movie import Movie
from movies_db import load_movies
from users.user import User
from auth import register_user, login_user
def welcome_screen():
    tprint("MovieMate")
    print(Fore.CYAN + Style.BRIGHT + "-" * 40)
    print(Fore.YELLOW + "🎥 Welcome to your personalized movie planner!")
    print(Fore.CYAN + "-" * 40)

def main_menu():
    while True:
        print("\n=== MovieMate ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            user = register_user()
            if user:
                print(f"Welcome, {user['name']}! Registration successful.")
        elif choice == "2":
            user = login_user()
            if user:
                print(f"Welcome back, {user['name']}! Logged in as {user['role']}.")
                if user['role'] == 'user':
                    customer_menu(User(user['username'], user['password'], user['name']))
                break
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

def display_movies(movies):
    print("\n🎬 Available Movies:")
    print("-" * 40)
    for movie in movies:
        print(f"🎞️  Title: {movie.title}")
        print(f"📚 Genre: {movie.genre}")
        print(f"⏱ Duration: {movie.duration} minutes")
        print(f"🔞 Age: {movie.age_classification}+")
        print(f"📺 Where to Watch: {movie.where_to_watch}")
        print(f"📆 Production Date: {movie.production_date}")
        print("-" * 40)

def customer_menu(user):
    movies = load_movies()
    while True:
        
        print("\n--- Customer Menu ---")
        print("1. Browse all movies") # ask if he want to add to watchlist *
        print("2. Search for movie") # and search by genre , ask if he want to add to watchlist

        # print("2. Search by genre")
        # print("3. Show movie details")

        print("3. View watchlist") #and ask him if he want to mark some movie, or remove it from watchlist, when movie is marked ask the user about rating

        # print("4. Add to watchlist")
        # print("5. Remove from watchlist")
        # print("7. Mark as watched")
        print("4. Rate a movie")
        print("5. Get movie recommendations")
        print("6. Plan a movie night")
        print("0. Logout")
        
        choice = input("Choose an option: ")

        match choice:
            case '1':
                display_movies(movies)
                chice = input("Do you want to add a movie to your watchlist ? (y / n): ")
                if chice == 'y':
                    title = input("Write the title of the movie: ")
                    movie = user.find_movie_by_title(title)
                    if movie:
                        user.add_to_watchlist(movie)
                    else:
                        print("movie title is wrong")
                input("\nPress Enter to back to menu..")
            case '2':
                pass
            case '3':
                print()
                user.view_watchlist()

            case '0':
                print("Logging out...")
                break
            case _:
                print("Invalid choice")

        










welcome_screen()
main_menu()

# m1 = Movie('interstiller', 'action',165,18,'netflix','2020')
# c1 = Customer('aa','123','abood',15)
# print(c1.add_to_watchlist(m1))
# c2 = Customer('bb','123','ahmed',15)

# print(c1.rate_movie(m1,9))
# print(c2.rate_movie(m1,10))

# print(c1.watch_list)
