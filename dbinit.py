import sqlite3

conn = sqlite3.connect('photonet.db')
cur = conn.cursor()

cur.execute('''CREATE TABLE album (
                  name TEXT,
                  url TEXT,
                  soundcloud_url TEXT
            )''')

cur.execute('''CREATE TABLE users (
                  album_url TEXT,
                  key TEXT,
                  email TEXT
            )''')

cur.execute('''CREATE TABLE images (
                  path TEXT,
                  size TEST,
                  album_url TEXT,
                  users_key TEXT
            )''')

cur.close()
