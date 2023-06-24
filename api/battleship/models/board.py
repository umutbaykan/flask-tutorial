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
    

    def check_if_position_suitable(self, params):
        column = params['column']
        row = params['row']
        ship_length = self.ships[params['ship_name']]


    def get_ship_by_name(self, ship_name):
        for ship in self.ships:
            if ship.name == ship_name:
                return ship
        return False


    def print_board(self):
        for row in self.board:
            print(row)
