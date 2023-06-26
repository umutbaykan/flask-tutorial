from flask import Blueprint, make_response, session, jsonify, request

from .auth import login_required
from ..utils.extensions import socketio
from ..utils.room_object import *
from ..database.db import *
from ..utils.helpers import *
from ..models.game import Game

bp = Blueprint("room", __name__, url_prefix="/room")


@bp.route("/create", methods=["POST"])
@login_required
def create_room():
    """
    Generates a unique ID for a game
    Creates a game object with the player in it.
    Adds the game object to the ongoing games.
    Returns the game_id as a JSON object
    """
    configs = request.json
    game_creator = session["user_id"]
    room_id = generate_unique_code()
    new_game = Game.create_new_game_from_configs(configs, server_allocated_room=room_id, game_creator=game_creator)
    ROOMS[room_id] = Game.serialize(new_game)
    
    # # Sends the updated list of games to the lobby
    socketio.emit("current_games", list_all_available_rooms())
    return make_response({"room": room_id}, 200)


@bp.route("/join", methods=["POST"])
@login_required
def join_room():
    """
    Sets the room in session object to the room_id received from request
    Adds the joinng player to the game object
    Returns an error if the game state has two players already
    """
    data = request.json        
    if add_player_to_game(data["room"], session["user_id"]):
        return {}, 200
    else:
        return make_response({"error": "Room is full"}, 409)


@bp.route("/list", methods=["GET"])
def list_rooms():
    return make_response(list_all_available_rooms(), 200)
