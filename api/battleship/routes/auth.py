import functools

from flask import Blueprint, g, request, session, make_response
from werkzeug.security import check_password_hash, generate_password_hash

from ..database.user import *

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/register", methods=["POST"])
def register():
    """
    Registers a new user and sets their id inside session
    Returns 200 if successful or a 400 error with a JSON
    object containing the error message
    """
    data = request.json
    username = data["username"]
    password = data["password"]
    error = None

    if not username:
        error = "Username is required."
    elif not password:
        error = "Password is required."
    elif len(password) < 8:
        error = "Password is too short"
    elif len(username) > 15:
        error = "Username is too long"

    if error is None:
        try:
            new_user_id = register_user(username, generate_password_hash(password))
        except ValueError as err:
            error = str(err)
        else:
            session.clear()
            session["user_id"] = new_user_id
            session["username"] = username
            return {}, 201

    return make_response({"error": error}, 400)


@bp.route("/login", methods=["POST"])
def login():
    """
    Logs in a user and sets their id inside session
    Returns 200 if successful or a 400 error with a JSON
    object containing the error message
    """
    data = request.json
    username = data["username"]
    password = data["password"]
    error = None

    user = get_user_by_username(username)

    if user is None:
        error = "Incorrect username."
    elif not check_password_hash(user["password"], password):
        error = "Incorrect password."

    if error is None:
        session.clear()
        session["user_id"] = str(user["_id"])
        session["username"] = user["username"]
        return {"user_id": session["user_id"]}, 200

    return make_response({"error": error}, 400)


@bp.before_app_request
def load_logged_in_user():
    """
    Retrieves the user data from db and assigns it to
    g object before each request
    """
    user_id = session.get("user_id")
    if user_id is None:
        g.user = None
    else:
        g.user = get_user_by_id(user_id)


@bp.route("/logout")
def logout():
    """
    Logs the user out and clears the session
    """
    session.clear()
    return {}, 204


def login_required(view):
    """
    Wrapper function to protect routes
    """

    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return make_response({"error": "You need to login."}, 401)
        return view(**kwargs)

    return wrapped_view
