from flask import (Blueprint, make_response, jsonify)

from bson import json_util
from . import db

bp = Blueprint('response', __name__, url_prefix='/response')

@bp.route('/', methods=['GET'])
def response():
  headers = {"Content-Type": "application/json"}
  return make_response(jsonify({'did it':'it worked!'}), 200, headers)

@bp.route('/getme', methods=['GET'])
def get_user():
  headers = {"Content-Type": "application/json"}
  print(db.db.list_collection_names())
  return make_response(json_util.dumps(db.get_user()), 200, headers)

@bp.route('/putme', methods=['POST'])
def put_user():
  headers = {"Content-Type": "application/json"}
  insertion = {"name": "Jim", "password": "552", "email":"pythonic" }
  db.db["users"].insert_one(insertion)
  return make_response(json_util.dumps(db.get_user()), 200, headers)

@bp.route('/drop', methods=['GET'])
def drop_users():
  response = db.db["users"].drop()
  return response

@bp.route('/remove', methods=['DELETE'])
def remove_user():
  query = {"name": "Jim"}
  response = db.db["users"].delete_one(query)
  return str(response)

@bp.route('/update', methods=['PATCH'])
def update_user():
  query = {"name": "Jim"}
  new_values = { "$set" : {"email": "updated@"}}
  response = db.db["users"].update_one(query, new_values)
  return str(response)