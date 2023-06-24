import json


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
        if name not in ship_classes:
            raise ValueError("Invalid ship name.")
        if type(coordinates) != list:
            raise ValueError("Invalid data type for coordinates.")
        if len(coordinates) > size:
            raise ValueError(
                "Invalid coordinates. The length exceeds the size of the ship."
            )
        for coord in coordinates:
            if not isinstance(coord, list) or len(coord) != 2:
                raise ValueError("Invalid coordinate format. Expected [x, y] format.")
            if not all(isinstance(val, int) and val >= 0 for val in coord):
                raise ValueError(
                    "Invalid coordinate value. Coordinates must be non-negative integers."
                )
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
        ship_dict = json.loads(ship_state)
        name = ship_dict["name"]
        if name in ship_classes:
            ship_class = ship_classes[name]
            coordinates = ship_dict["coordinates"]
            alive_override = ship_dict.get("alive")
            Ship._validate_ship_data(name, ship_class.size, coordinates, alive_override)
            return ship_class(coordinates, alive_override=alive_override)
        return False


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
