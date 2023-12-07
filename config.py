# app/config.py
from dotenv import load_dotenv
import os

arg = os.sys.argv


value = arg[1] if 1 < len(arg) else None

if value == '--env=prod':
    print('prod')
    load_dotenv(dotenv_path='.env', override=True)
elif value == '--env=tst':
    print('tst')
    load_dotenv(dotenv_path='.env.tst', override=True)
else:
    print('dev')
    load_dotenv(dotenv_path='.env.dev', override=True)



user = os.getenv('USER')
host = os.getenv('HOST')
password = os.getenv('PASSWORD')
db_name = os.getenv('DB_NAME')
port = os.getenv('PORT')

class Config:
    SECRET_KEY = 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = f'postgresql://{user}:{password}@{host}:{port}/{db_name}'
    # Add other configuration variables
