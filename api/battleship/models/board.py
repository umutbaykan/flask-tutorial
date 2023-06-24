class Board:
    def __init__(self, size=10, list_of_ships=[], shots=[]):
        self.size = size
        self.list_of_ships = list_of_ships
        self.shots = shots
    
    def place(self, ship):
        if self.can_place(ship):
            self.list_of_ships.append(ship)
            return True
        else:
            return False
        
    def can_place(self, ship):
        for coordinate in ship.coordinates:
            # Check for invalid data types and negative integers
            if not all(isinstance(coord, int) and coord >= 0 for coord in coordinate):
                return False
            # Check whether coordinates are out of range
            if not all(coord < self.size for coord in coordinate):
                return False
        return True
