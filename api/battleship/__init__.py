import os

from flask import Flask
from flask_cors import CORS
from . import thingy
from .routes import auth, room
from .events.events import socketio


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY="dev", MONGO_URI="mongodb://0.0.0.0/battleship")

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
    app.register_blueprint(thingy.bp)
    CORS(app, supports_credentials=True)
    socketio.init_app(app)
    return app


app = create_app()

if __name__ == "__main__":
    socketio.run(app)
