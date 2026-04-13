from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    val = validate_ingredients(ingredients)
    c = f"Spell recorded {spell_name} ({ingredients} - {val})"
    return c
