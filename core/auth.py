from flask_login import LoginManager
from lib.auth import find_by_username

def initialize_auth(app):
    # Login auth manager.
    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(username):
        return find_by_username(username)
