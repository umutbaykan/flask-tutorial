class Board:
    def __init__(self, size=10, ships=[], shots=[]):
        self.size = size
        self.ships = ships
        self.shots = shots

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
        return False
