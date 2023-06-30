import pytest
from battleship.database.user import *


def test_get_user_by_username(app_context):
    result = get_user_by_username("admiral_1")
    assert result["username"] == "admiral_1"


def test_username_doesnt_exist(app_context):
    result = get_user_by_username("admiral_x")
    assert result == None


def test_get_user_by_id(app_context):
    existing_user = get_user_by_username("admiral_1")
    returned_user = get_user_by_id(str(existing_user["_id"]))
    assert existing_user["_id"] == returned_user["_id"]


def test_id_doesnt_exist(app_context):
    result = get_user_by_id("648b0ab97d35b91c5d20db2e")
    assert result == None


def test_user_registration_went_okay(app_context):
    register_user("admiral_3", "password")


def test_user_already_registered(app_context):
    with pytest.raises(ValueError) as e:
        register_user("admiral_1", "password")
    error_message = str(e.value)
    assert error_message == "Username already exists"


def test_adding_game_to_user_history(app_context):
    user = get_user_by_username("admiral_1")
    for _ in range(2):
        add_game_to_user_history(user["_id"], "manual_game_id")
    user = get_user_by_username("admiral_1")
    assert user["games"] == ["manual_game_id", "manual_game_id"]