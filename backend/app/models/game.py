# Game model, represents one game on the portal
import uuid
from app.models import db

# TODO: review with everyone whether we all agree with this database model
class Game(db.Model):
    __tablename__ = "games"

    # Use a UUID string as primary key
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))

    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    subject = db.Column(db.String(100), nullable=False)
    grade_level = db.Column(db.String(50), nullable=False)
    thumbnail_url = db.Column(db.String(500), nullable=True)
    game_url = db.Column(db.String(500), nullable=False)
    is_active = db.Column(db.Boolean, default=True, nullable=False)

    def to_dict(self) -> dict:
        # Serializing the game to a JSON-safe dictionaru
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "subject": self.subject,
            "grade_level": self.grade_level,
            "thumbnail_url": self.thumbnail_url,
            "game_url": self.game_url,
            "is_active": self.is_active,
        }

    def __repr__(self):
        return f"<Game {self.title}>"
