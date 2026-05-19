from alchemy.grimoire.dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str):
    allowed = dark_spell_allowed_ingredients()
    lowcase = ingredients.lower()
    if any(item in lowcase for item in allowed):
        return (f"ingredients [{ingredients}]: VALID")
    return (f"ingredients [{ingredients}]: INVALID")
