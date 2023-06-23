class Board:
    def __init__(self, array_size=10, ships=None):
        self.ships = ships or []
        self.board = self.generate_board(array_size)


    def generate_board(self, array_size): 
        board = [([0] * array_size) for _ in range(array_size)]
        for ship in self.ships:
            for ship_piece in ship.coordinates:
                board[ship_piece['row']][ship_piece['column']] = ship.symbol
        return board


    def print_board(self):
        for row in self.board:
            print(row)
