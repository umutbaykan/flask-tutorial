from flask_socketio import SocketIO 

socketio = SocketIO(cors_allowed_origins="*", manage_session=True, 
                    engineio_logger=True, logger=True)