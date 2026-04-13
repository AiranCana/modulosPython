from alchemy.elements import create_air as air
from elements import create_fire as fire
from ..potions import strength_potion as strength


def lead_to_gold() -> str:
    return ("Recipe transmuting Lead to Gold: brew" +
            f"'{air()}' and '{strength()}' mixed with '{fire()}'")
