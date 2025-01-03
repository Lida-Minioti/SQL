import os
import psycopg2
from dotenv import load_dotenv
import datetime

load_dotenv()

# Create db connection
connection = psycopg2.connect(os.environ["DATABASE_URL"])

CREATE_MOVIES_TABLE = """ CREATE TABLE IF NOT EXISTS movies (
    id SERIAL PRIMARY KEY,
    title TEXT, 
    release_timestamp REAL
);"""

CREATE_USERS_TABLE = """ CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY
);"""

CREATE_WATCHED_TABLE = """ CREATE TABLE IF NOT EXISTS watched (
    user_username TEXT,
    movie_id INTEGER,
    FOREIGN KEY(user_username) REFERENCES users(username),
    FOREIGN KEY(movie_id) REFERENCES movies(id)
    
);"""

# CREATE_RELEASE_INDEX = "CREATE INDEX IF NOT EXISTS idx_movies_release ON movies(release_timestamp);"

INSERT_MOVIES = """ INSERT INTO movies (title, release_timestamp) VALUES (%s,%s);"""
INSERT_USER = """INSERT INTO users (username) VALUES (%s)"""
DELETE_MOVIE = "DELETE FROM movies WHERE title =%s;"

SELECT_ALL_MOVIES = """SELECT * FROM movies;"""
SELECT_UPCOMING_MOVIES = """SELECT * FROM movies WHERE release_timestamp>%s;"""
SELECT_WATCHED_MOVIES = """SELECT movies.* 
FROM movies 
JOIN watched on movies.id = watched.movie_id
JOIN users on  users.username = watched.user_username
WHERE users.username=%s;"""

INSERT_WATCHED_MOVIE = """INSERT INTO watched (user_username, movie_id) VALUES (%s,%s);"""

# SET_MOVIE_WATCHED = "UPDATE movies SET watched = 1 WHERE title = %s;"
SEARCH_MOVIES = "SELECT * FROM movies WHERE title LIKE %s;"


def create_tables():
    with connection:
        #cursor = connection.cursor()
        with connection.cursor() as cursor:
            cursor.execute(CREATE_MOVIES_TABLE)
            cursor.execute(CREATE_USERS_TABLE)
            cursor.execute(CREATE_WATCHED_TABLE)
            #cursor.execute(CREATE_RELEASE_INDEX)


def add_user(username):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(INSERT_USER, (username,))


def add_movies(title, release_timestamp):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(
                INSERT_MOVIES, (title, release_timestamp)  # remember you pass in a tuple
            )


# This function will be used to get all the movies when it is false or the upcoming ones when upcoming=True
def get_movies(upcoming=False):
    with connection:
        with connection.cursor() as cursor:
            if upcoming:
                today_timestamp = datetime.datetime.today().timestamp()
                cursor.execute(SELECT_UPCOMING_MOVIES, (today_timestamp,))
            else:
                cursor.execute(SELECT_ALL_MOVIES)
            return cursor.fetchall()


def search_movies(search_term):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SEARCH_MOVIES, (f"%{search_term}%",))
            return cursor.fetchall()


# marks the movie as watched
def watch_movie(username, movie_id):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(INSERT_WATCHED_MOVIE, (username, movie_id,))


def get_watched_movies(username):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_WATCHED_MOVIES, (username,))
            return cursor.fetchall()
