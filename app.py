# app.py
from apps import create_app
from apps.extensions import db

from flask_migrate import Migrate


app = create_app()

migrate = Migrate(app, db)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
