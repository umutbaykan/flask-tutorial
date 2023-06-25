import json
from .ship import ship_classes
from .board import Board

class Game:
    def __init__(self, gameId=None, p1_id=None, p2_id=None, allowed_ships={}):
        self.gameId = gameId
        self.p1_id = p1_id
        self.p2_id = p2_id
        self.boards = []
        self.game_ready = False
        self.turn = 0
        self.who_started = None
        self.allowed_ships = allowed_ships
        self.who_won = None

    def is_player_valid(self, player_id):
        pass

    def place_ships(self, player_id, ships_json):
        pass

    def are_boards_placed(self):
        pass

    @staticmethod
    def _validate_configurations(configs):
        configs_dict = json.loads(configs)
        # Throw an error if configs are corrupted, otherwise return as dictionary
        return configs_dict
    
    @staticmethod
    def _get_allowed_ships(validated_ship_dict):
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
        [new_game.boards.append(Board(size=parsed_configs['size'])) for _ in range(2)]
        new_game.allowed_ships = Game._get_allowed_ships(parsed_configs['ships'])
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
