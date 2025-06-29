from colorama import Fore, Style
from art import tprint
from movie import Movie
from users.Customer import Customer
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
                break  # This can be replaced with role-specific menu in future
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

welcome_screen()
main_menu()

# m1 = Movie('interstiller', 'action',165,18,'netflix','2020')
# c1 = Customer('aa','123','abood',15)
# print(c1.add_to_watchlist(m1))
# c2 = Customer('bb','123','ahmed',15)

# print(c1.rate_movie(m1,9))
# print(c2.rate_movie(m1,10))

# print(c1.watch_list)
