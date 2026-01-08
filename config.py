import os                  # Used to read environment variables securely
from dotenv import load_dotenv

load_dotenv()
class Config:              # Base configuration class
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")   # Database connection string (MySQL)
    SQLALCHEMY_TRACK_MODIFICATIONS = False                # Disable unnecessary SQLAlchemy overhead
    
