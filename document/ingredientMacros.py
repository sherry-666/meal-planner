from mongoengine import *

class IngredientMacros(Document):
    name = StringField(required=True)
    measurement = StringField(required=True)

    carbs = FloatField(required=True)
    fat = FloatField(required=True)
    protein = FloatField(required=True)
    cal = FloatField(required=True)

