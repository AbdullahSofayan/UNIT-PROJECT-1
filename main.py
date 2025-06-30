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


def to_watchlist(user):
    
    while True:
        choice  = input("Do you want to add a movie to your watchlist ? (yes / no): ")
        if choice  == 'yes':
            title = input("Write the title of the movie, or type stop : ").lower()
            while title != "stop":
                movie = user.find_movie_by_title(title)
                if movie:
                    if user.is_exist_in_watchlist(movie):
                        print(f"❗ {movie.title} is already in your watchlist.")
                    elif user.is_exist_in_watched_movies(movie):
                        print(f"❗ {movie.title} is already marked as watched.")
                    else:
                        user.add_to_watchlist(movie)
                        print(f"✅ {movie.title} added to your watchlist.")
                else:
                    print("❌ Movie title is wrong.")
                

                title = input("Write the title of the movie, or type stop : ").lower()
            user.save_watch_list()
            break
        elif choice  == 'no':
            break
        else:
            print("invalid choice")
                

def ask_watchlist(user, title):
    chice = input("Do you want to add it into your watchlist ? (yes / no): ")
  
    if chice == 'yes':
        movie = user.find_movie_by_title(title)
        if movie:
            if user.is_exist_in_watchlist(movie):
                print(f"❗ {movie.title} is already in your watchlist.")
            elif user.is_exist_in_watched_movies(movie):
                print(f"❗ {movie.title} is already marked as watched.")
            else:
                user.add_to_watchlist(movie)
                print(f"✅ {movie.title} added to your watchlist.")
        else:
            print("❌ Movie title is wrong.")
         
    elif chice == 'no':
        pass
    user.save_watch_list()

def mark_movie(user):
    while True:
        
        title = input("Enter the title of the movie to mark as watched, or type back: ").lower()
        if title == 'back':
            break
        movie = user.find_movie_by_title(title)

        if movie:
            if user.is_exist_in_watched_movies(movie):
                print(f"❗ {movie.title} is already marked as watched.")
            elif not user.is_exist_in_watchlist(movie):
                print(f"❌ {movie.title} is not in your watchlist.")
            
            elif user.mark_as_watched(movie):
                print(f"✅ {movie.title} marked as watched.")
                user.save_watch_list()
                user.save_watched_movies()
                break
                
        else:
            print("❌ Movie title is wrong.")

def delete_movie(user):
    while True:
        
        title = input("Enter the title of the movie to remove from watchlist, or type back: ").lower()
        if title == 'back':
            break
        movie = user.find_movie_by_title(title)

        if movie:
            if user.remove_from_watchlist(movie):
                print(f"✅ {movie.title} removed.")
                user.save_watch_list()
                user.save_watched_movies()
                break
            else:
                print(f"❌ {movie.title} is not in your watchlist.")            
                
        else:
            print("❌ Movie title is wrong.")
        



def customer_menu(user):
    user.load_watch_list()
    movies = load_movies()
    user.load_watched_movies()
    while True:
        
        print("\n--- User Menu ---")
        print("1. Browse all movies") # ask if he want to add to watchlist *
        print("2. Search for movie") # and search by genre , ask if he want to add to watchlist *
        print("3. View watchlist") #and ask him if he want to mark some movie, or remove it from watchlist * , when movie is marked ask the user about rating
        print("4.view watched movies") # ask if he wants to remove the mark
        print("5. Rate a movie")
        print("6. Get movie recommendations")
        print("7. Plan a movie night")
        print("0. Logout")
        
        choice = input("Choose an option: ")

        match choice:
            case '1':
                display_movies(movies)
                to_watchlist(user)
                input("\nPress Enter to back to menu..")
            case '2':
                print("\n1-Search by name\n2- Search by genre\n3- To back to menu\n")
                sub_choice  = input("Choose an option: ")
                while True:
                    if sub_choice  == '1':
                        search = input("🔍 Enter a movie title to search, or type back: ").lower()
                        if search == 'back':
                            pass
                        else:
                            found = False

                            for movie in movies : 
                                if search in movie.title.lower():
                                    movie.display_movie()
                                    found = True
                            if not found:
                                print("❌ No movies found matching your search.")

                            ask_watchlist(user,search)
                    elif sub_choice  == '2':
                        search = input("🔍 Enter a movie genre to search, or type back: ").lower()
                        if search == 'back':
                            pass
                        else:
                            found = False
                            for movie in movies : 
                                if search in movie.genre.lower():
                                    movie.display_movie()
                                    found = True
                            if not found:
                                print("❌ No movies found matching your search.")
                        to_watchlist(user)
                    elif sub_choice  == '3':
                        break
                    else:
                        print("invalid choice")


                    print("\n1-Search by name\n2- Search by genre\n3- To back to menu\n")
                    sub_choice  = input("Choose an option: ")
                


            case '3':
                print()
                if user.view_watchlist():
                    while True:
                        option = input("\n1- Mark a movie as watched\t2- Remove a movie from watchlist\t3- back to menu\nchoose of the above: ")
                        if option == '1':
                            mark_movie(user)
                            user.view_watchlist()
                        elif option == '2':
                            delete_movie(user)
                            user.view_watchlist()
                        elif option == '3':
                            break
                        else:
                            print("invalid choice")

                    
                    

                    


            case '0':
                print("Logging out...")
                break
            case _:
                print("Invalid choice")

        










welcome_screen()
main_menu()


