class Ship:
    def __init__(self, name, size, orientation, starting_coordinate):
        self.name = name
        self.size = size
        self.orientation = orientation
        self.coordinates = self.generate_coordinates(starting_coordinate)
        self.sunk = False

    def is_sunk(self):
        return all(piece["hit"] for piece in self.coordinates)
    
    def generate_coordinates(self, starting_coordinate):
        coordinates = []
        row, column = starting_coordinate
        for i in range(self.size):
            if self.orientation == "horizontal":
                coordinates.append({"column": column + i, "row": row, "hit": False})
            elif self.orientation == "vertical":
                coordinates.append({"column": column, "row": row + 1, "hit": False})
        return coordinates

    