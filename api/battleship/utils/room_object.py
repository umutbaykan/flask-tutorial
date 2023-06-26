ROOMS = {}
PLAYERS = {"online_users": 0}

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
        return True
    else:
        return False
    

def remove_player_from_game(room_id, player_id):
    """
    Removes a player's id from the game
    """
    global ROOMS
    current_players = ROOMS[room_id].get("players", [])
    if player_id in current_players:
        ROOMS[room_id]['players'].remove(player_id)
    


def room_event_is_from_users_within_room_object(room_id=None, player_id=None, *args):
    """
    Checks whether event is coming from a player in the room
    and none of the other additional parameters are none
    """
    if any(arg is None for arg in args):
        return False
    if room_id is None or player_id is None:
        return False
    current_players = ROOMS[room_id].get("players", [])
    return True if player_id in current_players else False
        

def check_global_game_id_is_unique(room_id):
    """
    Checks if the given id is already in the global room object
    Returns a boolean value
    """
    if room_id in ROOMS:
        return False
    return True
