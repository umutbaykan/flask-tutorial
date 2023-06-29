import copy
from .ship import Ship, ship_classes
from .board import Board


class Game:
    def __init__(
        self,
        game_id=None,
        players=None,
        allowed_ships=None,
        boards=None,
        who_started=1,
        turn=1,
        ready=None,
        who_won=None,
    ):
        self.game_id = game_id
        self.players = players if players is not None else []
        self.boards = boards if boards is not None else []
        self.ready = ready if ready is not None else [False, False]
        self.turn = turn
        self.who_started = who_started
        self.allowed_ships = allowed_ships if allowed_ships is not None else {}
        self.who_won = who_won
        
    def place_ships(self, user_id, ships_array):
        player_index = self.players.index(user_id)
        current_board = self.boards[player_index]
        current_board_state = Board.serialize(self.boards[player_index])
        for ship in ships_array:
            try:
                ship_object = Ship.deserialize(ship)
                if not current_board.place(ship_object):
                    self.boards[player_index] = Board.deserialize(current_board_state)
                    return {"error": "Cannot place ships."}
            except ValueError as ve:
                self.boards[player_index] = Board.deserialize(current_board_state)
                return {"error": str(ve.args[0])}
        return True

    def is_over(self):
        for index, board in enumerate(self.boards):
            if not board.ships_alive():
                self.who_won = self.players[index - 1]
                return True
        return False

    def add_player(self, user_id):
        if user_id in self.players:
            return {"error": "You are already in this game."}
        elif len(self.players) > 1:
            return {"error": "Game is full."}
        self.players.append(user_id)
        return True
        
    def fire(self, coordinate):
        result = self._get_opponents_board().shoot(coordinate)
        self.turn += 1
        self.is_over()
        return result
    
    def remove_player(self, user_id):
        if self.is_player_valid(user_id):
            player_index = self.players.index(user_id)
            if player_index == 0:
                del self.ready[0]
                self.ready.append(False)
            else:
                self.ready[player_index] = False
            self.players.remove(user_id)
            return True
        return False
    
    def remove_player_ships(self, user_id):
        if self.is_player_valid(user_id):
            player_index = self.players.index(user_id)
            self.boards[player_index].ships = []
            return True
        return False

    def is_player_turn(self, user_id):
        if self.is_player_valid(user_id):
            player_index = (self.who_started + self.turn) % 2
            return self.players[player_index] == user_id
        return False

    def is_player_valid(self, user_id):
        if user_id in self.players:
            return True
        return False
    
    def is_ready(self):
        if all(self.ready):
            self.ready = True
            return True
        return False
    
    def set_ready(self, user_id):
        player_index = self.players.index(user_id)
        self.ready[player_index] = True
        return

    def _get_opponents_board(self):
        opponent_index = (self.who_started + self.turn + 1) % 2
        return self.boards[opponent_index]

    def _check_incoming_ships_match_with_configs(self, ships_array):
        ship_occurrence = {}
        for ship in ships_array:
            ship_occurrence[ship.get("name", "invalid")] = (
                ship_occurrence.get(ship.get("name", "invalid"), 0) + 1
            )
        return ship_occurrence == self.allowed_ships

    @staticmethod
    def _validate_ship_json(ships_array):
        if ships_array.get("ships"):
            return ships_array["ships"]
        return False

    @staticmethod
    def _validate_firing_coordinates_json(fire_dict):
        if fire_dict.get("coordinates") and fire_dict.get("user_id"):
            return fire_dict
        return False

    @staticmethod
    def _validate_configurations(configs):
        # Throw an error if configs are corrupted, otherwise return as dictionary
        return configs

    @staticmethod
    def _get_allowed_ships(validated_ship_dict):
        chosen_ships = {}
        for item in validated_ship_dict:
            for key, value in item.items():
                if key in ship_classes and value > 0 and type(value) == int:
                    chosen_ships[key] = value
        return chosen_ships

    @staticmethod
    def create_new_game_from_configs(configs, server_allocated_room=None, game_creator=None):
        new_game = Game()
        parsed_configs = Game._validate_configurations(configs)
        [new_game.boards.append(Board(size=parsed_configs["size"])) for _ in range(2)]
        new_game.allowed_ships = Game._get_allowed_ships(parsed_configs["ships"])
        new_game.players.append(game_creator)
        new_game.game_id = server_allocated_room
        new_game.who_started = parsed_configs["who_started"]
        return new_game

    @staticmethod
    def hide_board_info(serialized_game, user_id, opponent=False):
        if len(serialized_game["players"]) == 2:
            masked_game_info = copy.deepcopy(serialized_game)
            if opponent is True:
                index = masked_game_info.get("players").index(user_id) - 1
            else:
                index = masked_game_info.get("players").index(user_id)
            opponent_board = masked_game_info["boards"][index]
            masked_game_info["boards"][index] = Board.hide_ship_coordinates(opponent_board)
            return masked_game_info
        return serialized_game

    @staticmethod
    def serialize(game):
        serialized_boards = []
        for i in range(2):
            serialized_boards.append(Board.serialize(game.boards[i]))
        data = {
            "game_id": game.game_id,
            "players": game.players,
            "boards": serialized_boards,
            "ready": game.ready,
            "turn": game.turn,
            "who_started": game.who_started,
            "allowed_ships": game.allowed_ships,
            "who_won": game.who_won,
        }
        return data

    @staticmethod
    def deserialize(game_state):
        unparsed_boards = game_state.get("boards")
        board_objects = []
        for board in unparsed_boards:
            board_objects.append(Board.deserialize(board))
        game_id = game_state.get("game_id")
        players = game_state.get("players", [])
        ready = game_state.get("ready", [False, False])
        turn = game_state.get("turn", 1)
        who_started = game_state.get("who_started", 1)
        allowed_ships = game_state.get("allowed_ships", {})
        who_won = game_state.get("who_won")
        return Game(
            boards=board_objects,
            game_id=game_id,
            players=players,
            ready=ready,
            turn=turn,
            who_started=who_started,
            allowed_ships=allowed_ships,
            who_won=who_won,
        )
