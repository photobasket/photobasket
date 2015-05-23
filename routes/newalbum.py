from bottle import Bottle, route

route_newalbum = Bottle()

@route_newalbum.route('/album/', 'POST')
def newalbum():
    # creates a new album
    # params:
    #   albumname: name for the new album (plain text)
    #   useremail: email for the initial user that can add new users
    return {
        "success": "created",
        "albumname": "Ostsee 2015",
        "albumurl": "ostsee2015",
        "useremail": "albumcreator@user.invalid",
        "userkey": "qwertyuiop1234567890"
    }
