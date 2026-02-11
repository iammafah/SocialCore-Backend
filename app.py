from flask import Flask
from flask_cors import CORS
from database.db import db, migrate
from config import Config

# blueprints
from routes.api import api_bp
from utils.exporters.csv_exporter import csv_bp
from utils.exporters.xlsx_exporter import xlsx_bp
from utils.exporters.pdf_exporter import pdf_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # enable CORS
    CORS(app)

    # database init
    db.init_app(app)
    migrate.init_app(app, db)

    # health check route
    @app.route("/")
    def health():
        return {"status": "Backend is running"}, 200

    # register blueprints
    app.register_blueprint(api_bp, url_prefix="/iammafah")
    app.register_blueprint(csv_bp, url_prefix="/iammafah")
    app.register_blueprint(xlsx_bp, url_prefix="/iammafah")
    app.register_blueprint(pdf_bp, url_prefix="/iammafah")

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
