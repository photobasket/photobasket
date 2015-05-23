from bottle import Bottle
from routes import route_album, route_newalbum, route_newuser, route_upload

root = Bottle()

root.merge(route_album)
root.merge(route_newalbum)
root.merge(route_newuser)
root.merge(route_upload)

root.run(host='0.0.0.0', port=8080)
