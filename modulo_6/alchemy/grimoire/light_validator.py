from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    lis = light_spell_allowed_ingredients()
    for element in lis:
        if element in ingredients:
            return "VALID"
    return "INVALID"
