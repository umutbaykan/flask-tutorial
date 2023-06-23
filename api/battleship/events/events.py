from flask_socketio import SocketIO, emit, join_room, leave_room, send
from flask import request, session
from ..utils.extensions import socketio
from ..utils.room_object import *


@socketio.on("connect")
def connect():
    print("client connected")
    emit("current_games", ROOMS, broadcast=True)


@socketio.on("disconnect")
def disconnected():
    """event listener when client disconnects to the server"""
    print("client disconnected")
    # emit("disconnect",f"user {request.sid} disconnected",broadcast=True)


@socketio.on("join")
def on_join(room):
    user_id = session.get("user_id")   
    username = session.get("username")
    session["room"] = room
    if not room_event_is_from_users_within_room_object(room, user_id):
        return
    join_room(room)
    print(f"{username} has joined {room}")
    emit("user_joined", {"room": room, "username": username}, to=room)


@socketio.on('leave')
def on_leave(room):
    user_id = session.get("user_id")
    username = session.get("username")
    if not room_event_is_from_users_within_room_object(room, user_id):
        return
    leave_room(room)
    session["room"] = ""
    print(f"{username} has left {room}")
    emit("user_left", {"room": room, "username": username}, to=room)


@socketio.on('chat')
def handle_message(data):
    """event listener when client types a message"""
    username = session.get("username")
    user_id = session.get("user_id")   
    message = data.get("message")
    room = data.get("room")
    if not room_event_is_from_users_within_room_object(room, user_id, message):
        return
    emit("chat_update", {"username": username, "message": message}, to=room)


@socketio.on("create-something")
def handle_something(data):
    print(session.get("room"))
    emit("respond-something", {"response": data}, broadcast=True)


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
