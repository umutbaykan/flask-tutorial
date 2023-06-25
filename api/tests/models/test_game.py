import pytest
import os
# from battleship.models.board import *
# from battleship.models.ship import *
from battleship.models.game import *

def test_game_initialization():
    test_directory = os.path.dirname(os.path.abspath(__file__))
    json_file_path = os.path.join(
        test_directory, "..", "seeds", "model_objects", "game_regular_configs.json"
    )   
    with open(json_file_path) as file:
        json_data = file.read()
        game = Game.create_new_game_from_configs(json_data)
        assert game.gameId == "fkEjOpkL"
        assert game.p1_id == "6495822522b4741d1481b1c6"
        assert game.p2_id == None
        assert game.boards[0].size == 8
        assert game.boards[1].size == 8
        assert game.game_ready == False
        assert game.turn == 0
        assert game.who_started == 1
        assert game.allowed_ships == {"Destroyer": 1, "Cruiser": 2, "AircraftCarrier": 1}
        assert game.who_won == None