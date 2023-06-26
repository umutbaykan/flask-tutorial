from flask import (
    Blueprint,
    make_response,
    jsonify,
    request,
    url_for,
    redirect,
    render_template,
    session,
)
import json
from bson import json_util, ObjectId
from .database.game import *
from .database.user import get_user_by_id
from .routes.auth import login_required
from .utils.helpers import generate_unique_code
from flask_socketio import join_room, leave_room, send, SocketIO

bp = Blueprint("response", __name__, url_prefix="/")


@bp.route("/callme", methods=["GET"])
def call():
    data = get_game_by_game_id("aFKeajFE")
    return data


@bp.route("/whereami")
def find_my_room():
    room = session.get("room")
    user_id = session.get("user_id")
    if user_id:
        username = db.get_user_by_id(user_id)["username"]
    else:
        username = ""
    response = make_response({"room": room, "user_id": user_id, "username": username}, 200)
    response.headers["Content-Type"] = "application/json"
    return response


@bp.route("/createroom", methods=["POST"])
def create_room():
    if session.get("user_id") is None:
        error_message = "You need to be signed in to create a room"
        print(error_message)
        response = make_response(json.dumps({"error": error_message}), 400)
    else:
        session["room"] = generate_unique_code()
        print(f"Your new room name is going to be {session['room']}")
        response = make_response(json.dumps({"room": session["room"]}), 200)
    response.headers["Content-Type"] = "application/json"
    return response


@bp.route("/joinroom", methods=["POST"])
def join_room():
    data = request.json
    room = data["room"]
    if room is None:
        error_message = "You need to specify a room name to join"
        print(error_message)
        response = make_response(json.dumps({"error": error_message}), 400)
    else:
        session["room"] = room
        response = make_response(json.dumps({"room": session["room"]}), 200)
    response.headers["Content-Type"] = "application/json"
    return response


@bp.route("/someroom", methods=["GET"])
def what_room():
    print(session.get("user_id"))
    return {"your user_id is": session.get("user_id")}


@bp.route("/manualseed", methods=["GET"])
def seed_stuff():
    db.seed_test_database(
        "users", [{"name": "Jason", "email": "hisemail"}, {"name": "Roger"}]
    )
    return "ok!"


@bp.route("/getme", methods=["GET"])
def get_user():
    data = request.json
    headers = {"Content-Type": "application/json"}
    return make_response(
        json_util.dumps(db.get_user_by_username(data["username"])), 200, headers
    )


@bp.route("/getgame", methods=["GET"])
def get_game():
    headers = {"Content-Type": "application/json"}
    return make_response({}, 200, headers)


@bp.route("/check")
# @login_required
def check():
    headers = {"Content-Type": "application/json"}
    data = request.json
    user = get_user_by_id(data["user_id"])
    name = user["username"]
    return {"data": name}


@bp.route("/putme", methods=["POST"])
def put_user():
    headers = {"Content-Type": "application/json"}
    insertion = {"name": "Jim", "password": "552", "email": "pythonic"}
    db.db["users"].insert_one(insertion)
    return make_response(json_util.dumps(db.get_user()), 200, headers)


@bp.route("/putgame", methods=["POST"])
def put_game():
    headers = {"Content-Type": "application/json"}
    insertion = {"game": 1}
    operation = db.insert_game(insertion)
    return make_response(str(operation), 200, headers)


@bp.route("/drop", methods=["GET"])
def drop_users():
    response = db.db["users"].drop()
    return response


@bp.route("/remove", methods=["DELETE"])
def remove_user():
    query = {"name": "Jim"}
    response = db.db["users"].delete_one(query)
    return str(response)


@bp.route("/update", methods=["PATCH"])
def update_user():
    query = {"name": "Jim"}
    new_values = {"$set": {"email": "updated@"}}
    response = db.db["users"].update_one(query, new_values)
    return str(response)
