from datetime import timedelta
import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

class Config:
    # SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS")
    JWT_ACCESS_TOKEN_EXPIRES=timedelta(minutes=int(os.getenv('ACCESS_TOKEN_EXPIRY')))
    JWT_REFRESH_TOKEN_EXPIRES=timedelta(days=int(os.getenv('REFRESH_TOKEN_EXPIRY')))
    JWT_SECRET_KEY=os.getenv('JWT_SECRET_KEY')


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")
    DEBUG = True
    SQLALCHEMY_ECHO=False


# class ProdConfig(Config):
#     SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:///prod.db")
#     DEBUG = os.getenv("DEBUG", False)
#     SQLALCHEMY_ECHO = os.getenv("ECHO", False)
#     SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS", False)


# class TestConfig(Config):
#     SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"
#     SQLALCHEMY_ECHO = False
#     TESTING = True