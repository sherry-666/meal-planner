from enum import IntEnum
from mongoengine import *

from document.ingredient import Ingredient


class Meal(Document):
    class Cuisine (IntEnum):
        ASIAN = 1
        CHINESE = 2
        JAPANESE = 3

    name = StringField(required=True)
    serving = IntField(required=True)
    prep_time = IntField(required=False)
    cook_time = IntField(required=False)
    ingredients = ListField(EmbeddedDocumentField(Ingredient))
    instruction = StringField(required=False)
    cuisine = IntField(required=True)
    taste = StringField(required=False)
    dietary = StringField(required=False)
    level = IntField(required=False)

    #constructor
    def __init__(
            self,name,serving,prep_time,cook_time,
            ingredients,instruction,cuisine,taste,dietary,level
    ):
        super().__init__()
        self.name = name
        if serving < 0:
            raise Exception("serving must be positive")
        self.serving = serving
        if prep_time < 0:
            raise Exception("prep time must be positive")
        self.prep_time = prep_time
        if cook_time < 0:
            raise Exception("cook time must be positive")
        self.cook_time = cook_time
        self.total_time = cook_time + prep_time
        self.ingredients = ingredients
        self.instruction = instruction
        if cuisine not in list(map(int,Meal.Cuisine)):
            raise Exception("%s is not in Cuisine List"%cuisine)
        self.cuisine = cuisine
        self.taste = taste #spicy,sweet,savoury
        self.dietary = dietary  #vegan, gluten free, vegetarian
        self.level = level#challenge level



    def get_ingredients(self):
        return self.ingredients