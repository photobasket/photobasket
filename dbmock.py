import sqlite3

conn = sqlite3.connect('photonet.db')
cur = conn.cursor()

cur.execute("INSERT INTO album VALUES ('Urlaub 2015', 'urlaub2015', 'https://soundcloud.com/philipp-demankowski/philipp-demankowski-balearic-sunday-mix')")

cur.execute("INSERT INTO users VALUES ('urlaub2015', 'x83hdz7w6x5dbn4t', 'John.Doe@gmail.com')")
cur.execute("INSERT INTO users VALUES ('urlaub2015', 'lsoe7fh4zf5ndh7e', 'Jane.Doe@gmail.com')")

cur.execute("INSERT INTO images VALUES ('static/example_images/cat.jpg', 'urlaub2015', 'x83hdz7w6x5dbn4t')")
cur.execute("INSERT INTO images VALUES ('static/example_images/beach.jpg', 'urlaub2015', 'x83hdz7w6x5dbn4t')")
cur.execute("INSERT INTO images VALUES ('static/example_images/hiking-family.jpg', 'urlaub2015', 'x83hdz7w6x5dbn4t')")
cur.execute("INSERT INTO images VALUES ('static/example_images/wedding.jpg', 'urlaub2015', 'x83hdz7w6x5dbn4t')")
cur.execute("INSERT INTO images VALUES ('static/example_images/dog.jpg', 'urlaub2015', 'x83hdz7w6x5dbn4t')")
cur.execute("INSERT INTO images VALUES ('static/example_images/happy-family.jpg', 'urlaub2015', 'notexistinguser')")
cur.execute("INSERT INTO images VALUES ('static/example_images/high-five.jpg', 'urlaub2015', 'lsoe7fh4zf5ndh7e')")

conn.commit()

cur.close()
