import datetime
import database

menu = """Please select one of the following options:
1) Add new movie.
2) View upcoming movies.
3) View all movies
4) Watch a movie
5) View watched movies.
6) Add user
7) Search for a movie
8) Exit.

Your selection: """
welcome = "Welcome to the watchlist app!"

print(welcome)
database.create_tables()


# Functions that interact with user

def prompt_add_movie():
    title = input("Movie title: ")
    release_date = input("Release_date in dd-mm-yyyy format: ")
    parsed_date = datetime.datetime.strptime(release_date, "%d-%m-%Y")  # create dataetime object
    timestamp = parsed_date.timestamp()  # create timestamp

    database.add_movies(title, timestamp)


def print_movie_list(heading, movies):
    print(f"-- {heading}--")
    for _id, title, released_date in movies:
        movie_date_object = datetime.datetime.fromtimestamp(released_date)  # create datetime object
        string_date = movie_date_object.strftime("%b-%d-%Y")  # create string

        print(f"{_id}: {title}, released on {string_date}")  # note this returns a timestamp
    print("--- \n")


# def print_watched_movie_list(username, movies):
#     print(f"--{username} watched the below movies--")
#     for movie in movies:
#         print(f"{movie[1]}")
#     print("--- \n")


def prompt_watch_movie():
    username = input("Who watched the movie?")
    movie_id = input("Enter movie id of movie you have already watched: ")
    database.watch_movie(username, movie_id)


def prompt_add_user():
    username = input("Who is the new user?")
    database.add_user(username)


def prompt_show_watched_movies():
    username = input('Whose watched list you want?')  # This could be a function
    movies = database.get_watched_movies(username)
    if movies:
        print_movie_list(f"{username} watched the below movies", movies)
    else:
        print(f"User {username} has not watched any movies yet")


def prompt_search_movies():
    search_term = input("Enter the partial movie title: ")
    movies = database.search_movies(search_term)
    if movies:
        print_movie_list("matching movies:", movies)
    else:
        print("No movies found")

while (user_input := input(menu)) != "8":
    if user_input == "1":
        prompt_add_movie()
    elif user_input == "2":
        movies = database.get_movies(True)
        print_movie_list("upcoming", movies)
    elif user_input == "3":
        movies = database.get_movies(False)
        print_movie_list("all movies", movies)
    elif user_input == "4":
        prompt_watch_movie()
    elif user_input == "5":
        prompt_show_watched_movies()
    elif user_input == "6":
        prompt_add_user()
    elif user_input == "7":
        prompt_search_movies()
    else:
        print("Invalid input, please try again!")
