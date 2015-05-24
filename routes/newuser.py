import json

from bottle import Bottle, route, request

from lib import create_user_for_album
from db import get_db
from lib import send_email

route_newuser = Bottle()

@route_newuser.route('/album/<albumurl>/<userkey>/users', 'POST')
def newuser(albumurl, userkey):
    # creates a new user for the album
    # params:
    #   useremail: email adress for the user
    
    jsonrequest = json.load(request.body)
    user_email = jsonrequest["useremail"]

    user_key = create_user_for_album(user_email, albumurl)

    db = get_db()

    # check if album exists
    cur = db.cursor()
    cur.execute("SELECT name FROM album WHERE url=?", (albumurl, ))
    albums = cur.fetchone()

    if albums is None:
        raise "Ablum not found"
    albumname = albums[0]
    
    # TODO: re-enable before live
    send_email(user_email, "You've been invited to share your memories of " + albumname + " with PhotoBasket", """Hello!

You've been invited to the album """ + albumname + """. 

With PhotoBasket, you can see your friends' photos and share your own from your phone or computer, download pictures you want to keep, and add the perfect soundtrack to your memories with SoundCloud. 
To start seeing and adding memories, follow this unique, personalized link:

""" + 'http://' + request.get_header('host') + "/album/" + albumurl + "/" + user_key + """

Just follow the link and the intuitive PhotoBasket interface will guide you through the process.

Can I share the link with others?
Your link is your unique identifier to access and add to this album on PhotoBasket, so make sure to keep it safe and don't share it -  or they might start sharing things under your name! Instead, you can add other users from the PhotoBasket album to have them sent their own personal link.

Is my data safe? Who can see my photos?
Your data will be stored on the server of your PhotoBasket host - so if you trust your friend, your data is in good hands. ;) None of it will be uploaded to third-party servers. 
Everyone who was invited to the group will be able to see and download your pictures but they will not be accessible without the correct access link.

Happy sharing!

Your friendly PhotoBasket bot""")
    
    return {
        "success": "created",
        "useremail": user_email,
        "userkey": user_key
    }
