from bottle import route, run

@route('/album/', 'POST')
def newalbum():
    # creates a new album
    # params:
    #   albumname: name for the new album (plain text)
    return {
        "success": "created",
        "albumname": "Ostsee 2015",
        "albumurl": "ostsee2015"
    }

@route('/album/<albumname>/<userkey>/users', 'POST')
def newuser(albumname, userkey):
    # creates a new user for the album
    # params:
    #   useremail: email adress for the user
    return {
        "success": "created",
        "useremail": "new@user.invalid"
    }

# @route('/album/<userkey>', 'GET')
# def allalbums(userkey):
#     return {"key": "value"}

@route('/album/<albumname>/<userkey>', 'GET')
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

@route('/album/<albumname>/<userkey>/upload', 'POST')
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

run(host='localhost', port=8080)
