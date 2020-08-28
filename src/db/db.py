import sqlite3

def query(query):
    conn = sqlite3.connect('db.sqlite')
    c = conn.cursor()

    out = list(c.execute(query))

    conn.commit()
    conn.close()
    return out
