import os                  # Used to read environment variables securely
from dotenv import load_dotenv

load_dotenv()
class Config:              # Base configuration class
    SECRET_KEY = os.getenv("SECRET_KEY")                  # Flask security key
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")   # Database connection string (MySQL)
    SQLALCHEMY_TRACK_MODIFICATIONS = False                # Disable unnecessary SQLAlchemy overhead
    DEBUG = os.getenv("FLASK_DEBUG", "False") == "True"
    
