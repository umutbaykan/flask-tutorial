import pytest
import json
import os
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


def test_if_ship_coordinates_are_larger_than_allowed_size():
    with pytest.raises(ValueError) as e:
        Destroyer([[0, 0], [0, 1], [0, 2]])
    assert (
        str(e.value) == "Invalid coordinates. The length exceeds the size of the ship."
    )


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
    ship = Destroyer([[0, 0], [0, 1]], overridden=[False, True])
    assert ship.alive == [False, True]


def test_if_ship_is_serialized_correctly():
    ship = Cruiser([[0, 0], [0, 1], [0, 2]])
    ship.hit([0, 2])
    expected_state = {
        "name": "Cruiser",
        "coordinates": [[0, 0], [0, 1], [0, 2]],
        "alive": [True, True, False],
    }
    json_ship = Ship.serialize(ship)
    parsed_data = json.loads(json_ship)
    assert parsed_data == expected_state


def test_if_ship_is_deserialized_correctly():
    test_directory = os.path.dirname(os.path.abspath(__file__))
    json_file_path = os.path.join(
        test_directory, "..", "seeds", "model_objects", "ship_correct.json"
    )
    with open(json_file_path) as file:
        json_data = file.read()
        result = Ship.deserialize(json_data)
    assert result.name == "Cruiser"
    assert result.coordinates == [[0, 0], [0, 1], [0, 2]]
    assert result.alive == [True, True, False]


@pytest.mark.parametrize(
    "json_file, expected_error",
    [
        ("ship_too_long.json", "Invalid coordinates. The length exceeds the size of the ship."),
        ("ship_invalid.json", "Invalid overridden ship data."),
    ]
)
def test_if_ship_deserialized_input_is_incorrect(json_file, expected_error):
    test_directory = os.path.dirname(os.path.abspath(__file__))
    json_file_path = os.path.join(test_directory, "..", "seeds", "model_objects", json_file)
    with open(json_file_path) as file:
        json_data = file.read()
        with pytest.raises(ValueError) as e:
            Ship.deserialize(json_data)
        assert str(e.value) == expected_error
