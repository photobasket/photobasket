from bottle import Bottle, route, static_file, SimpleTemplate
from routes import route_album, route_newalbum, route_newuser, route_upload, route_image, route_downloadalbum

root = Bottle()

@root.route('/')
def index():
    tpl = SimpleTemplate(name='frontend/index.html.tpl')
    return tpl.render()

@root.route('/album/<albumname>/<userkey>', 'GET')
def album(albumname, userkey):
    tpl = SimpleTemplate(name='frontend/album.html.tpl')
    return tpl.render()

@root.route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='frontend')

@root.route('/fonts/<filename:path>')
def send_static(filename):
    return static_file(filename, root='fonts')

root.merge(route_album)
root.merge(route_newalbum)
root.merge(route_newuser)
root.merge(route_downloadalbum)
root.merge(route_upload)
root.merge(route_image)

root.run(host='0.0.0.0', port=80)
