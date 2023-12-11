from apps.extensions import db
import enum
from werkzeug.security import generate_password_hash, check_password_hash


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

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f"<User {self.username}>"

    @classmethod
    def get_user_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

