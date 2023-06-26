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