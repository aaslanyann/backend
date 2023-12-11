from flask import jsonify, request
from ..user.models import User

from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_identity,
)


class Controller:
    def get_access_token(self, ):
        data = request.get_json()

        user = User.get_user_by_email(email=data.get("email"))

        if user and (user.check_password(password=data.get("password"))):
            access_token_ttl = 3600  # 1 hour
            refresh_token_ttl = 3600 * 24  # 24 hour

            access_token = create_access_token(identity=user.email, expires_delta=access_token_ttl)
            refresh_token = create_refresh_token(identity=user.email, expires_delta=refresh_token_ttl)

            return (
                jsonify(
                    {
                        "message": "Logged In ",
                        "access_token": access_token,
                        "refresh": refresh_token,
                    }
                ),
                200,
            )

        return jsonify({"error": "Invalid username or password"}), 400


    @jwt_required(refresh=True)
    def refresh_access_token(self):
        identity = get_jwt_identity()
        new_access_token = create_access_token(identity=identity)
        new_refresh_token = create_refresh_token(identity=identity)
        return jsonify({"access_token": new_access_token, "refresh_token": new_refresh_token})
