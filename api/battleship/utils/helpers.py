import random
import string


def generate_unique_code():
    """
    Generates a unique code for the room
    """
    characters = string.ascii_letters + string.digits
    code = "".join(random.choice(characters) for _ in range(8))
    return code


def validate_coordinate_input(coordinates):
    if type(coordinates) != list:
        raise ValueError("Invalid coordinate data type.")
    for coord in coordinates:
        if not isinstance(coord, list) or len(coord) != 2:
            raise ValueError("Invalid coordinate format. Expected [x, y] format.")
        if not all(isinstance(val, int) and val >= 0 for val in coord):
            raise ValueError(
                "Invalid coordinate value. Coordinates must be non-negative integers."
            )