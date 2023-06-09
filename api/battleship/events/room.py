from flask_socketio import emit, join_room, leave_room, close_room
from flask import session, request
from ..models.game import Game
from .game import hide_and_emit_boards
from ..utils.extensions import socketio
from ..utils.room_object import PLAYERS, ROOMS
from ..utils.helpers import (
    save_game_state,
    validate_user_and_game,
    list_all_available_rooms,
)


@socketio.on("connect")
def connect():
    print("Client connected.")
    PLAYERS["online_users"] = PLAYERS.get("online_users") + 1
    emit("current_games", list_all_available_rooms(), broadcast=True)


@socketio.on("disconnect")
def disconnect():
    print("Client disconnected.")
    PLAYERS["online_users"] = PLAYERS.get("online_users") - 1


@socketio.on("join")
def on_join(room):
    username = session.get("username")
    game = validate_user_and_game(room)
    if not game:
        return
    join_room(room)
    hide_and_emit_boards(room, game)
    emit("user_joined", {"room": room, "username": username}, to=room)
    emit("current_games", list_all_available_rooms(), broadcast=True)


@socketio.on("leave")
def on_leave(room):
    username = session.get("username")
    user_id = session.get("user_id")
    game = validate_user_and_game(room)
    if not game:
        return
    leave_room(room)
    emit("user_left", {"room": room, "username": username}, to=room)

    if game.who_won or game.ready == True:
        if not game.who_won:
            emit(
                "chat_update",
                {
                    "username": "Server",
                    "message": "Your opponent has left an unfinished game. You can load this game later. Closing room now.",
                },
                to=room,
            )
        save_game_state(Game.serialize(game))
        del ROOMS[room]
        close_room(room)
    else:
        game.remove_player(user_id)
        if game.players == []:
            del ROOMS[room]
            close_room(room)
        emit("current_games", list_all_available_rooms(), broadcast=True)


@socketio.on("chat")
def on_chat(data):
    """event listener when client types a message"""
    username = session.get("username")
    message = data.get("message")
    room = data.get("room")
    if not validate_user_and_game(room):
        return
    emit("chat_update", {"username": username, "message": message}, to=room)
