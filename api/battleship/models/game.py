import json
from .ship import Ship, ship_classes
from .board import Board


class Game:
    def __init__(self, gameId=None, p1_id=None, p2_id=None, allowed_ships={}):
        self.gameId = gameId
        self.p1_id = p1_id
        self.p2_id = p2_id
        self.boards = []
        self.ready = False
        self.turn = 0
        self.who_started = None
        self.allowed_ships = allowed_ships
        self.who_won = None

    def place_ships(self, player_index, ships_array):
        current_board = self.boards[player_index]
        current_board_state = Board.serialize(self.boards[player_index])
        for ship in ships_array:
            try:
                ship_object = Ship.deserialize(ship)
                if not current_board.can_place(ship_object):
                    self.boards[player_index] = Board.deserialize(current_board_state)
                    return {"error": "Cannot place ships"}
            except ValueError as ve:
                self.boards[player_index] = Board.deserialize(current_board_state)
                return {"error": ve}
        self._are_boards_placed()
        return True
    
    def _is_player_valid(self, session_id):
        if session_id == self.p1_id:
            return 0
        elif session_id == self.p2_id:
            return 1
        return False

    def _are_boards_placed(self):
        for board in self.boards:
            if len(board.ships) == 0:
                return False
        self.ready = True
        return True
    
    def _validate_ship_array(self, ships_array):
        ship_occurrence = {}
        for ship in ships_array:
            ship_occurrence[ship.get("name", "invalid")] = (
                ship_occurrence.get(ship.get("name", "invalid"), 0) + 1
            )
        return ship_occurrence == self.allowed_ships

    @staticmethod
    def _validate_ship_json(ships_json):
        try:
            ships_array = json.loads(ships_json)
            if ships_array.get("ships"):
                return ships_array["ships"]
        except json.JSONDecodeError:
            pass
        return False

    @staticmethod
    def _validate_configurations(configs):
        configs_dict = json.loads(configs)
        # Throw an error if configs are corrupted, otherwise return as dictionary
        return configs_dict

    @staticmethod
    def _get_allowed_ships(validated_ship_dict):
        # Tests currently missing
        chosen_ships = {}
        for item in validated_ship_dict:
            for key, value in item.items():
                if key in ship_classes and value > 0:
                    chosen_ships[key] = value
        return chosen_ships

    @staticmethod
    def create_new_game_from_configs(configs):
        new_game = Game()
        parsed_configs = Game._validate_configurations(configs)
        [new_game.boards.append(Board(size=parsed_configs["size"])) for _ in range(2)]
        new_game.allowed_ships = Game._get_allowed_ships(parsed_configs["ships"])
        new_game.p1_id = parsed_configs["p1_id"]
        new_game.gameId = parsed_configs["game_id"]
        new_game.who_started = parsed_configs["who_started"]
        return new_game

    @staticmethod
    def serialize(gamestate):
        pass

    @staticmethod
    def deserialize(gamestate):
        pass
