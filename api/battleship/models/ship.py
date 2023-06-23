class Ship:
    def __init__(self, name, size, symbol):
        self.name = name
        self.size = size
        self.symbol = symbol
        self.coordinates = []
        self.sunk = False

    def is_sunk(self):
        return all(piece["hit"] for piece in self.coordinates)
    
    def generate_coordinates(self, starting_coordinate, orientation):
        coordinates = []
        if starting_coordinate is None or orientation not in ['vertical', 'horizontal']:
            return
        row, column = starting_coordinate
        for i in range(self.size):
            if orientation == "horizontal":
                coordinates.append({"column": column + i, "row": row, "hit": False})
            elif orientation == "vertical":
                coordinates.append({"column": column, "row": row + 1, "hit": False})
        return coordinates
    


    