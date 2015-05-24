import os

from bottle import Bottle, route, request
from lib import check_existing_album_url
from lib import check_user_on_album
from db import get_db

route_album = Bottle()

@route_album.route('/rest/album/<albumname>/<userkey>', 'GET')
def album(albumname, userkey):
    # returns album informations including users, images

    db = get_db()

    cur = db.cursor()
    cur.execute("SELECT name, soundcloud_url FROM album WHERE url=?", (albumname, ))
    album_info = cur.fetchone()
    if album_info is None:
        raise "album not existing"

    if check_user_on_album(userkey, albumname) is None:
        raise "user not on album"

    album_users = []
    cur = db.cursor()
    cur.execute("SELECT email FROM users WHERE album_url=?", (albumname, ))
    user_emails = cur.fetchall()
    for user_email in user_emails:
        album_users.append(user_email[0])

    album_images = []
    cur = db.cursor()
    cur.execute("SELECT images.path, users.email, images.size FROM images, users WHERE images.album_url=? AND users.key = images.users_key", (albumname, ))
    db_album_images = cur.fetchall()
    for album_image in db_album_images:
        filename_parts = os.path.splitext( album_image[0] )
        thumb_name = filename_parts[0] + '.320' + filename_parts[1]

        album_images.append({
            'url': 'http://' + request.get_header('host') + album_image[0],
            'thumb320': 'http://' + request.get_header('host') + thumb_name,
            'size': album_image[2],
            'uploader': album_image[1]
        })


    return {
        "name": album_info[0],
        "soundcloud_url": album_info[1],
        "users": album_users,
        "images": album_images
    }
