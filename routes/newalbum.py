from bottle import Bottle, route, request
from lib import create_user_for_album
from lib import create_album, full_album_url
from lib import send_email
import json


route_newalbum = Bottle()

@route_newalbum.route('/rest/album/', 'POST')
def newalbum():
    # creates a new album
    # params:
    #   albumname: name for the new album (plain text)
    #   useremail: email for the initial user that can add new users

    jsonrequest = json.load(request.body)
    album_name = jsonrequest["albumname"]
    user_email = jsonrequest["useremail"]

    album_key = create_album(album_name)
    user_key = create_user_for_album(user_email, album_key)
    album_url = full_album_url(request, album_key, user_key)

    # TODO: re-enable before live
    # send_email("useremail", "Neues Album", "Das Album wurde erstellt")

    return {
        "success": "created",
        "albumname": jsonrequest["albumname"],
        "albumurl": album_url,
        "useremail": user_email,
        "userkey": user_key
    }
