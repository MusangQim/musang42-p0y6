def validate_ingredients(ingredients: str):
    allowed = ["earth", "air", "fire", "water"]
    lowcase = ingredients.lower()
    if any(item in lowcase for item in allowed):
        return (f"{ingredients} - VALID")
    return (f"{ingredients} - INVALID")
