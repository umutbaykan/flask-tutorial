import pytest
import os
from battleship.models.game import *


@pytest.fixture
def game(request):
    configs = request.param
    test_directory = os.path.dirname(os.path.abspath(__file__))
    json_file_path = os.path.join(
        test_directory, "..", "seeds", "model_objects", f"{configs}.json"
    )
    with open(json_file_path) as file:
        json_data = file.read()
        game = Game.create_new_game_from_configs(json_data)
        yield game


@pytest.fixture
def ships_array(request):
    configs = request.param
    test_directory = os.path.dirname(os.path.abspath(__file__))
    json_file_path = os.path.join(
        test_directory, "..", "seeds", "model_objects", f"{configs}.json"
    )
    with open(json_file_path) as file:
        json_data = file.read()
        yield json_data


def test_successful_game_initialization():
    test_directory = os.path.dirname(os.path.abspath(__file__))
    json_file_path = os.path.join(
        test_directory, "..", "seeds", "model_objects", "game_regular_configs.json"
    )
    with open(json_file_path) as file:
        json_data = file.read()
        game = Game.create_new_game_from_configs(json_data)
        assert game.gameId == "fkEjOpkL"
        assert game.p1_id == "6495822522b4741d1481b1c6"
        assert game.p2_id == None
        assert game.boards[0].size == 8
        assert game.boards[1].size == 8
        assert game.ready == False
        assert game.turn == 0
        assert game.who_started == 1
        assert game.allowed_ships == {
            "Destroyer": 1,
            "Cruiser": 2,
            "AircraftCarrier": 1,
        }
        assert game.who_won == None


class TestValidators:
    def test_valid_player_request(self):
        game = Game(p1_id="p1idfromdb", p2_id="p2idfromdb")
        assert game._is_player_valid("p1idfromdb") == 0
        assert game._is_player_valid("p2idfromdb") == 1

    def test_invalid_player_request(self):
        game = Game(p1_id="p1idfromdb")
        assert game._is_player_valid("p2idfromdb") == False

    @pytest.mark.parametrize("game", ["game_regular_configs"], indirect=True)
    def test_returns_true_when_boards_are_placed(self, game):
        game.boards[0].ships = ["someshipobject"]
        game.boards[1].ships = ["someshipobject"]
        assert game._are_boards_placed() == True
        assert game.ready == True

    @pytest.mark.parametrize("game", ["game_regular_configs"], indirect=True)
    def test_returns_false_if_one_board_is_empty(self, game):
        game.boards[0].ships = []
        game.boards[1].ships = ["someshipobject"]
        assert game._are_boards_placed() == False
        assert game.ready == False

    @pytest.mark.parametrize(
        "game, ships_array",
        [("game_regular_configs", "ship_placement_multiple")],
        indirect=["game", "ships_array"],
    )
    def test_validates_if_the_ship_array_passed_in_is_valid(self, game, ships_array):
        parsed_ships_array = json.loads(ships_array)
        assert game._validate_ship_array(parsed_ships_array) == True

    @pytest.mark.parametrize(
        "game, ships_array",
        [
            ("game_regular_configs", "ship_placement_mismatch"),
            ("game_regular_configs", "ship_placement_empty"),
            ("game_regular_configs", "ship_placement_invalid_ship_names"),
        ],
        indirect=["game", "ships_array"],
    )
    def test_invalid_ship_array(self, game, ships_array):
        parsed_ships_array = json.loads(ships_array)
        assert game._validate_ship_array(parsed_ships_array) is False
