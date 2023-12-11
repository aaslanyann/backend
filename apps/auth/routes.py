from flask import Blueprint
from .controllers import Controller

auth = Blueprint('oauth2', __name__)
controller = Controller()

auth.route('token', methods=['POST'])(controller.get_access_token)
auth.route('token/refresh', methods=['POST'])(controller.refresh_access_token)