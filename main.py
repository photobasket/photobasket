from bottle import Bottle, route, static_file
from routes import route_album, route_newalbum, route_newuser, route_upload

root = Bottle()

@root.route('/')
def index():
    return static_file('index.html', root='frontend')

@root.route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='frontend')

@root.route('/fonts/<filename:path>')
def send_static(filename):
    return static_file(filename, root='fonts')

root.merge(route_album)
root.merge(route_newalbum)
root.merge(route_newuser)
root.merge(route_upload)

root.run(host='0.0.0.0', port=8080)
