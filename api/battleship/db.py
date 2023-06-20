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


def seed_test_database(collection, seed_data):
    """
    Reseeds the database based on the JSON data in seeds folder
    """
    db[collection].drop()
    db[collection].insert_many(seed_data)