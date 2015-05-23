import re
import inspect
from db import get_db

map = {' ' : '_',
       '.' : '_dot_',
       '&' : '_and_',
       '$' : '_dolar_',
       ':' : '_colon_',
       ',' : '_comma_'
       }

_under = re.compile(r'_+')

def parse_for_beautiful_url(text):
	str = ''.join([map.get(ch,ch) for ch in text])
	str = _under.sub('_',str)
	if str[-1:] == '_': return str[0:-1]
	return str

def create_album(album_name):
    album_name_cleaner = re.compile( '[^a-zA-Z0-9]')
    clean_album_name = album_name_cleaner.subn( '', album_name)[0]

    existing_album_name = _check_existing_album_url(clean_album_name)
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

#############################
# private

def _check_existing_album_url(album_url):
    db = get_db()

    # check if album exists
    cur = db.cursor()
    cur.execute("SELECT url FROM album WHERE url=?", (album_url, ))
    albums = cur.fetchone()

    if albums is not None:
        return albums[0]
