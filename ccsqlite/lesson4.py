import sqlite3

conn = sqlite3.connect("database.db")


# put cursor
c = conn.cursor()

# execute sql directly to database
c.execute("CREATE TABLE IF NOT EXISTS books (title TEXT,pages INTEGER)")

# c.execute('INSERT INTO books VALUES("The Count of  Monte Cristo",1316)')

# conn.commit()

# c.execute('SELECT * FROM books')

# table = c.fetchone()
# print(table)

# list of tuples

books = [
    ("Metro 2033", 400),
    ('Metro 2034', 400),
    ('Metro 2035', 400)
]


c.executemany('INSERT INTO books VALUES(?,?)', books)
conn.commit()
c.execute('SELECT * FROM books')

data = c.fetchall()
print(data)
