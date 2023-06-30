from flask import Blueprint, make_response, session, request

from .auth import login_required
from ..utils.extensions import socketio
from ..utils.room_object import ROOMS
from ..utils.helpers import *
from ..models.game import Game
from ..database.game import get_game_by_game_id, get_user_game_history

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
    ROOMS[room_id] = new_game
    # # Sends the updated list of games to the lobby
    socketio.emit("current_games", list_all_available_rooms())
    return make_response({"room": room_id}, 200)


@bp.route("/join", methods=["POST"])
@login_required
def join_room():
    """
    Adds the joinng player to the game object
    Returns an error if the game state has two players already
    """
    room = request.json["room"]  
    response = add_player_to_game(room, session["user_id"])
    if response == True:
        return {}, 200
    else:
        return make_response({"error": response["error"]}, 400)
    

@bp.route("/load", methods=["POST"])
@login_required
def load_game():
    room = request.json["room"]
    player = session.get("user_id")
    game = get_game_by_game_id(room)
    if not game:
        return make_response({"error": "No such game to load."}, 400)
    
    if player not in game["players"]:
        return make_response({"error": "You are not a player in this game."}, 400)

    ROOMS[room] = Game.deserialize(game)
    return {}, 200


@bp.route("/load_check", methods=["GET"])
@login_required
def load_check():
    player = session.get("user_id")
    return make_response(list_load_games(player), 200)


@bp.route("/load_history")
@login_required
def load_game_history():
    player = session.get("user_id")
    result = get_user_game_history(player)
    return make_response(list(result), 200)


### Development methods - To be removed later
@bp.route("/list", methods=["GET"])
def list_rooms():
    return make_response(get_all_room_data(), 200)


def get_all_room_data():
    all_serialized_data = {}
    for game_id, game in ROOMS.items():
        all_serialized_data[game_id] = Game.serialize(game)
    return all_serialized_data