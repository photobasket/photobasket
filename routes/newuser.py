from bottle import Bottle, route

from lib import create_user_for_album
from lib import send_email

route_newuser = Bottle()

@route_newuser.route('/album/<albumname>/<userkey>/users', 'POST')
def newuser(albumname, userkey):
    # creates a new user for the album
    # params:
    #   useremail: email adress for the user
    
    jsonrequest = json.load(request.body)
    user_email = jsonrequest["useremail"]

    user_key = create_user_for_album(user_email, albumname)
    
    # TODO: re-enable before live
    # send_email("useremail", "Neues Album", "Das Album wurde erstellt")
    
    return {
        "success": "created",
        "useremail": user_email,
        "userkey": user_key
    }
