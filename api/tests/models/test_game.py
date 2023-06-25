import pytest
import os
from battleship.models.game import *
from unittest.mock import Mock
from unittest import TestCase


class FakeBoards(TestCase):
    def setUp(self):
        self.live_board_1 = Mock()
        self.live_board_1.ships_alive.return_value = True
        self.live_board_1.ships = ["P1 Ship"]

        self.live_board_2 = Mock()
        self.live_board_2.ships_alive.return_value = True
        self.live_board_2.ships = ["P2 Ship"]

        self.sunk_board = Mock()
        self.sunk_board.ships_alive.return_value = False


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
    game.boards[0].ships, game.boards[1].ships = [], []
    game.boards[0].missed_shots, game.boards[1].missed_shots = [], []
    game.players == []


@pytest.fixture
def read_json(request):
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
        assert game.players[0] == "6495822522b4741d1481b1c6"
        assert game.boards[0].size == 8
        assert game.boards[1].size == 8
        assert game.ready == False
        assert game.turn == 1
        assert game.who_started == 2
        assert game.allowed_ships == {
            "Destroyer": 1,
            "Cruiser": 2,
            "AircraftCarrier": 1,
        }
        assert game.who_won == None


@pytest.mark.parametrize(
    "game, read_json",
    [("game_regular_configs", "ship_placement_multiple")],
    indirect=["game", "read_json"],
)
def test_successful_ship_placement(game, read_json):
    parsed_ships = Game._validate_ship_json(read_json)
    result = game.place_ships(0, parsed_ships)
    assert result == True
    assert len(game.boards[0].ships) == 4
    for ship in game.boards[0].ships:
        assert all(element == True for element in ship.alive)
    assert game.boards[0].ships[0].coordinates == [[4, 4], [4, 5]]


@pytest.mark.parametrize(
    "game, read_json, expected_error",
    [
        ("game_regular_configs", "ship_placement_multiple_but_clashing", {"error": "Cannot place ships."}),
        ("game_regular_configs", "ship_placement_invalid_ship_class", {"error": "Invalid ship size."})
     ],
    indirect=["game", "read_json"],
)
def test_unsuccessful_ship_placement_due_to_ship_corruption(game, read_json, expected_error):
    parsed_ships = Game._validate_ship_json(read_json)
    result = game.place_ships(0, parsed_ships)
    assert result == expected_error
    assert game.boards[0].ships == []


class TestIfPlayersCanBeAddedToGame:
    def test_adding_new_player(self):
        game = Game(players=[])
        assert game.add_player('player_1') == True
        assert game.players == ['player_1']
        assert game.add_player('player_2') == True
        assert game.players == ['player_1', 'player_2']

    def test_adding_another_player_when_capacity_is_full(self):
        game = Game(players=['player_1', 'player_2'])
        assert game.add_player('player_3') == {"error": "Game is full."}
        

class TestIfGameUnderstandsWhoseTurnIsIt(FakeBoards):
    def test_returns_true_if_it_is_your_turn(self):
        # Game instance - Player 1 should start and its the first turn.
        # Player 1 should have the turn
        game = Game(boards=[self.live_board_1, self.live_board_2], who_started=1, turn=1, players=['player_1', 'player_2'])
        assert game.is_players_turn('player_1') == True
        assert game.is_players_turn('player_2') == False
        assert game.is_players_turn('player_3') == False

    def test_returns_the_opponents_board_to_shoot_at_when_its_your_turn(self):
        # Game instance - Player 1 should start and its the first turn.
        # Player 2 board should return
        game = Game(boards=[self.live_board_1, self.live_board_2], who_started=1, turn=1, players=['player_1', 'player_2'])
        assert game.is_players_turn('player_1') == True
        assert game._get_opponents_board() == self.live_board_2


class TestIfGameUnderstandsItsOver(FakeBoards):
    def test_returns_false_if_both_boards_are_alive(self):
        game = Game(boards=[self.live_board_1, self.live_board_2])
        assert game.is_over() == False

    def test_returns_true_if_one_board_is_sunk(self):
        game = Game(boards=[self.live_board_1, self.sunk_board])
        assert game.is_over() == True


class TestValidators:
    def test_valid_player_request(self):
        game = Game(players=["p1idfromdb", "p2idfromdb"])
        assert game._is_player_valid("p1idfromdb") == True
        assert game._is_player_valid("p2idfromdb") == True

    def test_invalid_player_request(self):
        game = Game(players=["p1idfromdb"])
        assert game._is_player_valid("p2idfromdb") == {"error": "You are not in the game."}

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
        "parsed_configs_ships, expected_result",
        [
            (
                [
                    {"Destroyer": 1},
                    {"Cruiser": 2},
                    {"Battleship": 0},
                    {"AircraftCarrier": 1},
                ],
                {"Destroyer": 1, "Cruiser": 2, "AircraftCarrier": 1},
            ),
            (
                [
                    {"Submarine": 3},
                ],
                {},
            ),
            (
                [
                    {"Cruiser": -3},
                    {"Battleship": 2},
                ],
                {"Battleship": 2},
            ),
            ([{"Cruiser": True}], {}),
        ],
    )
    def test_getting_allowed_ships(self, parsed_configs_ships, expected_result):
        result = Game._get_allowed_ships(parsed_configs_ships)
        assert result == expected_result

    @pytest.mark.parametrize(
        "read_json, expected_result",
        [
            ("ship_placement_empty", False),
            ("ship_placement_invalid_ship_array", False),
            (
                "ship_placement_single",
                [{"name": "Destroyer", "coordinates": [[4, 4], [4, 5]]}],
            ),
        ],
        indirect=["read_json"],
    )
    def test_invalid_ship_json(self, read_json, expected_result):
        assert Game._validate_ship_json(read_json) == expected_result

    @pytest.mark.parametrize(
        "game, read_json, expected_result",
        [
            ("game_regular_configs", "ship_placement_multiple", True),
            ("game_regular_configs", "ship_placement_mismatch", False),
        ],
        indirect=["game", "read_json"],
    )
    def test_validates_if_the_ship_array_passed_in_is_valid(
        self, game, read_json, expected_result
    ):
        parsed_ships = Game._validate_ship_json(read_json)
        assert (
            game._check_incoming_ships_match_with_configs(parsed_ships)
            == expected_result
        )
