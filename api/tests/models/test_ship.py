import pytest
import os
import json
from battleship.models.ship import *


def test_successful_ship_initiation_on_default_class():
    ship = Ship("Battleship", 4, [[0, 0], [0, 1], [0, 2], [0, 3]])
    assert ship.coordinates == [[0, 0], [0, 1], [0, 2], [0, 3]]
    assert ship.name == "Battleship"
    assert ship.alive == [True, True, True, True]


@pytest.mark.parametrize(
    "ship_class, size, coordinates",
    [
        (Destroyer, 2, [[0, 0], [0, 1]]),
        (Cruiser, 3, [[0, 0], [0, 1], [0, 2]]),
        (Battleship, 4, [[0, 0], [0, 1], [0, 2], [0, 3]]),
        (AircraftCarrier, 5, [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4]]),
    ],
)
def test_successful_ship_creation(ship_class, size, coordinates):
    ship = ship_class(coordinates)
    assert ship.coordinates == coordinates
    assert ship.name == ship_class.__name__
    assert ship.alive == [True] * size


@pytest.mark.parametrize(
    "coordinates, expected_error",
    [
        (
            [[0, 0], [0, 1], [0, 2]],
            "Invalid coordinates. The length does not match the size of the ship.",
        ),
        (
            [[0, 0]],
            "Invalid coordinates. The length does not match the size of the ship.",
        ),
        (True, "Invalid data type for coordinates."),
        (
            [[0, 0], [-1, 1]],
            "Invalid coordinate value. Coordinates must be non-negative integers.",
        ),
        (
            [[0, 0], [1, 1]],
            "Invalid coordinates. Ships can't be placed diagonally.",
        ),
        (
            [[0, 0], ["-1", 1]],
            "Invalid coordinate value. Coordinates must be non-negative integers.",
        ),
    ],
)
def test_validate_ship_coordinates(coordinates, expected_error):
    with pytest.raises(ValueError) as e:
        Destroyer(coordinates)
    assert str(e.value) == expected_error


def test_if_ship_name_is_invalid():
    with pytest.raises(ValueError) as e:
        Ship("Submarine", 3, [[0, 0], [0, 1], [0, 2]])
    assert str(e.value) == "Invalid ship name."


def test_if_ship_is_hit_successfully():
    ship = Destroyer([[0, 0], [0, 1]])
    result = ship.hit([0, 0])
    assert result == True
    assert ship.alive == [False, True]


def test_if_ship_is_not_hit():
    ship = Destroyer([[0, 0], [0, 1]])
    result = ship.hit([0, 2])
    assert result == False
    assert ship.alive == [True, True]


def test_if_ship_damage_can_be_overridden():
    ship = Destroyer([[0, 0], [0, 1]], alive_override=[False, True])
    assert ship.alive == [False, True]


def test_if_ship_is_serialized_correctly():
    ship = Cruiser([[0, 0], [0, 1], [0, 2]])
    ship.hit([0, 2])
    expected_state = {
        "name": "Cruiser",
        "coordinates": [[0, 0], [0, 1], [0, 2]],
        "alive": [True, True, False],
    }
    dict_ship = Ship.serialize(ship)
    assert dict_ship == expected_state


@pytest.mark.parametrize(
    "json_file, expected_name, expected_coordinates, expected_alive",
    [
        (
            "ship_correct.json",
            "Cruiser",
            [[0, 0], [0, 1], [0, 2]],
            [True, True, False],
        ),
        (
            "ship_fully_alive.json",
            "Cruiser",
            [[3, 0], [4, 0], [5, 0]],
            [True, True, True],
        ),
    ],
)
def test_ship_deserialization(
    json_file, expected_name, expected_coordinates, expected_alive
):
    test_directory = os.path.dirname(os.path.abspath(__file__))
    json_file_path = os.path.join(
        test_directory, "..", "seeds", "model_objects", json_file
    )
    with open(json_file_path) as file:
        json_data = json.load(file)
        result = Ship.deserialize(json_data)

    assert result.name == expected_name
    assert result.coordinates == expected_coordinates
    assert result.alive == expected_alive


@pytest.mark.parametrize(
    "json_file, expected_error",
    [
        (
            "ship_too_long.json",
            "Invalid coordinates. The length does not match the size of the ship.",
        ),
        ("ship_invalid.json", "Invalid overridden ship data."),
        ("ship_empty_object.json", "Invalid ship size."),
    ],
)
def test_if_ship_deserialized_input_is_incorrect(json_file, expected_error):
    test_directory = os.path.dirname(os.path.abspath(__file__))
    json_file_path = os.path.join(
        test_directory, "..", "seeds", "model_objects", json_file
    )
    with open(json_file_path) as file:
        json_data = json.load(file)
        with pytest.raises(ValueError) as e:
            Ship.deserialize(json_data)
        assert str(e.value) == expected_error
