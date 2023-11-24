import random
from typing import Tuple


characters = "abcdefghijklmnopqrstuvwxyz   ."


def get_text(chamber: int, wall: int, shelf: int, volume: int) -> str:
    """Returns the text from the library of Babel given the parameters

    Args:
        chamber (int): Chamber in the tower of Babel, can be any int >= 0
        wall (int): Which wall to use, must be on one of 0-3
        shelf (int): Which shelf to use, must be 0-4
        volume (int): Which volume to use, must be 0-31

    Returns:
        str: Text in the volume in the specified location
    """

    # if (
    #     wall not in [0, 1, 2, 3]
    #     or shelf not in [0, 1, 2, 3, 4]
    #     or volume not in [i for i in range(32)]
    # ):
    #     raise ValueError("Parameters are not in the correct range")

    seed = chamber * 640 + wall * 160 + shelf * 32 + volume
    random.seed(seed)

    return_text = ""
    for i in range(40):
        return_text += "".join(random.choices(characters, k=80)) + "\n"

    return return_text


def find_str(str_to_find: str) -> Tuple[int, int, int, int]:
    """Finds the first occurence of the input string in the Library of Babel

    Args:
        str_to_find (str): String to find

    Returns:
        Tuple[int, int, int, int]: Location of string given by chamber, wall, shelf, volume
    """

    i = 0

    while True:
        for j in range(4):
            for k in range(5):
                for l in range(32):
                    if str_to_find in get_text(i, j, k, l):
                        return (i, j, k, l)
        i += 1


def show_str(str_to_show: str) -> str:
    pass
