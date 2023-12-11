from flask import jsonify


class Controller:
    @staticmethod
    def index():
        return 'User Home'

    @staticmethod
    def example():
        return 'Example page'

    @staticmethod
    def json_example():
        data = {'name': 'John', 'age': 30, 'city': 'New York'}
        response = jsonify(data)

        return response
