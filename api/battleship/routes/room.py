from flask import Blueprint, make_response, session, request

from .auth import login_required
from ..utils.extensions import socketio
from ..utils.room_object import ROOMS
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
    ROOMS[room_id] = new_game
    
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
    room = request.json["room"]  
    response = add_player_to_game(room, session["user_id"])
    if response == True:
        session["room"] = room
        return {}, 200
    else:
        return make_response({"error": response["error"]}, 400)
    

@bp.route("/available", methods=["GET"])
def list_all_rooms_in_lobby():
    """
    Retrieves a list of available games and sends it as a JSON.
    JSON is formatted to reflect the host, game ID and configurations.
    Availability is determined on how many players are currently in the game object.
    """
    return make_response(list_all_available_rooms(), 200)


### Development methods - To be removed later
@bp.route("/list", methods=["GET"])
def list_rooms():
    return make_response(get_all_room_data(), 200)


def get_all_room_data():
    all_serialized_data = {}
    for game_id, game in ROOMS.items():
        all_serialized_data[game_id] = Game.serialize(game)
    return all_serialized_data