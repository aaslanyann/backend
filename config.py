# app/config.py
from dotenv import load_dotenv
import os



load_dotenv(dotenv_path='.env', override=True)



user = os.getenv('USER')
host = os.getenv('HOST')
password = os.getenv('PASSWORD')
db_name = os.getenv('DB_NAME')
port = os.getenv('PORT')

print(user,host,password,db_name,port)

class Config:
    SECRET_KEY = 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = f'postgresql://{user}:{password}@{host}:{port}/{db_name}'
    # Add other configuration variables
