import pytest
from battleship.utils.room_object import *


@pytest.mark.parametrize("room_id, player_id, args, expected_result", [
    ("manually_generated", "admiral_1", (), True),  # Test case 1: No additional args
    ("manually_generated", "admiral_2", (), False),  # Test case 2: Different player_id
    (None, "admiral_2", (), False),  # Test case 3: No room_id
    ("manually_generated", None, (), False),  # Test case 4: No player_id
    ("manually_generated", "admiral_1", ('someothercheck', None), False),  # Test case 5: Additional args with none
    ("manually_generated", "admiral_1", ('arg1', 'arg2'), True)  # Test case 6: Additional args with valid inputs
])
def test_room_event_is_from_users_within_room_object(room_id, player_id, args, expected_result):
    ROOMS['manually_generated'] = {"players": ['admiral_1']}
    result = room_event_is_from_users_within_room_object(room_id, player_id, *args)
    assert result == expected_result


def test_creating_a_new_game_state():
    create_new_game_state('manually_generated', {"configs":1,"players":["admiral_1", "admiral_2"]})
    assert ROOMS['manually_generated'] == {"configs":1,"players":["admiral_1", "admiral_2"]}


@pytest.mark.parametrize("room_name, player_to_remove, expected_result", [
    ("manually_generated", "admiral_1", {"players": ['admiral_2']}),  
    ("manually_generated", "admiral_2", {"players": ['admiral_1']}),  
    ("manually_generated", "not_here", {"players": ['admiral_1', 'admiral_2']}), 
    ("manually_generated", "", {"players": ['admiral_1', 'admiral_2']}),  
])
def test_user_leaving_a_room(room_name, player_to_remove, expected_result):
    ROOMS[room_name] = {"players": ['admiral_1', 'admiral_2']}
    remove_player_from_game(room_name, player_to_remove)
    assert ROOMS[room_name] == expected_result