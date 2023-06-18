from flask_socketio import SocketIO, emit
from flask import request
from .extensions import socketio

@socketio.on("connect")
def connected():
    """event listener when client connects to the server"""
    print("client has connected")
    # emit("connect",{"data":f"id: {request.sid} is connected"})

@socketio.on('data')
def handle_message(data):
    """event listener when client types a message"""
    print("data from the front end: ",str(data))
    emit("data",{'data':data,'id':request.sid},broadcast=True)

@socketio.on('create-something')
def handle_something(data):
    emit('respond-something', {'response': data}, broadcast=True)
    
@socketio.on("disconnect")
def disconnected():
    """event listener when client disconnects to the server"""
    print("user disconnected")
    emit("disconnect",f"user {request.sid} disconnected",broadcast=True)