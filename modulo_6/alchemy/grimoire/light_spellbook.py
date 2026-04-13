def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    from .light_validator import validate_ingredients
    val = validate_ingredients(ingredients)
    c = f"Spell recorded {spell_name} ({ingredients} - {val})"
    return c
