import pytest
from battleship.database.game import *
from ..seeds.model_states.game_state import *


def test_create_game(app_context):
    result = create_game(state_2)
    assert result.inserted_id is not None


def test_get_game_by_game_id(app_context):
    result = get_game_by_game_id("aFKeajFE")
    assert result["game_id"] == "aFKeajFE"


def test_save_game(app_context):
    result = save_game(state_3)
    updated_game = get_game_by_game_id(state_3["game_id"])
    assert updated_game["game_id"] == state_3["game_id"]
    assert updated_game["boards"][0]["ships"][0]["alive"] == [False, False, False]
    assert updated_game["turn"] == 12
    assert updated_game["who_won"] == 'player_2'


def test_save_game_on_nonexistent_game(app_context):
    with pytest.raises(ValueError) as e:
        save_game(state_2)
    error_message = str(e.value)
    assert error_message == "No such game exists"


def test_load_game(app_context):
    result = load_game("aFKeajFE")
    assert result["game_id"] == state_1["game_id"]
    assert result["boards"] == state_1["boards"]