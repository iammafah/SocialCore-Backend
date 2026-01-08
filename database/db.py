from flask_sqlalchemy import SQLAlchemy    # ORM for handling database models and queries
from flask_migrate import Migrate          # Manages database schema migrations

db = SQLAlchemy()                          # Global SQLAlchemy instance
migrate = Migrate()                        # Handles Alembic-based migrations
