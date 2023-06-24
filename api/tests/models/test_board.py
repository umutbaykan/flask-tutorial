import pytest
from battleship.models.board import *
from unittest.mock import Mock, MagicMock
from unittest import TestCase


class FakeShips(TestCase):
    def setUp(self):
        self.fake_cruiser = MagicMock()
        self.fake_cruiser.name = "Cruiser"
        self.fake_cruiser.size = 3
        self.fake_cruiser.coordinates = [[0, 0], [0, 1], [0, 2]]
        self.fake_cruiser.alive = [True, True, False]
        self.fake_cruiser.hit.return_value = True

        self.fake_destroyer = MagicMock()
        self.fake_destroyer.name = "Destroyer"
        self.fake_destroyer.hit.return_value = False

        self.sunk_cruiser = Mock()
        self.sunk_cruiser.alive = [False, False, False]

        self.sunk_destroyer = Mock()
        self.sunk_destroyer.alive = [False, False]


def test_board_initialization():
    board = Board()
    assert board.size == 10
    assert board.ships == []
    assert board.missed_shots == []


class TestShipCanBePlaced:
    @pytest.mark.parametrize(
        "coordinates, expected_result",
        [
            ([[0, 0], [1, 0], [2, 0]], True),
            ([[0, 1], [0, 2], [0, 3]], False),
            ([[3, 0], [3, 1]], False),
        ],
    )
    def test_can_place_ship_on_empty_board(self, coordinates, expected_result):
        test_ship = Mock()
        test_ship.coordinates = coordinates
        board = Board(3)
        assert board.can_place(test_ship) == expected_result

    @pytest.mark.parametrize(
        "coordinates, expected_result",
        [
            ([[1, 1], [1, 2]], True),
            ([[0, 2], [0, 3]], False),
            ([[3, 0], [4, 0]], False),
        ],
    )
    def test_can_place_ship_on_already_populated_board(
        self, coordinates, expected_result
    ):
        test_ship, ship1, ship2 = Mock(), Mock(), Mock()
        test_ship.coordinates = coordinates
        ship1.coordinates = [[0, 0], [0, 1], [0, 2]]
        ship2.coordinates = [[1, 0], [2, 0], [3, 0]]
        board = Board(5, ships=[ship1, ship2])
        assert board.can_place(test_ship) == expected_result


class TestShipsGetHit(FakeShips):
    def test_can_get_hit(self):
        board = Board(ships=[self.fake_destroyer, self.fake_cruiser])
        result = board.shoot([0, 2])
        self.fake_destroyer.hit.assert_called_with([0, 2])
        self.fake_cruiser.hit.assert_called_with([0, 2])
        assert result == True
        assert board.missed_shots == []

    def test_miss(self):
        board = Board(ships=[self.fake_destroyer])
        result = board.shoot([0, 2])
        self.fake_destroyer.hit.assert_called_with([0, 2])
        assert result == False
        assert board.missed_shots == [[0, 2]]


class TestIfShipsAreAlive(FakeShips):
    def test_ships_alive(self):
        board = Board(ships=[self.fake_cruiser, self.sunk_destroyer])
        assert board.ships_alive() == True

    def test_all_ships_sunk(self):
        board = Board(ships=[self.sunk_cruiser, self.sunk_destroyer])
        assert board.ships_alive() == False


from battleship.models.ship import *

cruiser = Cruiser([[0, 0], [0, 1], [0, 2]], alive_override=[True, True, False])
destroyer = Destroyer([[3,3], [4,3]], alive_override=[False, True] )

def test_if_board_is_serialized_correctly():
    board = Board(
        size=7,
        ships=[cruiser, destroyer],
        missed_shots=[[0, 4], [2, 3], [5, 5]],
    )
    expected_state = {
        "size": 7,
        "ships": [
            {
                "name": "Cruiser",
                "coordinates": [[0, 0], [0, 1], [0, 2]],
                "alive": [True, True, False],
            },
            {
                "name": "Destroyer",
                "coordinates": [[3, 3], [4, 3]],
                "alive": [False, True],
            },
        ],
        "missed_shots": [[0, 4], [2, 3], [5, 5]],
    }
    assert Board.serialize(board) == expected_state
