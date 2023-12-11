from apps.extensions import db
from sqlalchemy import Enum
import enum


class User(db.Model):
    __tablename__ = 'users'

    class UserRoleEnum(str, enum.Enum):
        USER = 'user'
        ADMIN = 'admin'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    position = db.Column(db.String(50))
    role = db.Column(db.Enum(UserRoleEnum), default='user', nullable=False)
