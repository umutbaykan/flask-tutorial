from flask_socketio import emit, join_room, leave_room, close_room
from flask import session
from ..utils.extensions import socketio
from ..utils.room_object import PLAYERS, ROOMS
from ..utils.helpers import fetch_game, validate_user_and_game, list_all_available_rooms


@socketio.on("connect")
def connect():
    print("Client connected.")
    PLAYERS["online_users"] = PLAYERS.get("online_users") + 1
    emit("current_games", list_all_available_rooms(), broadcast=True)


@socketio.on("disconnect")
def disconnect():
    print("client disconnected")
    PLAYERS["online_users"] = PLAYERS.get("online_users") - 1


@socketio.on("join")
def on_join(room):   
    username = session.get("username")
    if not validate_user_and_game(room):
        return
    join_room(room)
    emit("user_joined", {"room": room, "username": username}, to=room)


@socketio.on('leave')
def on_leave(room):
    username = session.get("username")
    if not validate_user_and_game(room):
        return
    game = fetch_game(room)
    game.remove_player(session.get("user_id"))
    leave_room(room)
    print(f"{username} has left {room}")
    emit("user_left", {"room": room, "username": username}, to=room)
    if game.players == []:
        del ROOMS[room]
        close_room(room)
        emit("current_games", list_all_available_rooms(), broadcast=True)

@socketio.on('chat')
def on_chat(data):
    """event listener when client types a message"""
    username = session.get("username")
    message = data.get("message")
    room = data.get("room")
    if not validate_user_and_game(room):
        return
    emit("chat_update", {"username": username, "message": message}, to=room)
