# app.py
from apps import create_app
from apps.extensions import db
from config import Config
from flask_migrate import Migrate
from flasgger import Swagger



app = create_app()
swagger = Swagger(app)
migrate = Migrate(app, db)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=Config.DEBUG)

