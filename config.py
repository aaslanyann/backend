# app/config.py
from dotenv import load_dotenv
import os



load_dotenv(dotenv_path='.env', override=True)



user = os.getenv('POSTGRES_USER')
host = os.getenv('HOST')
password = os.getenv('POSTGRES_PASSWORD')
db_name = os.getenv('POSTGRES_DB')
port = os.getenv('PORT')
debug = bool(os.getenv('DEBUG'))


class Config:
    SECRET_KEY = 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = f'postgresql://{user}:{password}@{host}/{db_name}'
    DEBUG = debug
    # Add other configuration variables
