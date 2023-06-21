from flask import (Blueprint, make_response, session, jsonify, request)

from .auth import login_required
from ..utils.extensions import socketio
from ..utils.room_object import *
from ..database.db import check_if_room_id_is_unique
from ..helpers.helpers import generate_unique_code

bp = Blueprint('room', __name__, url_prefix='/room')

@bp.route('/create', methods=['POST'])
@login_required
def create_room():
  while True:
    room_id = generate_unique_code()
    if (check_if_room_id_is_unique(room_id) and check_global_room_id_is_unique(room_id)):
      break
  session['room'] = room_id
  create_new_game_state(session['room'], {"gamestate": "someconfigs"})
  add_player_to_game(session['room'], session['user_id'])

  # Sends the updated list of games to the lobby
  socketio.emit('current_games', list_all_rooms())
  return make_response({'room': session['room']}, 200)

@bp.route('/join', methods=['POST'])
@login_required
def join_room():
  data = request.json
  if 'room' in session:
      del session['room']
  session['room'] = data['room']
  if add_player_to_game(session['room'], session['user_id']):
    return {}, 200
  else:
    return make_response({"error": "Room is full"}, 409)
  
  
@bp.route('/leave', methods=["GET"])
def leave_room():
  if 'room' in session:
      del session['room']
  return {}, 200
  

@bp.route('/list', methods=['GET'])
def list_rooms():
  return make_response(list_all_rooms(), 200)