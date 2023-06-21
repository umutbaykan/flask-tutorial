import pytest
import json
from flask import g, session
from battleship.utils.room_object import ROOMS

def test_successful_room_creation(client, auth):
    with client:
        auth.login()
        response = client.post('/room/create')
        assert response.status_code == 200
        assert len(session['user_id']) == 24
        assert 'room' in session
        assert len(ROOMS[session['room']]['players']) > 0

def test_unsuccessful_room_creation(client):
    response = client.post('/room/create')
    data = json.loads(response.data.decode('utf-8')) 
    assert 'error' in data

def test_successful_room_join(client, auth):
    ROOMS['manuallycreated'] = {"players":['I_was_here']}
    data={'room': 'manuallycreated'}
    with client:
        auth.login()
        response = client.post(
        '/room/join', data=json.dumps(data), content_type='application/json'
        )
        assert len(ROOMS['manuallycreated']['players']) == 2

def test_unsuccessful_room_join(client):
    response = client.post('/room/create')
    data = json.loads(response.data.decode('utf-8')) 
    assert 'error' in data


        
    