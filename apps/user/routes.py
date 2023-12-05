from flask import jsonify
from flask_restful import Resource
from .models import User

class UserListResource(Resource):
    def get(self):
        return jsonify({"message": "List of users"})

    def post(self):
        return jsonify({"message": "User added"})

class UserResource(Resource):
    def get(self, user_id):
        return jsonify({"message": f"Details of user {user_id}"})

    def delete(self, user_id):
        return jsonify({"message": f"User {user_id} deleted"})