from flask import (Blueprint, make_response, session, jsonify, request)

from .auth import login_required
from .extensions import socketio
from .events import create_new_game_state, list_all_rooms, add_player_to_game
from .helpers import generate_unique_code

bp = Blueprint('room', __name__, url_prefix='/room')

@bp.route('/create', methods=['POST'])
@login_required
def create_room():
  session['room'] = generate_unique_code()
  create_new_game_state(session['room'], {"gamestate": "someconfigs"})
  add_player_to_game(session['room'], session['user_id'])

  # Sends the updated list of games to the lobby
  socketio.emit('current_games', list_all_rooms())
  return make_response({'room': session['room']}, 200)

@bp.route('join', methods=['POST'])
@login_required
def join_room():
  data = request.json
  if 'room' in session:
      del session['room']
  session['room'] = data['room']
  add_player_to_game(session['room'], session['user_id'])
  return make_response({}, 200)

@bp.route('/list', methods=['GET'])
def list_rooms():
  return make_response(list_all_rooms(), 200)