from apps.extensions import db
from datetime import datetime
import enum
from werkzeug.security import check_password_hash


class User(db.Model):
    __tablename__ = 'users'

    class UserRoleEnum(str, enum.Enum):
        USER = 'user'
        ADMIN = 'admin'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    first_name = db.Column(db.String(60), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    position = db.Column(db.String(50))
    role = db.Column(db.Enum(UserRoleEnum), default='user', nullable=False)
    password = db.Column(db.Text())
    created_at = db.Column(db.DateTime, default=datetime.utcnow, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, server_default=db.func.now())

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f"<User {self.username}>"

    @classmethod
    def get_user_by_email(cls, email):
        return cls.query.filter_by(email=email).first()


