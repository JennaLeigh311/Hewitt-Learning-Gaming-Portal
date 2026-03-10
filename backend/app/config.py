import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:

    # Secret key for session signing and CSRF protection
    # CSRF (Cross‑Site Request Forgery) is basically an attack that tricks a user's browser
    # into making unwanted authenticated requests. Keep this key
    # secret (in your local .env) and use CSRF tokens or token-based auth for protected routes
    SECRET_KEY = os.getenv("SECRET_KEY", "change-me-in-production")

    # Database connection string (MariaDB via PyMySQL)
    # Set DATABASE_URL in .env
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "mysql+pymysql://root:@localhost:3306/edu_games"
    )

    # Disable SQLAlchemy event notification overhead
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Domain where game files are hosted 
    # TODO: change this once we get more info from Hewitt
    GAME_HOST_DOMAIN = os.getenv("GAME_HOST_DOMAIN", "games.yourdomain.com")

    # Frontend origin
    FRONTEND_ORIGIN = os.getenv("FRONTEND_ORIGIN", "http://localhost:3000")


class DevelopmentConfig(Config):
    # Dev specific settings
    DEBUG = True


class ProductionConfig(Config):
    # Production specific settings
    DEBUG = False


class TestingConfig(Config):
    # Testing-specific settings
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"


# Map config names to classes for easy lookup
config_by_name = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig,
}
