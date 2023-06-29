import pytest
import json
import os
from flask import g, session
from battleship.utils.room_object import ROOMS
from battleship.models.game import Game


@pytest.fixture
def read_json(request):
    configs = request.param
    test_directory = os.path.dirname(os.path.abspath(__file__))
    json_file_path = os.path.join(
        test_directory, ".", "seeds", "model_objects", f"{configs}.json"
    )
    with open(json_file_path) as file:
        yield file


@pytest.mark.parametrize("read_json", ["game_regular_configs"], indirect=["read_json"])
def test_successful_room_creation(client, auth, read_json):
    with client:
        auth.login()
        response = client.post(
            "/room/create", data=read_json, content_type="application/json"
        )
        assert response.status_code == 200
        for game_id, v in ROOMS.items():
            id_of_game_created = game_id
        game_object = ROOMS[id_of_game_created]
        assert game_object.players[0] == session["user_id"]
        assert game_object.game_id == id_of_game_created
        assert response.json == {"room": id_of_game_created}


@pytest.mark.parametrize("read_json", ["game_regular_configs"], indirect=["read_json"])
def test_unlogged_room_creation(client, read_json):
    response = client.post(
        "/room/create", data=read_json, content_type="application/json"
    )
    assert response.json == {"error": "You need to login."}
    assert response.status_code == 401


@pytest.mark.parametrize("read_json", ["game_state_02"], indirect=["read_json"])
def test_successful_room_join(client, auth, read_json):
    game = Game.deserialize(json.load(read_json))
    ROOMS[game.game_id] = game
    data = {"room": game.game_id}
    with client:
        auth.login()
        response = client.post(
            "/room/join", data=json.dumps(data), content_type="application/json"
        )
        assert response.status_code == 200
        assert len(ROOMS[game.game_id].players) == 2


@pytest.mark.parametrize("read_json", ["game_state_01"], indirect=["read_json"])
def test_joining_a_full_room(client, auth, read_json):
    game = Game.deserialize(json.load(read_json))
    ROOMS[game.game_id] = game
    data = {"room": game.game_id}
    with client:
        auth.login()
        response = client.post(
            "/room/join", data=json.dumps(data), content_type="application/json"
        )
        assert response.status_code == 400
        assert response.json["error"] == "Game is full."
        assert len(ROOMS[game.game_id].players) == 2


def test_unlogged_room_join(client):
    data = {"room": "somegameid"}
    response = client.post(
        "/room/join", data=json.dumps(data), content_type="application/json"
    )
    assert response.json == {"error": "You need to login."}
    assert response.status_code == 401
