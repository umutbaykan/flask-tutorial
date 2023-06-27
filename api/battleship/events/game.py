from flask_socketio import emit
from flask import session
from ..models.game import Game
from ..utils.extensions import socketio
from ..utils.room_object import PLAYERS, ROOMS
from ..utils.helpers import fetch_game, validate_user_and_game


@socketio.on("place_ships")
def on_place_ships(data):
    room = data.get("room")
    ship_positions = data.get("ships")
    game = validate_user_and_game(room)
    if not game:
        return
    user_id = session.get("user_id")
    ships = ship_positions["ships"]
    result = game.place_ships(user_id, ships)
    if result is True:
        emit('update', {"game": Game.serialize(game)}, to=room)
    else:
        emit('error', result, to=room)


@socketio.on("update")
def on_update():
    pass

@socketio.on("fire")
def on_fire():
    pass

@socketio.on("game_over")
def on_game_over():
    pass

