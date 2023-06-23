from battleship.models.board import *
from unittest.mock import Mock
from unittest import TestCase

class MyTestCase(TestCase):
    def setUp(self):
        self.fake_cruiser = Mock()
        self.fake_cruiser.coordinates = [{"row": 0, "column": 0}, {"row": 0, "column": 1}, {"row": 0, "column": 2}]
        self.fake_cruiser.symbol = "C"
        self.fake_destroyer = Mock()
        self.fake_destroyer.coordinates = [{"row": 1, "column": 0}, {"row": 1, "column": 1}]
        self.fake_destroyer.symbol = "D"

    def test_render_board_with_one_ship(self):
        board = Board(array_size=5, ships=[self.fake_cruiser])
        assert board.board == [
            ['C', 'C', 'C', 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]

    def test_render_board_with_multiple_ships(self):
        board = Board(array_size=5, ships=[self.fake_destroyer, self.fake_cruiser])
        assert board.board == [
            ['C', 'C', 'C', 0, 0],
            ['D', 'D', 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]