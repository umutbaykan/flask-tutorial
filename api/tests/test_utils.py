import pytest
from battleship.utils.room_object import ROOMS
from battleship.utils.helpers import *
from unittest.mock import Mock

# @pytest.mark.parametrize("room_id, player_id, args, expected_result", [
#     ("manually_generated", "admiral_1", (), True),  # Test case 1: No additional args
#     ("manually_generated", "admiral_2", (), False),  # Test case 2: Different player_id
#     (None, "admiral_2", (), False),  # Test case 3: No room_id
#     ("manually_generated", None, (), False),  # Test case 4: No player_id
#     ("manually_generated", "admiral_1", ('someothercheck', None), False),  # Test case 5: Additional args with none
#     ("manually_generated", "admiral_1", ('arg1', 'arg2'), True)  # Test case 6: Additional args with valid inputs
# ])
# def test_room_event_is_from_users_within_room_object(room_id, player_id, args, expected_result):
#     ROOMS['manually_generated'] = {"players": ['admiral_1']}
#     result = validate_user_and_game(room_id, player_id, *args)
#     assert result == expected_result


