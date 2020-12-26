from mongoengine import *

class UserAuth(Document):
    username = StringField(required=True, primary_key=True)
    password = StringField(requirezd=True)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.username

    def to_dict(self):
        return {
            "username": self.username,
        }
