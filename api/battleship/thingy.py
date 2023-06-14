from flask import (Blueprint, make_response, jsonify)

bp = Blueprint('response', __name__, url_prefix='/response')

@bp.route('/', methods=['GET'])
def response():
  headers = {"Content-Type": "application/json"}
  return make_response(jsonify({'did it':'it worked!'}), 200, headers)