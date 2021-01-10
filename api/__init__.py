from api.ingredient import ingredient_bp
from api.recipe import recipe_bp
from api.auth import auth_bp
from api.profile import profile_bp

blueprints = [
    ingredient_bp,
    recipe_bp,
    auth_bp,
    profile_bp,
]