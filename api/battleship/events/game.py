from flask_socketio import emit
from flask import session
from ..utils.extensions import socketio
from ..utils.room_object import PLAYERS, ROOMS
from ..utils.helpers import fetch_game, validate_user_and_game


@socketio.on("place_ships")
def on_place_ships(ship_positions):
    # game = validate_user_and_game(room)
    pass

@socketio.on("update")
def on_update():
    pass

@socketio.on("fire")
def on_fire():
    pass

@socketio.on("game_over")
def on_game_over():
    pass

