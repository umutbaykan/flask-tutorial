import json
from ..utils.helpers import validate_coordinate_input


class Ship:
    def __init__(self, name, size, coordinates, alive_override=None):
        self._validate_ship_data(name, size, coordinates, alive_override)
        self.name = name
        self.coordinates = coordinates
        if alive_override is not None:
            self.alive = alive_override
        else:
            self.alive = [True for _ in range(size)]

    def hit(self, bombed_coordinate):
        for i in range(len(self.coordinates)):
            if self.coordinates[i] == bombed_coordinate:
                self.alive[i] = False
                return True
        return False

    @staticmethod
    def _validate_ship_data(name, size, coordinates, alive_override):
        if type(size) != int:
            raise ValueError("Invalid ship size.")
        if name not in ship_classes:
            raise ValueError("Invalid ship name.")
        if type(coordinates) != list:
            raise ValueError("Invalid data type for coordinates.")
        if len(coordinates) > size:
            raise ValueError(
                "Invalid coordinates. The length exceeds the size of the ship."
            )
        validate_coordinate_input(coordinates)
        ## Add method to check for diagonal ships
        if alive_override is not None and len(alive_override) > size:
            raise ValueError("Invalid overridden ship data.")

    @staticmethod
    def serialize(ship):
        data = {
            "name": ship.name,
            "coordinates": ship.coordinates,
            "alive": ship.alive,
        }
        return data

    @staticmethod
    def deserialize(ship_state):
        if isinstance(ship_state, str):
            ship_dict = json.loads(ship_state)
        else:
            ship_dict = ship_state
        name = ship_dict.get("name")
        ship_class = ship_classes.get(name)
        size = ship_class.size if ship_class else None
        coordinates = ship_dict.get("coordinates")
        alive_override = ship_dict.get("alive")
        Ship._validate_ship_data(name, size, coordinates, alive_override)
        return ship_class(coordinates, alive_override=alive_override)


class Destroyer(Ship):
    size = 2

    def __init__(self, coordinates, alive_override=None):
        super().__init__("Destroyer", self.size, coordinates, alive_override)


class Cruiser(Ship):
    size = 3

    def __init__(self, coordinates, alive_override=None):
        super().__init__("Cruiser", self.size, coordinates, alive_override)


class Battleship(Ship):
    size = 4

    def __init__(self, coordinates, alive_override=None):
        super().__init__("Battleship", self.size, coordinates, alive_override)


class AircraftCarrier(Ship):
    size = 5

    def __init__(self, coordinates, alive_override=None):
        super().__init__("AircraftCarrier", self.size, coordinates, alive_override)


ship_classes = {
    "Destroyer": Destroyer,
    "Cruiser": Cruiser,
    "Battleship": Battleship,
    "AircraftCarrier": AircraftCarrier,
}
