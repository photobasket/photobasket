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

    return {
        "users": album_users,
        "images": [
            {
                "url": "/static/example_images/beach.jpg",
                "thumb320": "/static/example_images/beach-320.jpg",
                "uploader": "user1@gmail.com"
            },
            {
                "url": "/static/example_images/dog.jpg",
                "thumb320": "/static/example_images/dog-320.jpg",
                "uploader": "lemmings@hotmail.fi"
            },
            {
                "url": "/static/example_images/happy-family.jpg",
                "thumb320": "/static/example_images/happy-family-320.jpg",
                "uploader": "lemmings@hotmail.fi"
            },
            {
                "url": "/static/example_images/high-five.jpg",
                "thumb320": "/static/example_images/high-five-320.jpg",
                "uploader": "lemmings@hotmail.fi"
            },
            {
                "url": "/static/example_images/hiking-family.jpg",
                "thumb320": "/static/example_images/hiking-family-320.jpg",
                "uploader": "lemmings@hotmail.fi"
            },
            {
                "url": "/static/example_images/cat.jpg",
                "thumb320": "/static/example_images/cat-320.jpg",
                "uploader": "lemmings@hotmail.fi"
            },
            {
                "url": "/static/example_images/wedding.jpg",
                "thumb320": "/static/example_images/wedding-320.jpg",
                "uploader": "lemmings@hotmail.fi"
            }

        ]
    }
