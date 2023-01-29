import sqlite3

with sqlite3.connect("mydb.db") as connection:
    cursore = connection.cursor()
    with open("BooksAndAuthors.sql", "r") as sql:
        req = sql.read()
        cursore.executescript(req)
