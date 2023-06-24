from battleship.models.board import *
from unittest.mock import Mock
from unittest import TestCase


class FakeShips(TestCase):
    def setUp(self):
        self.fake_cruiser = Mock()
        self.fake_cruiser.name = "Cruiser"
        self.fake_cruiser.size = 3
        self.fake_cruiser.coordinates = [[0,0], [0,1], [0,2]]
        self.fake_cruiser.alive = [True, True, True]


class TestShipCanBePlaced():
    def test_returns_false_if_ship_coords_are_negative_integers(self):
        invalid_ship = Mock()
        invalid_ship.coordinates = [[0,0], [-1,0]]
        board = Board()
        assert board.can_place(invalid_ship) == False
        
    def test_returns_false_if_ship_coords_are_not_integers(self):
        ship1, ship2 = Mock()
        ship1.coordinates = [[0,0], [-1,'hello']]
        ship2.coordinates = [[]]
        board = Board()
        assert board.can_place(invalid_ship) == False

    def test_returns_false_if_ship_coords_are_out_of_range(self):
        invalid_ship = Mock()
        invalid_ship.coordinates = [[0,0], [0,1], [0,2], [0,3], [0,4]]
        board = Board(size=4)
        assert board.can_place(invalid_ship) == False

    

# class TestBoardInitiation(FakeShips):
#     def test_render_board_with_default_size(self):
#         board = Board()
#         assert board.board == [[0] * 10 for x in range(10)]


#     def test_render_board_with_no_ships(self):
#         board = Board(array_size=5)
#         assert board.board == [[0] * 5 for x in range(5)]


#     def test_render_board_with_one_ship(self):
#         board = Board(array_size=5, ships=[self.fake_cruiser])
#         assert board.board == [
#             ["C", "C", "C", 0, 0],
#             [0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0],
#         ]


#     def test_render_board_with_multiple_ships(self):
#         board = Board(array_size=5, ships=[self.fake_destroyer, self.fake_cruiser])
#         assert board.board == [
#             ["C", "C", "C", 0, 0],
#             ["D", "D", 0, 0, 0],
#             [0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0],
#         ]


# class TestBoardShips(FakeShips):
#     def test_if_ship_object_can_be_returned(self):
#         board = Board(5, ships=[self.fake_destroyer, self.fake_cruiser])
#         assert board.get_ship_by_name('cruiser') == self.fake_cruiser

#     def test_returns_false_when_ship_not_found(self):
#         board = Board(5, ships=[self.fake_destroyer, self.fake_cruiser])
#         assert board.get_ship_by_name('battleship') == False