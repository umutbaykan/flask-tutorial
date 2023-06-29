from .ship import Ship
from ..utils.helpers import validate_coordinate_input


class Board:
    def __init__(self, size=10, ships=None, missed_shots=None):
        self.size = size
        self.ships = ships if ships is not None else []
        self.missed_shots = missed_shots if missed_shots is not None else []

    def place(self, ship):
        if self.can_place(ship):
            self.ships.append(ship)
            return True
        else:
            return False

    def can_place(self, ship):
        placed_ship_coords = self.retrieve_placed_ship_coordinates()
        for coordinate in ship.coordinates:
            if (
                coordinate[0] >= self.size
                or coordinate[1] >= self.size
                or tuple(coordinate) in placed_ship_coords
            ):
                return False
            placed_ship_coords.add(tuple(coordinate))
        return True

    def retrieve_placed_ship_coordinates(self):
        placed_ship_coords = set()
        for ship in self.ships:
            for coordinate in ship.coordinates:
                placed_ship_coords.add(tuple(coordinate))
        return placed_ship_coords

    def shoot(self, coordinate):
        for ship in self.ships:
            if ship.hit(coordinate):
                return True
        self.missed_shots.append(coordinate)
        return False

    def ships_alive(self):
        for ship in self.ships:
            if True in ship.alive:
                return True
        return False

    @staticmethod
    def _validate_board_size(size):
        if type(size) != int or size > 16 or size < 5:
            raise ValueError("Invalid board size.")
        
    @staticmethod
    def hide_ship_coordinates(serialized_board):
        ships_array = serialized_board.get("ships")
        for ship in ships_array:
            i = 0
            while i < len(ship["coordinates"]):
                if ship["alive"][i] is True:
                    del ship["alive"][i]
                    del ship["coordinates"][i]
                else:
                    i += 1
        serialized_board["ships"] = ships_array
        return serialized_board

    @staticmethod
    def serialize(board):
        serialized_ships = []
        for ship in board.ships:
            serialized_ships.append(Ship.serialize(ship))
        data = {
            "size": board.size,
            "ships": serialized_ships,
            "missed_shots": board.missed_shots,
        }
        return data

    @staticmethod
    def deserialize(board_state):
        unparsed_ships = board_state.get("ships", [])
        ship_objects = []
        for ship in unparsed_ships:
            ship_objects.append(Ship.deserialize(ship))
        size = board_state.get("size")
        missed_shots = board_state.get("missed_shots", [])
        validate_coordinate_input(missed_shots)
        Board._validate_board_size(size)
        return Board(size=size, ships=ship_objects, missed_shots=missed_shots)
