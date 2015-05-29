import sqlite3

conn = sqlite3.connect('photonet.db')
cur = conn.cursor()

cur.execute("INSERT INTO album VALUES ('hackathonHH 2015', 'hackathonhh2015', '')")

cur.execute("INSERT INTO users VALUES ('hackathonhh2015', 'x83hdz7w6x5dbn4t', 'Arne.Steen@gmx.de')")

conn.commit()

cur.close()
