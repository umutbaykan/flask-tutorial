from flask import Blueprint, make_response, session, jsonify, request

from .auth import login_required
from ..utils.extensions import socketio
from ..utils.room_object import *
from ..database.db import check_if_room_id_is_unique
from ..helpers.helpers import generate_unique_code

bp = Blueprint("room", __name__, url_prefix="/room")


@bp.route("/create", methods=["POST"])
@login_required
def create_room():
    """
    Generates a unique ID for a game
    Adds the creating player to the game object.
    Returns the room ID as a JSON object
    """
    while True:
        room_id = generate_unique_code()
        if check_if_room_id_is_unique(room_id) and check_global_game_id_is_unique(
            room_id
        ):
            break
    create_new_game_state(room_id, {"gamestate": "someconfigs"})
    add_player_to_game(room_id, session["user_id"])

    # Sends the updated list of games to the lobby
    socketio.emit("current_games", list_all_rooms())
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
    return make_response(list_all_rooms(), 200)
