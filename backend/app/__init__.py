from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate

from app.config import config_by_name
from app.models import db
from app.routes.games import games_bp
from app.routes.admin import admin_bp


# THis file is for creating and configuring the app

# Flask-Migrate instance (handles Alembic migrations)
migrate = Migrate()

"""
    Application factory.

    Args:
        config_name: One of 'development', 'production', or 'testing'.

    Returns:
        Configured Flask application instance.
"""
def create_app(config_name: str = "development") -> Flask:

    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    # Extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # CORS ( only allow requests from the frontend origin)
    CORS(app, origins=[app.config["FRONTEND_ORIGIN"]])

    # Blueprints
    app.register_blueprint(games_bp, url_prefix="/api")
    app.register_blueprint(admin_bp, url_prefix="/api/admin")

    # Security headers (applied to every response)
    @app.after_request
    def set_security_headers(response):

        game_host = app.config["GAME_HOST_DOMAIN"]
        response.headers["Content-Security-Policy"] = (
            f"default-src 'self'; frame-src {game_host};"
        )
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        return response

    return app
