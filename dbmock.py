import sqlite3

conn = sqlite3.connect('photonet.db')
cur = conn.cursor()

cur.execute("INSERT INTO album VALUES ('hackathonHH Awesomeness', 'hackathonhhawesomeness', '')")

cur.execute("INSERT INTO users VALUES ('hackathonhhawesomeness', 'xb5ndH73GHz3jApc', 'hackers@hackathonHH2015.de')")

conn.commit()

cur.close()
