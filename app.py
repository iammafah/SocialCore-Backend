from flask import Flask, app
from flask_cors import CORS
from database.db import db, migrate
from config import Config
from routes.api import api_bp
from utils.exporters.csv_exporter import csv_bp
from utils.exporters.xlsx_exporter import xlsx_bp  # xlsx exporter
from utils.exporters.pdf_exporter import pdf_bp  # pdf exporter



def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app)  # 🔥 allow browser requests

    db.init_app(app)
    migrate.init_app(app, db)

    @app.route("/")
    def health():
        return {"status": "Backend is running"}, 200

    app.register_blueprint(
        api_bp,
        url_prefix="/iammafah"
    )
    app.register_blueprint(csv_bp,url_prefix="/iammafah")
    app.register_blueprint(xlsx_bp,url_prefix="/iammafah")
    app.register_blueprint(pdf_bp,url_prefix="/iammafah")

    return app


app = create_app()

if __name__ == "__main__":
    app.run()
