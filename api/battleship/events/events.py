from flask_socketio import SocketIO, emit, join_room, leave_room, send
from flask import request, session
from ..utils.extensions import socketio
from ..utils.room_object import *


# @socketio.on("connect")
# def connected():
#     """event listener when client connects to the server"""
#     print("client has connected")
#     print(session.get('user_id', False))
#     print(session.get('room'))
#     # print(request.sid)
#     # # emit("connect",{"data":f"id: {request.sid} is connected"})


@socketio.on("data")
def handle_message(data):
    """event listener when client types a message"""
    print("data from the front end: ", str(data))
    emit("data", {"data": data, "id": request.sid}, broadcast=True)


@socketio.on("create-something")
def handle_something(data):
    print(session.get("room"))
    emit("respond-something", {"response": data}, broadcast=True)


# @socketio.on("disconnect")
# def disconnected():
#     """event listener when client disconnects to the server"""
#     print("user disconnected")
#     emit("disconnect",f"user {request.sid} disconnected",broadcast=True)


@socketio.on("foo")
def handle_something(data):
    message = f"Someone triggered the foo event with {data}. This message should only be seen by people in the room"
    room = session.get("room")
    # send(message, to=room)
    emit("foo", {"response": message}, room=room, include_self=False)


# @socketio.on("connect")
# def connect():
#     room = session.get("room")
#     user_id = session.get("user_id")
#     # if not room or not user_id:
#     #     return
#     # if room not in rooms:
#     #     leave_room(room)
#     #     return

#     join_room(room)
#     # send({"id": user_id, "message": "has entered the room"})
#     # rooms[room].get("members", 0) + 1
#     # print(f"{user_id} joined room {room}")
#     send(f"{user_id} joined room {room}", to=room)


@socketio.on("connect")
def connect():
    emit("current_games", ROOMS, broadcast=True)


# @socketio.on("disconnect")
# def disconnect():
#     room = session.get("room")
#     user_id = session.get("user_id")
#     leave_room(room)

#     # if room in rooms:
#     #     rooms[room]["members"] -= 1
#     #     if rooms[room]["members"] <= 0:
#     #         del rooms[room]

#     # send({"name": name, "message": "has left the room"}, to=room)
#     # print(f"{user_id} has left the room {room}")
#     send(f"{user_id} has left the room {room}", to=room)
