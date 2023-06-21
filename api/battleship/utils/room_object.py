ROOMS = {}


def create_new_game_state(room_id, configurations):
    """
    Updates the global room object with a new game state.
    Takes in two variables, ID of the room to update and game configurations.
    """
    global ROOMS
    ROOMS[room_id] = configurations


def add_player_to_game(room_id, player_id):
    """
    Adds a player to the game based on their user ID stored
    in session (which is their DB id)
    """
    global ROOMS
    current_players = ROOMS[room_id].get("players", [])
    if len(current_players) < 2:
        current_players.append(player_id)
        ROOMS[room_id]["players"] = current_players
    else:
        return False


def list_all_rooms():
    """Returns all the available rooms in the global room object"""
    return ROOMS


def check_global_game_id_is_unique(room_id):
    """
    Checks if the given id is already in the global room object
    Returns a boolean value
    """
    if room_id in ROOMS:
        return False
    return True
