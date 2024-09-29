#his module is called repository

import sqlite3  # This runs when I import the .py  but it does not remember the variable in the app.py
connection = sqlite3.connect("data.db")
connection.row_factory = sqlite3.Row # To get dictionary when I create a cursor


# connections
def create_table():
    with connection:
        connection.execute(
            "CREATE TABLE IF NOT EXISTS entries (content TEXT, date TEXT);"
        )
    # or skip with and do connection.commit() here


def close_connection():
    connection.close()


# Functions to add a new entry or view existing entries

def add_entry(entry_content, entry_date):
    with connection:
        connection.execute(
            "INSERT INTO entries VALUES (?, ?);", (entry_content, entry_date)
        )

        # with connection:
        #     connection.execute(
        #         f"INSERT INTO entries VALUES ('{entry_content}', '{entry_date}');"
        #     )



def get_entries():

    cursor = connection.execute("SELECT * FROM entries;")
    # print(type(cursor.fetchone()))
    # print(cursor.fetchone())
    # print(type(cursor.fetchall()))
    # print(cursor.fetchall())
    # print(type(cursor))
    # print(cursor)
    # for row in cursor:
    #     print(type(row))
    #     print(row)
    return cursor

    # return connection.execute("SELECT * FROM entries;")

    # cursor = connection.cursor()
    # cursor.execute("SELECT * FROM entries;")
    # return cursor








# connection = sqlite3.connect("data.db")
# cursor = connection.cursor()
# cursor.execute(“SELECT * FROM users;”)
#
# for row in cursor:
#     print(row)
# connection.close()




# connection = sqlite3.connect("data.db")
# cursor = connection.cursor()
# cursor.execute(“INSERT INTO users ('John Smith', 35);”)
#
# connection.close()




# connection = sqlite3.connect("data.db")
# connection.execute(“INSERT INTO users ('John Smith', 35);”)
# connection.close()
