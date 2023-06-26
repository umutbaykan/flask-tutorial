from flask_socketio import emit
from flask import session
from ..utils.extensions import socketio
from ..utils.room_object import PLAYERS, ROOMS
from ..utils.helpers import fetch_game, validate_user_and_game


@socketio.on("place_ships")
def place_ships():
    pass

@socketio.on("update")
def update():
    pass

@socketio.on("fire")
def fire():
    pass

@socketio.on("game_over")
def game_over():
    pass

