from flask import Flask
from datetime import timedelta
from flask_jwt_extended import JWTManager
from .db_config import  heroku_config
def create_app():
    # create the app
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'ZXXHLFIHT'
    app.config['JWT_ACCESS_TOKEN_EXPIRES']=timedelta(days=5)
    heroku_config()
    @app.route('/')
    def index():
        return "App Deployed!"
    jwt = JWTManager(app)
    from . import auth
    app.register_blueprint(auth.bp)
    from . import api
    app.register_blueprint(api.banks)
    from . import db
    db.init_app(app)
    return app