import shortuuid
from db import get_db

def create_user_for_album(user_email, album_ident):
    db = get_db()

    # check if album exists
    cur = db.cursor()
    cur.execute("SELECT url FROM album WHERE url=?", (album_ident, ))
    albums = cur.fetchone()

    if albums is None:
        raise "Ablum not found"

    # check if user has already a key
    cur = db.cursor()
    cur.execute("SELECT key FROM users WHERE album_url=? AND email=?", (album_ident, user_email, ))
    users = cur.fetchone()

    if users is not None:
        return users[0]

    # create new user
    new_user_id = shortuuid.ShortUUID().random(length=15)
    cur = db.cursor()
    cur.execute("INSERT INTO users (album_url, email, key) VALUES (?, ?, ?)", (album_ident, user_email, new_user_id, ))
    db.commit()

    return new_user_id
