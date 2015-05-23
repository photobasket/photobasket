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
                "thumb320": "https://myownspace.invalid/photonet/albumname/images/strandfoto.320.jpg",
                "thumb640": "https://myownspace.invalid/photonet/albumname/images/strandfoto.640.jpg",
                "uploader": "user1@gmail.com"
            },
            {
                "url": "https://myownspace.invalid/photonet/albumname/images/lagerfeuer.jpg",
                "thumb320": "https://myownspace.invalid/photonet/albumname/images/lagerfeuer.320.jpg",
                "thumb640": "https://myownspace.invalid/photonet/albumname/images/lagerfeuer.640.jpg",
                "uploader": "lemmings@hotmail.fi"
            },
            {
                "url": "https://myownspace.invalid/photonet/albumname/images/sonnenuntergang+auf+r%C3%BCgen.jpg",
                "thumb320": "https://myownspace.invalid/photonet/albumname/images/sonnenuntergang+auf+r%C3%BCgen.320.jpg",
                "thumb640": "https://myownspace.invalid/photonet/albumname/images/sonnenuntergang+auf+r%C3%BCgen.640.jpg",
                "uploader": "lemmings@hotmail.fi"
            },
            {
                "url": "https://myownspace.invalid/photonet/albumname/images/lustige+leute.jpg",
                "thumb320": "https://myownspace.invalid/photonet/albumname/images/lustige+leute.320.jpg",
                "thumb640": "https://myownspace.invalid/photonet/albumname/images/lustige+leute.640.jpg",
                "uploader": "lemmings@hotmail.fi"
            },
            {
                "url": "https://myownspace.invalid/photonet/albumname/images/bootsfahrt.jpg",
                "thumb320": "https://myownspace.invalid/photonet/albumname/images/bootsfahrt.320.jpg",
                "thumb640": "https://myownspace.invalid/photonet/albumname/images/bootsfahrt.640.jpg",
                "uploader": "user1@gmail.com"
            },
            {
                "url": "https://myownspace.invalid/photonet/albumname/images/unfall.jpg",
                "thumb320": "https://myownspace.invalid/photonet/albumname/images/unfall.320.jpg",
                "thumb640": "https://myownspace.invalid/photonet/albumname/images/unfall.640.jpg",
                "uploader": "user1@gmail.com"
            }
        ]
    }
