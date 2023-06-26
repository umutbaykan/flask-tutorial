from flask_socketio import SocketIO
from flask_session import Session

socketio = SocketIO(
    cors_allowed_origins="*", manage_session=False, engineio_logger=True, logger=True
)

sess = Session()
