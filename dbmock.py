import sqlite3

conn = sqlite3.connect('photonet.db')
cur = conn.cursor()

cur.execute("INSERT INTO album VALUES ('Urlaub 2015', 'urlaub2015')")

cur.execute("INSERT INTO users VALUES ('urlaub2015', 'x83hdz7w6x5dbn4t', 'John.Doe@gmail.com')")
cur.execute("INSERT INTO users VALUES ('urlaub2015', 'lsoe7fh4zf5ndh7e', 'Jane.Doe@gmail.com')")

cur.execute("INSERT INTO images VALUES ('images/urlaub2015/1234.jpeg', 'urlaub2015', 'x83hdz7w6x5dbn4t')")
cur.execute("INSERT INTO images VALUES ('images/urlaub2015/2345.jpeg', 'urlaub2015', 'x83hdz7w6x5dbn4t')")
cur.execute("INSERT INTO images VALUES ('images/urlaub2015/3456.jpeg', 'urlaub2015', 'notexistinguser')")
cur.execute("INSERT INTO images VALUES ('images/urlaub2015/4567.jpeg', 'urlaub2015', 'lsoe7fh4zf5ndh7e')")

conn.commit()

cur.close()
