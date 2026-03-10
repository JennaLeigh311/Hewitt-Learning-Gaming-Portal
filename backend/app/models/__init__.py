# Database models package
# Exports the shared SQLAlchemy instance and all model classes
from flask_sqlalchemy import SQLAlchemy

# Shared SQLAlchemy instance, initialized in the app factory
db = SQLAlchemy()

# Import models so they're registered with SQLAlchemy
from app.models.game import Game
