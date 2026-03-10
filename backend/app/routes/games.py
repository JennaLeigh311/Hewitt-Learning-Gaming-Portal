# Public game routes (read-only endpoints for the frontend portall)
from flask import Blueprint, jsonify, request
from app.models import db
from app.models.game import Game

games_bp = Blueprint("games", __name__)

@games_bp.route("/games", methods=["GET"])
def get_games():
    """
    GET /api/games
    Returns a list of active games.
    Optional query params:
        - subject: filter by subject (e.g. ?subject=Math)
        - grade:   filter by grade level (e.g. ?grade=K-2)
        - search:  search title/description (e.g. ?search=fraction)
    """
    # TODO: fill this in


@games_bp.route("/games/<string:game_id>", methods=["GET"])
def get_game(game_id: str):
    """
    GET /api/games/<id>
    Returns a single game by its ID.
    404 if not found or inactive.
    """
    # TODO: fill this in