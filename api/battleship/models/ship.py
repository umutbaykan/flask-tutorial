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
    def _validate_ship_is_straight(coordinates):
        rows, columns = set(), set()
        for coord in coordinates:
            rows.add(coord[0])
            columns.add(coord[1])
        if len(rows) > 1 and len(columns) > 1:
            raise ValueError("Invalid coordinates. Ships can't be placed diagonally.")

    @staticmethod
    def _validate_ship_data(name, size, coordinates, alive_override):
        if type(size) != int:
            raise ValueError("Invalid ship size.")
        if name not in ship_classes:
            raise ValueError("Invalid ship name.")
        if type(coordinates) != list:
            raise ValueError("Invalid data type for coordinates.")
        if len(coordinates) != size:
            raise ValueError(
                "Invalid coordinates. The length does not match the size of the ship."
            )
        validate_coordinate_input(coordinates)
        Ship._validate_ship_is_straight(coordinates)
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
        name = ship_state.get("name")
        ship_class = ship_classes.get(name)
        size = ship_class.size if ship_class else None
        coordinates = ship_state.get("coordinates")
        alive_override = ship_state.get("alive")
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
