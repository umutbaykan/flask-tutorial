import json
from flask import g, session
from battleship.utils.room_object import ROOMS


def test_successful_room_creation(client, auth):
    with client:
        auth.login()
        response = client.post("/room/create")
        data = json.loads(response.data.decode("utf-8"))
        assert response.status_code == 200
        assert len(session["user_id"]) == 24
        assert len(ROOMS[data["room"]]["players"]) > 0


def test_unlogged_room_creation(client):
    response = client.post("/room/create")
    data = json.loads(response.data.decode("utf-8"))
    assert "error" in data
    assert response.status_code == 401


def test_successful_room_join(client, auth):
    ROOMS["manuallycreated"] = {"players": ["I_was_here"]}
    data = {"room": "manuallycreated"}
    with client:
        auth.login()
        client.post(
            "/room/join", data=json.dumps(data), content_type="application/json"
        )
        assert len(ROOMS["manuallycreated"]["players"]) == 2


def test_joining_a_full_room(client, auth):
    ROOMS["manuallycreated"] = {"players": ["I_was_here", "so_was_i"]}
    data = {"room": "manuallycreated"}
    with client:
        auth.login()
        response = client.post(
            "/room/join", data=json.dumps(data), content_type="application/json"
        )
        message = json.loads(response.data.decode("utf-8"))
        assert len(ROOMS["manuallycreated"]["players"]) == 2
        assert response.status_code == 409
        assert message["error"] == "Room is full"


def test_unlogged_room_join(client):
    response = client.post("/room/create")
    data = json.loads(response.data.decode("utf-8"))
    assert "error" in data
    assert response.status_code == 401
