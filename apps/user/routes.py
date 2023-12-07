from flask import Blueprint
from .controllers import Controller

user = Blueprint('user', __name__)


user.route('', methods=['GET'])(Controller.index)
user.route('example', methods=['GET'])(Controller.example)
user.route('json-example', methods=['GET'])(Controller.json_example)