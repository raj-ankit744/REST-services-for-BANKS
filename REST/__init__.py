from flask import Flask
from datetime import timedelta
from flask_jwt_extended import JWTManager

def create_app():
    # create the app
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'super-secret'
    app.config['JWT_ACCESS_TOKEN_EXPIRES']=timedelta(seconds=200)
    jwt = JWTManager(app)
    from . import auth
    app.register_blueprint(auth.bp)
    from . import api
    app.register_blueprint(api.banks)
    from . import db
    db.init_app(app)
    return app