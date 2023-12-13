from flask import jsonify, request
from ..user.models import User
from datetime import datetime, timedelta

from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_identity,
)


class Controller:
    def get_access_token(self, ):
        """
        Authenticate a user.
        ---
        parameters:
        - in: body
          name: body
          description: Get access token
          required: true
          schema:
            type: object
            properties:
              email:
                type: string
              password:
                type: string
        responses:
          200:
            description: Successfully authenticated. Returns access and refresh tokens.
          400:
            description: Invalid username or password.

        """

        data = request.get_json()

        user = User.get_user_by_email(email=data.get("email"))

        if user and (user.check_password(password=data.get("password"))):
            now = datetime.now()
            access_token_ttl = timedelta(hours=1)
            refresh_token_ttl = timedelta(hours=24)

            access_token = create_access_token(identity=user.email, expires_delta=access_token_ttl)
            refresh_token = create_refresh_token(identity=user.email, expires_delta=refresh_token_ttl)

            return (
                jsonify(
                    {
                        "message": "Logged In ",
                        "access_token": access_token,
                        "refresh_token": refresh_token,
                    }
                ),
                200,
            )

        return jsonify({"error": "Invalid username or password"}), 400


    @jwt_required(refresh=True)
    def refresh_access_token(self):
        """
        Refresh Access Token
        ---
        parameters:
        - in: header
          name: header
          description: Get new access and refresh tokens
          required: true
          schema:
            type: object
            properties:
              refresh_token:
                type: string
        responses:
          200:
            description: Refresh Token Valid. Returns access and refresh tokens.
          400:
            description: Signature verification failed.
       """
        identity = get_jwt_identity()
        new_access_token = create_access_token(identity=identity)
        new_refresh_token = create_refresh_token(identity=identity)
        return jsonify({"access_token": new_access_token, "refresh_token": new_refresh_token}), 200
