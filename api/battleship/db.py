from bson import json_util

from flask import current_app, g
from werkzeug.local import LocalProxy
from flask_pymongo import PyMongo

from pymongo.errors import DuplicateKeyError, OperationFailure
from bson.objectid import ObjectId
from bson.errors import InvalidId


def get_db():
    """
    Configuration method to return db instance
    """
    db = getattr(g, "_database", None)

    if db is None:
        connection = PyMongo(current_app)
        db = g._database = connection.db
       
    return db

# Use LocalProxy to read the global db instance with just `db`
db = LocalProxy(get_db)

def get_user():
    response = db.users.find_one({"name": "Jonathan"})
    return response

def get_game():
    response = db.games.find_one({"game": 1})
    return response

def insert_game(game):
    response = db.games.insert_one(game)
    return response.acknowledged

def seed_test_database(collection, seed_data):
    db[collection].drop()
    db[collection].insert_many(seed_data)