from bottle import Bottle, route

route_upload = Bottle()

@route_upload.route('/album/<albumname>/<userkey>/upload', 'POST')
def upload(albumname, userkey):
    # bildupload
    # multiplart upload, all files accepted
    return {
        "images": [
            {
                "url": "https://myownspace.invalid/photonet/albumname/images/neues+bild.jpg",
                "thumb320": "https://myownspace.invalid/photonet/albumname/images/neues+bild.320.jpg",
                "thumb640": "https://myownspace.invalid/photonet/albumname/images/neues+bild.640.jpg",
                "uploader": "user1@gmail.com"
            },
            {
                "url": "https://myownspace.invalid/photonet/albumname/images/abschied.jpg",
                "thumb320": "https://myownspace.invalid/photonet/albumname/images/abschied.320.jpg",
                "thumb640": "https://myownspace.invalid/photonet/albumname/images/abschied.640.jpg",
                "uploader": "user1@gmail.com"
            }
        ]
    }
