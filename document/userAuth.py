from mongoengine import *

class UserAuth(Document):
    username = StringField(required=True)
    password = StringField(requirezd=True)