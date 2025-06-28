from colorama import Fore, Style
from art import tprint
from movie import Movie
from users.Customer import Customer

def welcome_screen():
    tprint("MovieMate")
    print(Fore.CYAN + Style.BRIGHT + "-" * 40)
    print(Fore.YELLOW + "🎥 Welcome to your personalized movie planner!")
    print(Fore.CYAN + "-" * 40)

welcome_screen()

m1 = Movie('interstiller', 'action',165,18,'netflix','2020')
c1 = Customer('aa','123','abood',15)
print(c1.add_to_watchlist(m1))
c2 = Customer('bb','123','ahmed',15)

print(c1.rate_movie(m1,9))
print(c2.rate_movie(m1,10))

# print(c1.watch_list)
