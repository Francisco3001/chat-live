import os
import configparser
from flask_sqlalchemy import SQLAlchemy

config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), '../main.conf'))
db = SQLAlchemy()
BASEDIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    
    # Directorio base del proyecto
    UPLOAD_FOLDER = os.path.join(BASEDIR, 'uploads')
    
    DB_USER = config['database']['user']
    DB_PASSWORD = config['database']['password']
    DB_HOST = config['database']['host']
    DB_PORT = config['database']['port']
    DB_NAME = config['database']['database']

    SQLALCHEMY_DATABASE_URI = (
        f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False