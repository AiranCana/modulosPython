from .elements import create_air, create_earth
from elements import create_fire, create_water


def healing_potion() -> str:
    e = (f"Healing potion brewed with '{create_fire()}'" +
         f" and '{create_water()}'")
    return e


def strength_potion() -> str:
    e = ("Strength potion brewed " +
         f"with '{create_earth()}' and '{create_air()}'")
    return e
