from bottle import Bottle, route

route_album = Bottle()

@route_album.route('/album/<albumname>/<userkey>', 'GET')
def album(albumname, userkey):
    # returns album informations including users, images
    return {
        "users": [ "user1@gmail.com", "lemmings@hotmail.fi", "loremipsum@yahoo.de" ],
        "images": [
            {
                "url": "https://myownspace.invalid/photonet/albumname/images/strandfoto.jpg",
                "thumb320": "/static/example_images/beach-320.jpg",
                "uploader": "user1@gmail.com"
            },
            {
                "url": "https://myownspace.invalid/photonet/albumname/images/lagerfeuer.jpg",
                "thumb320": "/static/example_images/dog-320.jpg",
                "uploader": "lemmings@hotmail.fi"
            },
            {
                "url": "https://myownspace.invalid/photonet/albumname/images/sonnenuntergang+auf+r%C3%BCgen.jpg",
                "thumb320": "/static/example_images/happy-family-320.jpg",
                "uploader": "lemmings@hotmail.fi"
            },
            {
                "url": "https://myownspace.invalid/photonet/albumname/images/lustige+leute.jpg",
                "thumb320": "/static/example_images/high-five-320.jpg",
                "uploader": "lemmings@hotmail.fi"
            },
            {
                "url": "https://myownspace.invalid/photonet/albumname/images/lustige+leute.jpg",
                "thumb320": "/static/example_images/hiking-family-320.jpg",
                "uploader": "lemmings@hotmail.fi"
            },
            {
                "url": "https://myownspace.invalid/photonet/albumname/images/lustige+leute.jpg",
                "thumb320": "/static/example_images/cat-320.jpg",
                "uploader": "lemmings@hotmail.fi"
            },
            {
                "url": "https://myownspace.invalid/photonet/albumname/images/lustige+leute.jpg",
                "thumb320": "/static/example_images/wedding-320.jpg",
                "uploader": "lemmings@hotmail.fi"
            }

        ]
    }
