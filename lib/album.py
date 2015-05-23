import re
import inspect
from db import get_db

def create_album(album_name):
    album_name_cleaner = re.compile( '[^a-zA-Z0-9]')
    clean_album_name = album_name_cleaner.subn( '', album_name)[0]

    existing_album_name = check_existing_album_url(clean_album_name)
    if existing_album_name is not None:
        raise "Ablum already existing"

    db = get_db()
    cur = db.cursor()
    cur.execute("INSERT INTO album (name, url) VALUES (?, ?)", (album_name, clean_album_name, ))
    db.commit()
    cur.close()

    return clean_album_name

def full_album_url(request, album_key, user_id):
    return 'http://' + request.get_header('host') + '/' + album_key + '/' + user_id + '/'

def check_existing_album_url(album_url):
    db = get_db()

    # check if album exists
    cur = db.cursor()
    cur.execute("SELECT url FROM album WHERE url=?", (album_url, ))
    albums = cur.fetchone()

    if albums is not None:
        return albums[0]
