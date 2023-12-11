# app/__init__.py
from flask import Flask, jsonify
from apps.extensions import db, jwt
from .user.routes import user
from .auth.routes import auth

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)
    app.register_blueprint(user, url_prefix='/user/')
    app.register_blueprint(auth, url_prefix='/oauth2/')

    return app


def config_jwt():
    @jwt.user_lookup_loader
    def user_lookup_callback(_jwt_headers, jwt_data):
        identity = jwt_data["sub"]

        return User.query.filter_by(username=identity).one_or_none()

    # jwt error handlers

    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_data):
        return jsonify({"message": "Token has expired", "error": "token_expired"}), 401

    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return (
            jsonify(
                {"message": "Signature verification failed", "error": "invalid_token"}
            ),
            401,
        )

    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return (
            jsonify(
                {
                    "message": "Request doesnt contain valid token",
                    "error": "authorization_header",
                }
            ),
            401,
        )