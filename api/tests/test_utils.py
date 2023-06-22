from battleship.utils.room_object import *


def test_if_room_object_contains_user_id():
    ROOMS['manually_generated'] = {"players": ['admiral_1']}
    result = room_event_is_from_users_within_room_object('manually_generated', 'admiral_1')
    assert result == True


def test_if_room_object_does_not_contain_id():
    ROOMS['manually_generated'] = {"players": ['admiral_1']}
    result = room_event_is_from_users_within_room_object('manually_generated', 'admiral_2')
    assert result == False


def test_if_no_room_input_is_passed_in():
    ROOMS['manually_generated'] = {"players": ['admiral_1']}
    result = room_event_is_from_users_within_room_object(None, 'admiral_2')
    assert result == False


def test_if_no_id_input_is_passed_in():
    ROOMS['manually_generated'] = {"players": ['admiral_1']}
    result = room_event_is_from_users_within_room_object('manually_generated', None)
    assert result == False

def test_if_additional_inputs_are_valid():
    ROOMS['manually_generated'] = {"players": ['admiral_1']}
    result = room_event_is_from_users_within_room_object('manually_generated', 'admiral_1', 'someothercheck', None)
    assert result == False