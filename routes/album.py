from bottle import Bottle, route

route_album = Bottle()

@route_album.route('/album/<albumname>/<userkey>', 'GET')
def album(albumname, userkey):
    # returns album informations including users, images
    return {
        "users": [ "user1@gmail.com", "lemmings@hotmail.fi", "loremipsum@yahoo.de" ],
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
