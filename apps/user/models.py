from apps.extensions import db



class User(db.Model):
    __tablename__ = 'results'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=True)
    page = db.Column(db.Integer, nullable=True)

