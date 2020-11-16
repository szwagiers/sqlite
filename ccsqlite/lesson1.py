import sqlite3

# connect to database. Save db fale in memory
conn = sqlite3.connect(":memory:")

# or on harddrive
# name_of_db.db


# put cursor
c = conn.cursor()
