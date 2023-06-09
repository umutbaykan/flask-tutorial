import os

from flask import Flask
from flask_cors import CORS
from .routes import auth, room
from .events.room import socketio
from .events.game import socketio
from .utils.extensions import sess


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev", 
        MONGO_URI="mongodb://0.0.0.0/battleship",
        SESSION_TYPE="filesystem"
        )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        print("Launching on overridden (test) settings")
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.register_blueprint(auth.bp)
    app.register_blueprint(room.bp)
    CORS(app, supports_credentials=True)
    sess.init_app(app)
    socketio.init_app(app)
    return app
