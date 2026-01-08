from flask import Flask
from database.db import db, migrate
from config import Config
from routes.api import api_bp

def create_app():                   # Application factory function

    app = Flask(__name__)           # Create Flask app instance

    app.config.from_object(Config)  # Load configuration

    db.init_app(app)                # Initialize SQLAlchemy

    migrate.init_app(app, db)       # Initialize migrations

    app.register_blueprint(api_bp, url_prefix="/iammafah")  # Register API blueprint with URL prefix     
    return app                      # Return configured app


app = create_app()                  # Create app using factory

if __name__ == "__main__":
    app.run(debug=True)             # Run development server
