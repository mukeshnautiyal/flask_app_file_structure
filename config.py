import os
from dotenv import load_dotenv

# Load .env file in the app
load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = "mysql://"+os.environ.get('DBUSER')+":"+os.environ.get('DBPASSWORD')+"@localhost/"+os.environ.get('DBNAME')
    SQLALCHEMY_TRACK_MODIFICATIONS = False