# MovieMate – A Personalized Movie Planner



#### Overview : MovieMate is a simple command-line application that helps users explore and manage a collection of movies. The system supports two types of users: regular users and admins. Each type has a different functions to do.

Users can browse the available movies, and admins have full control over the movie JSON file — including adding, editing, and deleting movies. 

### Features & User Stories
#### As a user I can do the following :
- View  all movies . 
- Search for a movie, either by name or genre.
- View watchlist.
- Add/remove to/from watchlist.
- Mark a movie from watchlist as watched, or remove the mark.
- Rate a movie.
- Get a movie recommendations based on my watched history.
- Plan a movie night.

#### As Admin I can do the following :
 - Add new movies to the system.
 - Remove movies from the system.
 - View table showing all movies with ratings and info.





#### Usage :
 - type 1 to Register or 2 to login. note: You can not register as Admin for saftey.
 - After successful login, the menu (for the user or admin) will appear.
     #### As a user :
   - type 1 to browse all movies. You can view details and add movies to your watchlist.
   - type 2 to search for movies by title or genre. You can add matching movies to your watchlist.
   - type 3 to view your watchlist. You can:
      - mark a movie as watched
      - remove a movie from the watchlist
      - rate a movie after marking it as watched
    - type 4 to view your watched movies. You can:
       - rate a watched movie     
       - remove the watched mark from a movie
     - type 5 to rate a movie you’ve already watched.

      - type 6 to get movie recommendations based on your watch history.

    - type 7 to plan a movie night.

   - type 0 to logout and return to the main menu.
     ### As an Admin:
     - type 1 to add a new movie. You will be asked to enter title, genre, duration, age classification,   platform, and production date. Input will be validated.
     - type 2 to remove a movie by entering its title.
     - type 3 to view all movies in a formatted table.
     - type 0 to logout and return to the main menu.

