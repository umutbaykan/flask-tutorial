from . import db
from werkzeug.local import LocalProxy
from flask_pymongo import PyMongo

from bson.objectid import ObjectId

db = LocalProxy(db.get_db)


def get_game_by_game_id(game_id):
    """
    Returns the game with the given game ID
    """
    response = db.games.find_one({"game_id": game_id})
    return response


def create_game(serialized_game):
    """
    Creates the game in the database as an object
    """
    response = db.games.insert_one(serialized_game)
    return response


def save_game(serialized_game):
    game_id, turn, boards, who_won = (
        serialized_game.get("game_id"),
        serialized_game.get("turn"),
        serialized_game.get("boards"),
        serialized_game.get("who_won"),
    )
    response = db.games.update_one(
        {"game_id": game_id}, {"$set": {"turn": turn, "boards": boards, "who_won": who_won}}
    )
    return response

