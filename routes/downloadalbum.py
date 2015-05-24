import os
import zipfile
import hashlib
from fdsend import send_file

from bottle import Bottle, route
from db import get_db
from lib import check_user_on_album

route_downloadalbum = Bottle()

@route_downloadalbum.route('/rest/album/<albumname>/<userkey>/download/<dummy>.zip', 'GET')
def downloadalbum(albumname, userkey, dummy):

    db = get_db()

    cur = db.cursor()
    cur.execute("SELECT name, url FROM album WHERE url=?", (albumname, ))
    album_info = cur.fetchone()
    if album_info is None:
        raise "album not existing"

    if check_user_on_album(userkey, albumname) is None:
        raise "user not on album"

    album_path = './images/' + albumname + '/'

    zip_file_path = zip_album(album_path, albumname)

    size = os.path.getsize(zip_file_path)
    mtime = os.path.getmtime(zip_file_path)

    fd = open(zip_file_path, 'rb')
    return send_file(fd, filename=albumname+'.zip', ctype='application/zip', size=size, timestamp=mtime)

def zip_album(path, albumname):
    files_in_path = []
    for root, dirs, files in os.walk(path):
        for file in files:
            files_in_path.append( file )

    album_hash = hashlib.md5('/'.join(files_in_path)).hexdigest()

    zip_file_path = '/tmp/' + albumname + '.' + album_hash + '.zip'

    if os.path.isfile(zip_file_path):
        return zip_file_path

    zipf = zipfile.ZipFile(zip_file_path, 'w')

    for root, dirs, files in os.walk(path):
        for file in files:
            zipf.write(os.path.join(root, file))

    zipf.close()

    return zip_file_path
