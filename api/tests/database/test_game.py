from battleship.database.game import *
from ..seeds.model_states.game_state import *


def test_create_game(app_context):
    result = create_game(state_2)
    assert result.inserted_id is not None


def test_get_game_by_game_id(app_context):
    result = get_game_by_game_id("aFKeajFE")
    assert result["game_id"] == "aFKeajFE"
    assert result["boards"] == state_1["boards"]


def test_if_game_id_does_not_exist(app_context):
    result = get_game_by_game_id("abcdefgh")
    assert result is None


def test_save_game(app_context):
    save_game(state_3)
    updated_game = get_game_by_game_id(state_3["game_id"])
    assert updated_game["game_id"] == state_3["game_id"]
    assert updated_game["boards"][0]["ships"][0]["alive"] == [False, False, False]
    assert updated_game["turn"] == 12
    assert updated_game["who_won"] == "player_2"


def test_save_game_on_nonexistent_game(app_context):
    save_game(state_2)
    result = get_game_by_game_id("jDKwRo12")
    assert result is None
