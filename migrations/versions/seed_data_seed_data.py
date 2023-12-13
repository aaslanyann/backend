"""Seed data

Revision ID: seed_data
Revises: 5a19440ab7af
Create Date: 2023-12-12 19:34:36.116443

"""
from alembic import op
from werkzeug.security import generate_password_hash
from apps.user.models import User
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'seed_data'
down_revision = '5a19440ab7af'
branch_labels = None
depends_on = None


def upgrade():
    op.bulk_insert(User.__table__,[
                   {'email': 'admin1@example.com', 'first_name': 'John', 'last_name': 'Doe', 'position': 'Engineer',
                    'role': 'admin', 'password': generate_password_hash('Pass_word1')},
                   {'email': 'admin2@example.com', 'first_name': 'Jane', 'last_name': 'Doe', 'position': 'Manager',
                    'role': 'admin', 'password': generate_password_hash('Pass_word!2')},
                   {'email': 'admin3@example.com', 'first_name': 'Alice', 'last_name': 'Smith', 'position': 'Developer',
                    'role': 'admin', 'password': generate_password_hash('!Pass_word3')},
                   {'email': 'admin4@example.com', 'first_name': 'Bob', 'last_name': 'Johnson', 'position': 'Designer',
                    'role': 'admin', 'password': generate_password_hash('!!Pass_word4')},
                   {'email': 'admin5@example.com', 'first_name': 'Eve', 'last_name': 'Brown', 'position': 'Analyst',
                    'role': 'admin', 'password': generate_password_hash('Pass__word5')}
                   ])


def downgrade():
    pass
