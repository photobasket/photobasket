from bottle import Bottle, route
from fdsend import send_file
import os

route_image = Bottle()

@route_image.route('/images/<albumname>/<filename>', 'GET')
def album(albumname, filename):
    
    filepath = "images/"+albumname+"/"+filename

    size = os.path.getsize(filepath)
    mtime = os.path.getmtime(filepath)
    
    fd = open(filepath, 'rb')    
    return send_file(fd, ctype='image/jpeg', size=size, timestamp=mtime)
