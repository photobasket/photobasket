from bottle import route, run

@route('/album/', 'POST')
def newalbum():
    return {"key": "value"}

@route('/album/<albumname>/<userkey>/users', 'POST')
def newuser(albumname, userkey):
    return {"key": "value"}

@route('/album/<userkey>', 'GET')
def allalbums(userkey):
    return {"key": "value"}

@route('/album/<albumname>/<userkey>', 'GET')
def album(albumname, userkey):
    return {"key": "value"}

@route('/album/<albumname>/<userkey>/upload', 'POST')
def upload(albumname, userkey):
    return {"key": "value"}

run(host='localhost', port=8080)
