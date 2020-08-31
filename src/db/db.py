import sqlite3

def query(query, params=[]):
    conn = sqlite3.connect('db.sqlite')
    c = conn.cursor()

    out = list(c.execute(query, params))

    conn.commit()
    conn.close()
    return out
