from enum import Enum

class Meal():
    class Cuisine (Enum):
        ASIAN = 1
        CHINESE = 2
        JAPANESE = 3



    #constructor
    def __init__(self,name,serving,prep_time,cook_time,ingredients,instruction,cuisine,taste,dietary,level):
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
        if not isinstance(cuisine,Meal.Cuisine):
            raise Exception("%s is not in Cuisine List"%cuisine)
        self.cuisine = cuisine
        self.taste = taste #spicy,sweet,savoury
        self.dietary = dietary  #vegan, gluten free, vegetarian
        self.level = level#challenge level



    def get_ingredients(self):
        return self.ingredients