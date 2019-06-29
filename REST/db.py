import psycopg2
import psycopg2.extras
from flask import g
from .db_config import user, password, host, port, database
def connect_db():
    if 'conn' not in g:
        try:
            g.conn = psycopg2.connect(user = user, password=password , host=host, port=port, database=database, cursor_factory=psycopg2.extras.DictCursor)
        except Exception as e:
            print(str(e))
    if 'cur' not in g:
        try:
            g.cur = g.conn.cursor()
        except Exception as e:
            print(str(e))
    print("DB connected")

def update_query(query):
    if 'conn' not in g or 'cur' not in g:
        connect_db()
    g.cur.execute(query)
    g.conn.commit()

def select_query(query):
    if 'conn' not in g or 'cur' not in g:
        connect_db()
    g.cur.execute(query)
    return g.cur
def close_db(e=None):
    print("closing connection")
    conn = g.pop('conn', None)
    if conn is not None:
        try:
            conn.close()
        except Exception as e:
            print(str(e))

def init_app(app):
    print("in DB")
    app.before_request(connect_db)
    app.teardown_appcontext(close_db)