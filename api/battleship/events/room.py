from flask_socketio import emit, join_room, leave_room, close_room
from flask import session, request
from ..models.game import Game
from ..utils.extensions import socketio
from ..utils.room_object import PLAYERS, ROOMS
from ..utils.helpers import save_game_state, validate_user_and_game, list_all_available_rooms


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
    masked_game_info = Game.hide_board_info(Game.serialize(game), session.get("user_id"), opponent=True)
    emit("update", {"game": masked_game_info}, to=request.sid)
    emit("user_joined", {"room": room, "username": username}, to=room)
    emit("current_games", list_all_available_rooms(), broadcast=True)


@socketio.on('leave')
def on_leave(room):
    username = session.get("username")
    game = validate_user_and_game(room)
    if not game:
        return
    leave_room(room)
    emit("user_left", {"room": room, "username": username}, to=room)
    if game.who_won:
        save_game_state(Game.serialize(game))
        del ROOMS[room]
        close_room(room)
    else:
        game.remove_player(session.get("user_id"))
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
