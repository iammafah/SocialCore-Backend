from flask import Flask                       # Flask core
from database.db import db, migrate           # SQLAlchemy & Alembic instances
from config import Config                     # App configuration
from routes.api import api_bp                 # API blueprint


def create_app():
    app = Flask(__name__)                     # Create Flask app instance
    app.config.from_object(Config)            # Load config from Config class

    db.init_app(app)                          # Initialize SQLAlchemy with app
    migrate.init_app(app, db)                 # Initialize Alembic migrations

    app.register_blueprint(
        api_bp,
        url_prefix="/iammafah"                # API base URL
    )

    return app                                # Return configured app


app = create_app()                            # Gunicorn entry point (DO NOT CHANGE)


if __name__ == "__main__":
    app.run()                                 # Local development only
