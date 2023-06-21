import random
import string


def generate_unique_code():
    """
    Generates a unique code for the room
    """
    characters = string.ascii_letters + string.digits
    code = "".join(random.choice(characters) for _ in range(8))
    return code
