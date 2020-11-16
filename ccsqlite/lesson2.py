import sqlite3

conn = sqlite3.connect("database.db")


# put cursor
c = conn.cursor()

# execute sql directly to database
c.execute("CREATE TABLE IF NOT EXISTS books (title TEXT,pages INTEGER)")
