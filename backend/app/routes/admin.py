# Admin routes ( protected endpoints for managing the game cportal)
# TODO: Authentication/authorization will be added later
from flask import Blueprint, jsonify, request
from app.models import db
from app.models.game import Game

admin_bp = Blueprint("admin", __name__)

# Required fields when creating a new game (suggestion)
REQUIRED_FIELDS = ["title", "subject", "grade_level", "game_url"]


@admin_bp.route("/games", methods=["POST"])
def create_game():
    """
    POST /api/admin/games
    Creates a new game entry.
    Expects JSON body with at least: title, subject, grade_level, game_url.
    """
    # TODO: fill this in


@admin_bp.route("/games/<string:game_id>", methods=["PUT"])
def update_game(game_id: str):
    """
    PUT /api/admin/games/<id>
    Updates an existing game. Accepts partial updates.
    """
    # TODO: Fill thisin 


@admin_bp.route("/games/<string:game_id>", methods=["DELETE"])
def delete_game(game_id: str):
    """
    DELETE /api/admin/games/<id>
    Soft-deletes a game by setting is_active to False.
    """
    # TODO : fill this in
