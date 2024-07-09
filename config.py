import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'b2e9f07c8d7a8b9c9e1f7d2e5a7d1c9f'  # Rastgele oluşturulmuş secret key
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///site.db'  # SQLite veritabanı URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
