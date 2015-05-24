import sqlite3

conn = sqlite3.connect('photonet.db')
cur = conn.cursor()

cur.execute("INSERT INTO album VALUES ('hackathonHH 2015', 'hackathonhh2015', '')")

cur.execute("INSERT INTO users VALUES ('hackathonhh2015', 'xb5ndH73GHz3jApc', 'hackers@hackathonHH2015.de')")

conn.commit()

cur.close()
