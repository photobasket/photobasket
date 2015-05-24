import sqlite3

conn = sqlite3.connect('photonet.db')
cur = conn.cursor()

cur.execute("INSERT INTO album VALUES ('Urlaub 2015', 'urlaub2015', 'https://soundcloud.com/philipp-demankowski/philipp-demankowski-balearic-sunday-mix')")

cur.execute("INSERT INTO users VALUES ('urlaub2015', 'x83hdz7w6x5dbn4t', 'John.Doe@gmail.com')")
cur.execute("INSERT INTO users VALUES ('urlaub2015', 'lsoe7fh4zf5ndh7e', 'Jane.Doe@gmail.com')")

conn.commit()

cur.close()
