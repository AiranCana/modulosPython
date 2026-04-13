from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    lis = dark_spell_allowed_ingredients()
    for element in lis:
        if element in ingredients:
            return "VALID"
    return "INVALID"
