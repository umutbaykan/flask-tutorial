import random
import string
from flask import session
from .room_object import ROOMS
from ..database.game import get_game_by_game_id, create_game, save_game
from ..database.user import get_user_by_id

def generate_unique_code():
    """
    Generates a unique code for the room
    """
    while True:
        characters = string.ascii_letters + string.digits
        code = "".join(random.choice(characters) for _ in range(8))
        if get_game_by_game_id(code) or code in ROOMS:
            code = ""
        else:
            return code


def validate_coordinate_input(coordinates):
    if type(coordinates) != list:
        raise ValueError("Invalid coordinate data type.")
    for coord in coordinates:
        if not isinstance(coord, list) or len(coord) != 2:
            raise ValueError("Invalid coordinate format. Expected [x, y] format.")
        if not all(isinstance(val, int) and val >= 0 for val in coord):
            raise ValueError(
                "Invalid coordinate value. Coordinates must be non-negative integers."
            )
        

def list_all_available_rooms():
    """Returns all the available games to join in the global room object"""
    available_games = {}
    for game_id, game in ROOMS.items():
        if len(game.players) < 2:
            user = get_user_by_id(game.players[0])
            username = user["username"] if user else "anonymous"
            available_games[game_id] = {"who_started": game.who_started, "allowed_ships": game.allowed_ships, "players": username}
    return available_games


def add_player_to_game(game, player_id):
    game = ROOMS.get(game)
    if game:
        return game.add_player(player_id)
    return {"error": "No game specified to join."}


def fetch_game(game_id):
    game = ROOMS.get(game_id)
    return game if game else None


def validate_user_and_game(room):
    user_id = session.get("user_id") 
    game = fetch_game(room)
    if not game or not game.is_player_valid(user_id):
        return False
    return game


def save_game_state(serialized_game):
    game = get_game_by_game_id(serialized_game.get("game_id"))
    if game is None:
        create_game(serialized_game)
    else:
        save_game(serialized_game)


def list_load_games(user_id):
    user = get_user_by_id(user_id)
    available_games = {}
    for game_id in user["games"]:
        if game_id in ROOMS:
            game = ROOMS[game_id]
            available_games[game_id] = {"game_id": game.game_id, "who_started": game.who_started, "turn": game.turn, "last_modified": game.last_modified, "players": game.players}
    return available_games
