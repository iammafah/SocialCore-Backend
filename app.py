from flask import Flask
from flask_cors import CORS
from database.db import db, migrate
from config import Config
from routes.api import api_bp


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

    return app


app = create_app()

if __name__ == "__main__":
    app.run()
