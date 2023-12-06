# app/__init__.py
from flask import Flask
from apps.extensions import db

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    # Initialize extensions
    db.init_app(app)

    return app