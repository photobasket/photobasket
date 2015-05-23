from bottle import Bottle, route, request
from lib import create_user_for_album
from lib import send_email
import json


route_newalbum = Bottle()

@route_newalbum.route('/album/', 'POST')
def newalbum():
    jsonrequest = json.load(request.body)
    albumname = jsonrequest["albumname"] 
    useremail = jsonrequest["useremail"] 
    userkey = create_user_for_album(useremail, albumname);
    send_email(useremail, "Neues Album", "Das Album wurde erstellt")
    # creates a new album
    # params:
    #   albumname: name for the new album (plain text)
    #   useremail: email for the initial user that can add new users
    return {
        "success": "created",
        "albumname": albumname,
        "albumurl": "ostsee2015",
        "useremail": useremail,
        "userkey": userkey
    }
