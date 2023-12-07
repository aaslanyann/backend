# app/__init__.py
from flask import Flask
from apps.extensions import db
from .user.routes import user

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    # Initialize extensions
    db.init_app(app)
    app.register_blueprint(user, url_prefix='/user/')

    return app