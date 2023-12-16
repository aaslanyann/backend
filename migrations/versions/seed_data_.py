"""empty message

Revision ID: seed_data
Revises: 9a03d89a61a4
Create Date: 2023-12-16 00:34:44.649012

"""
from alembic import op
from werkzeug.security import generate_password_hash
from apps.user.models import User
from apps.company.models import Industry
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'seed_data'
down_revision = '4e0abcae108e'
branch_labels = None
depends_on = None


def upgrade():
    op.bulk_insert(User.__table__, [
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

    op.bulk_insert(Industry.__table__, [
        {"name": "saas"},
        {"name": "ai and ml"},
        {"name": "big data"},
        {"name": "fintech"},
        {"name": "ecommerce"},
        {"name": "cybersecurity"},
        {"name": "healthech"},
        {"name": "mobility tech"},
        {"name": "life sciences"},
        {"name": "cloud tech"}
    ])


def downgrade():
    pass
