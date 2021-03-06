import os
from PIL import Image, ImageOps

from bottle import Bottle, route, request

from db import get_db

route_upload = Bottle()

@route_upload.route('/rest/album/<albumname>/<userkey>/upload', 'POST')
def upload(albumname, userkey):
    # bildupload
    # multiplart upload, all files accepted

    db = get_db()

    cur = db.cursor()
    cur.execute("SELECT email FROM users WHERE key=?", (userkey, ))
    user = cur.fetchone()
    cur.close()

    if user is None:
        raise 'user does not exist'

    upload = request.files.get('file')
    name, ext = os.path.splitext(upload.filename)

    if ext not in ('.png','.jpg','.jpeg','.gif'):
        return {'error' : 'File extension not allowed.'}

    save_path = "images/"+albumname+'/'

    if not os.path.exists(save_path):
        os.makedirs(save_path)

    upload.save(save_path)

    img = Image.open(save_path+upload.filename)
    width, height = img.size

    thumb = ImageOps.fit(img, (320, 320), method = Image.ANTIALIAS, centering = (0.5,0.5))
    fileext = os.path.splitext( upload.filename )
    thumb.save(save_path + fileext[0] + '.320' + fileext[1], 'JPEG', quality=80)

    cur = db.cursor()

    cur.execute("""
        INSERT INTO images (path, size, album_url, users_key) VALUES (?, ?, ?, ?)
    """, ('/'+save_path+upload.filename, str(width)+'x'+str(height), albumname, userkey, ))
    db.commit()

    cur.close()

    return {
        "images": [
            {
                "url": 'http://' + request.get_header('host') + '/' + save_path + upload.filename,
                "uploader": user[0],
            }
        ]
    }
