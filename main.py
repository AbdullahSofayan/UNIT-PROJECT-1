from colorama import Fore, Style
from art import tprint
from users.Admin import Admin
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
                    user_menu(User(user['username'], user['password'], user['name']))
                elif user['role'] == 'admin':
                    admin_menu(Admin(user['username'], user['password'], user['name']))
                break
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")




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
                while True:
                    # ask about rating
                    rate = input(f"⭐ Do you want to rate '{movie.title}'? (yes / no): ").lower()

                    if rate == 'yes':
                        try:
                            rate_movie(user,movie)
                            break
                        except Exception as e:
                            print(e)
                            continue
                        


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
            raise Exception("⚠️ Rating must be between 1 and 10.")
        

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
        



def user_menu(user):
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
                # movie.display_movie()
                Movie.display_movies_table(movies)
                to_watchlist(user)
                print()
            case '2':
                print("\n1-Search by name\n2- Search by genre\n3- To back to menu\n")
                sub_choice  = input("Choose an option: ")
                while True:
                    if sub_choice  == '1':
                        search = input("🔍 Enter a movie title to search, or type back: ").lower()
                        if search == 'back':
                            pass
                        else:
                            # Filter matching movies
                            matched_movies = [movie for movie in movies if search in movie.title.lower()]
                            
                            if matched_movies:
                                Movie.display_movies_table(matched_movies)
                                ask_watchlist(user, search)
                            else:
                                print("❌ No movies found matching your search.")

                    elif sub_choice  == '2':
                        print("🎭 Available genres:")
                        all_genres = sorted(set(movie.genre for movie in movies))
                        for genre in all_genres:
                            print(f"- {genre}")

                        search = input("\n🔍 Enter a movie genre to search, or type back: ").lower()
                        if search == 'back':
                            pass
                        else:
                            matched_movies = [movie for movie in movies if search in movie.genre.lower()]
                            
                            if matched_movies:
                                Movie.display_movies_table(matched_movies)
                                to_watchlist(user)
                            else:
                                print("❌ No movies found in that genre.")


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
                            while True:
                                title = input("\n⭐ Type the movie title to rate, or type back: ")
                                if title == 'back':
                                    break
                                movie = user.find_movie_by_title(title)
                                if movie:
                                    if not user.is_exist_in_watched_movies(movie):
                                        print(f"❗ {movie.title} is not marked as watched.")
                                    else:
                                        try:
                                            rate_movie(user,movie)
                                        except Exception as e:
                                            print(e)
                                            continue
                                        # Reload updated movies and watched list
                                        movies = load_movies()
                                        user.load_watched_movies()
                                        user.view_watched_movies()
                                        break
                                else:
                                    print("❌ No movies found matching your search.")
                        elif option == '2':
                            delete_movie(user, user.watched_movies)
                            user.view_watched_movies()
                        elif option == '3':
                            break
                        else:
                            print("Invalid choice")

            case '5':
                while True:
                    title = input("\n⭐️ Type the movie title to rate, or type back: ")
                    if title == 'back':
                        break
                    movie = user.find_movie_by_title(title)
                    if movie:
                        if not user.is_exist_in_watched_movies(movie):
                            print(f"❗️ {movie.title} is not marked as watched.")
                        else:
                            try:
                                rate_movie(user,movie)
                            except Exception as e:
                                print(e)
                                continue
                            # Reload updated movies and watched list
                            movies = load_movies()
                            user.load_watched_movies()
                            user.view_watched_movies()
                            break
                    else:
                        print("❌ No movies found matching your search.")

            case '6':
                msg = user.get_recommendation()
                if msg:
                    print(msg)

            case '7':
                user.plan_movie_night()

            case '0':
                print("Logging out...")
                break
            case _:
                print("Invalid choice")

        





def admin_menu(admin: Admin):
    movies = load_movies()
    
    while True:
        print("\n🎬 Admin Menu:")
        print("1. Add Movie")
        print("2. Remove Movie")
        print("3. View All Movies")
        print("0. Logout")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
                while True:
                    title = input("\nEnter movie title: ").strip()
                    if Movie.is_duplicate_title(title, movies):
                        print("❌ A movie with that title already exists.")
                        continue
                    break
                        
                genres = Movie.available_genres(movies)
                while True:
                    print(f"\nAvailable genres: {', '.join(genres)}")
                    genre = input("Enter genre: ").strip().lower()
                    if not Movie.is_valid_genre(genre, movies):
                        print("❌ Invalid genre. Please choose from existing genres.")
                        continue

                    # Get the genre from the movie list with original casing
                    genre = next((m.genre for m in movies if m.genre.lower() == genre), genre)
                    break
                while True:
                    duration = Movie.input_duration()
                    if duration is None:
                        continue
                    break

                while True:
                    age_classification = Movie.input_age_classification()
                    if age_classification is None:
                        continue
                    break

                print()
                where_to_watch = input("Where to watch: ").strip()

                while True:
                    production_date = Movie.input_production_date()
                    if production_date is None:
                        continue
                    break

                new_movie = Movie(
                    title, genre, duration, age_classification,
                    where_to_watch, production_date
                )
                admin.add_movie(new_movie, movies)
                
            
        elif choice == "2":
            title = input("Enter the title of the movie to remove: ")
            admin.remove_movie(title, movies)

        elif choice == "3":
            if not movies:
                print("📭 No movies available.")
            else:
                Movie.display_movies_table(movies)

        elif choice == "0":
            print("Logging out...")
            break
        else:
            print("❌ Invalid choice. Try again.")





welcome_screen()
main_menu()


