from bottle import Bottle, route
from lib import check_existing_album_url
from lib import check_user_on_album
from db import get_db

route_album = Bottle()

@route_album.route('/rest/album/<albumname>/<userkey>', 'GET')
def album(albumname, userkey):
    # returns album informations including users, images

    if check_existing_album_url(albumname) is None:
        raise "album not existing"

    if check_user_on_album(userkey, albumname) is None:
        raise "user not on album"

    db = get_db()

    album_users = []
    cur = db.cursor()
    cur.execute("SELECT email FROM users WHERE album_url=?", (albumname, ))
    user_emails = cur.fetchall()
    for user_email in user_emails:
        album_users.append(user_email[0])

    album_images = []
    cur = db.cursor()
    cur.execute("SELECT images.path, users.email FROM images, users WHERE images.album_url=? AND users.key = images.users_key", (albumname, ))
    db_album_images = cur.fetchall()
    for album_image in db_album_images:
        album_images.append({
            'url': album_image[0],
            'thumb320': album_image[0],
            'uploader': album_image[1]
        })

    return {
        "users": album_users,
        "images": album_images
    }
