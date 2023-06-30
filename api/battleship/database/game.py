from . import db
from .user import get_user_by_id
from werkzeug.local import LocalProxy
from datetime import datetime

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
    serialized_game["last_modified"] = datetime.now()
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
        {"game_id": game_id},
        {"$set": {"turn": turn, "boards": boards, "who_won": who_won, "last_modified": datetime.now()}},
    )
    return response


def get_user_game_history(user_id):
    """
    Retrieves all the games user has played.
    """
    user = get_user_by_id(user_id)
    game_ids = user["games"]
    response = db.games.aggregate(
        [
            {"$match": {"game_id": {"$in": game_ids}}},
            {
                "$addFields": {
                    "player_ids": {
                        "$map": {
                            "input": "$players",
                            "as": "player",
                            "in": {"$toObjectId": "$$player"},
                        }
                    },
                },
            },
            {
                "$lookup": {
                    "from": "users",
                    "localField": "player_ids",
                    "foreignField": "_id",
                    "as": "players_info",
                    "pipeline": [{"$project": {"_id": 0, "username": 1}}],
                }
            },
            {"$project": {"_id": 0, "boards": 0, "player_ids": 0}},
            {"$sort": {"last_modified": -1}}
        ]
    )
    return response
