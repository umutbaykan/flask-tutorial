from . import db
from werkzeug.local import LocalProxy
from flask_pymongo import PyMongo

from bson.objectid import ObjectId

db = LocalProxy(db.get_db)


def get_user_by_username(name):
    """
    Returns the user with the given username
    """
    response = db.users.find_one({"username": name})
    return response


def get_user_by_id(id):
    """
    Returns the user with the ID
    """
    response = db.users.find_one({"_id": ObjectId(id)})
    return response


def register_user(username, password):
    """
    Registers a user in DB. Throws an error if username already exists.
    """
    existing_user = get_user_by_username(username)
    if existing_user:
        raise ValueError("Username already exists")
    else:
        result = db.users.insert_one({"username": username, "password": password})
        return str(result.inserted_id)


def add_game_to_user_history(user_id, game_id):
    """
    Registers a game_id in user's games. Only invoked if the game has already started.
    """
    response = db.users.find_one_and_update({'_id': user_id}, {'$push': {'games': game_id}})
    return response