from flask_socketio import emit
from flask import session, request
from ..models.game import Game
from ..utils.extensions import socketio
from ..utils.helpers import validate_user_and_game, save_game_state


@socketio.on("place_ships")
def on_place_ships(data):
    room = data.get("room")
    ship_positions = data.get("ships")
    game = validate_user_and_game(room)
    if not game:
        return
    user_id = session.get("user_id")
    ships = ship_positions["ships"]
    game.remove_player_ships(user_id)
    result = game.place_ships(user_id, ships)
    if result is True:
        hide_and_emit_boards(room, game)
    else:
        emit("error", result, to=request.sid)


@socketio.on("fire")
def on_fire(data):
    room = data.get("room")
    coordinates = data.get("coordinates")
    user_id = session.get("user_id")

    game = validate_user_and_game(room)
    if not game or not coordinates:
        return

    player_turn = game.is_player_turn(user_id)
    if not player_turn:
        emit("error", {"error": "Not your turn to shoot."}, to=request.sid)
        return

    game.fire(coordinates)
    save_game_state(Game.serialize(game))

    if game.is_over():
        emit("update", {"game": Game.serialize(game)}, to=room)
    else:
        hide_and_emit_boards(room, game)


def hide_and_emit_boards(room, game):
    masked_opponent_board = Game.hide_board_info(
        Game.serialize(game), session.get("user_id"), opponent=True
    )
    emit("update", {"game": masked_opponent_board}, to=request.sid)
    masked_my_board = Game.hide_board_info(Game.serialize(game), session.get("user_id"))
    emit("update", {"game": masked_my_board}, to=room, include_self=False)
