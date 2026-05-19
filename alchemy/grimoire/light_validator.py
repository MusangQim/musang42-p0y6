from alchemy.grimoire.light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str):
    allowed = light_spell_allowed_ingredients()
    lowcase = ingredients.lower()
    if any(item in lowcase for item in allowed):
        return (f"ingredients [{ingredients}]: VALID")
    return (f"ingredients [{ingredients}]: INVALID")
