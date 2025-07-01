from colorama import Fore, Style
from art import tprint
from movie import Movie
from movies_db import load_movies
from users.user import User
from auth import register_user, login_user
from movies_db import save_movies 

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
            title = input("Write the title of the movie, or type back : ").lower()
            while title != "back":
                movie = user.find_movie_by_title(title)
                if movie:
                    if user.is_exist_in_watchlist(movie):
                        print(f"❗ {movie.title} is already in your watchlist.")
                    else:
                        user.add_to_watchlist(movie)
                        print(f"✅ {movie.title} added to your watchlist.")
                else:
                    print("❌ Movie title is wrong.")
                

                title = input("Write the title of the movie, or type back : ").lower()
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
            else:
                user.add_to_watchlist(movie)
                print(f"✅ {movie.title} added to your watchlist.")
        else:
            print("❌ Movie title is wrong.")
         
    elif chice == 'no':
        pass
    else:
        print("invalid choice")
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
                
                # ask about rating
                rate = input(f"⭐ Do you want to rate '{movie.title}'? (yes / no): ").lower()

                if rate == 'yes':
                    rate_movie(user,movie)



                break
                
        else:
            print("❌ Movie title is wrong.")

def rate_movie(user, movie):
    try:
        score = int(input("Enter your rating (1-10): "))
        if 1 <= score <= 10:
            if user.rate_movie(movie, score):
                print("✅ Your rating has been recorded.")
            else:
                print("❌ You have already rated this movie.")
        else:
            print("⚠️ Rating must be between 1 and 10.")
        

    except ValueError:
        print("⚠️ Invalid input. Please enter a number.")
def delete_movie(user, list):
    while True:
        
        title = input("Enter the title of the movie to remove from list, or type back: ").lower()
        if title == 'back':
            break
        movie = user.find_movie_by_title(title)

        if movie:
            if user.remove_from_list(movie,list):
                print(f"✅ {movie.title} removed.")
                if list is user.watch_list:
                    user.save_watch_list()
                elif list is user.watched_movies:
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
        print("4. view watched movies") # ask if he wants to remove the mark
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
                            movies = load_movies() # Reload movies to reflect updated rating
                            user.view_watchlist()
                        elif option == '2':
                            delete_movie(user, user.watch_list)
                            user.view_watchlist()
                        elif option == '3':
                            break
                        else:
                            print("invalid choice")

            case '4':
                if user.view_watched_movies():
                    while True:
                        option = input("\n1- Rate a movie\t2- Remove the mark as watched from a movie\t3- back to menu\nchoose of the above: ")
                        if option == '1':
                            title = input("⭐ Type the movie title to rate, or type back: ")
                            if title == 'back':
                                continue
                            movie = user.find_movie_by_title(title)
                            if movie:
                                if not user.is_exist_in_watched_movies(movie):
                                    print(f"❗ {movie.title} is not marked as watched.")
                                else:
                                    rate_movie(user,movie)
                                    # Reload updated movies and watched list
                                    movies = load_movies()
                                    user.load_watched_movies()
                                    user.view_watched_movies()
                                    continue
                            else:
                                print("❌ No movies found matching your search.")
                        elif option == '2':
                            delete_movie(user, user.watched_movies)
                            user.view_watched_movies()
                        elif option == '3':
                            break
                        else:
                            print("Invalid choice")



                    


            case '0':
                print("Logging out...")
                break
            case _:
                print("Invalid choice")

        










welcome_screen()
main_menu()


