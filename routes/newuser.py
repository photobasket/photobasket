from bottle import Bottle, route

route_newuser = Bottle()

@route_newuser.route('/album/<albumname>/<userkey>/users', 'POST')
def newuser(albumname, userkey):
    # creates a new user for the album
    # params:
    #   useremail: email adress for the user
    return {
        "success": "created",
        "useremail": "new@user.invalid",
        "userkey": "1234567890qwertyuiop"
    }
