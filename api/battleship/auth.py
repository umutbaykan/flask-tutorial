import functools

from flask import (
    Blueprint, g, request, session, make_response
)
from werkzeug.security import check_password_hash, generate_password_hash

from . import db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data['username']
    password = data['password']
    error = None

    if not username:
        error = 'Username is required.'
    elif not password:
        error = 'Password is required.'
    elif len(password) < 8:
        error = 'Password is too short'

    if error is None:
        try:
            db.register_user(username, generate_password_hash(password))
        except ValueError as err:
            error = str(err)
        else:
            return make_response({}, 201)

    return make_response({"error": error}, 400)


@bp.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data['username']
    password = data['password']
    error = None

    user = db.get_user_by_username(username)

    if user is None:
        error = 'Incorrect username.'
    elif not check_password_hash(user['password'], password):
        error = 'Incorrect password.'

    if error is None:
        session.clear()
        session['user_id'] = str(user['_id'])
        print(f"Someone logged in. Their user id is {session['user_id']}. This is stored in the session object now.")
        return make_response({}, 200)
    
    return make_response({"error": error}, 400)


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = db.get_user_by_id(user_id)


@bp.route('/logout')
def logout():
    print(f"{session.get('user_id')} was logged in.")
    session.clear()
    print(f"They are now logged out. The next line should be none to verify session is cleared")
    print(f"{session.get('user_id')}")
    return make_response({}, 204)

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return make_response({"error": "You need to login"}, 400)
        return view(**kwargs)

    return wrapped_view
