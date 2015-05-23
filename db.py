import sqlite3

def get_db():
    if not hasattr(get_db, 'db'):
        db = sqlite3.connect('photonet.db')
        get_c_lib.db = db

    return get_db.db
