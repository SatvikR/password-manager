import sqlite3

conn = sqlite3.connect('db.sqlite')

c = conn.cursor()

c.execute('CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, username VARCHAR(255), password TEXT)')

c.execute('CREATE TABLE password (id INTEGER PRIMARY KEY AUTOINCREMENT, uid INTEGER, website TEXT, password TEXT)')

conn.commit()
conn.close()