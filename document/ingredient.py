class Ingredient():
    #constructor
    def __init__(self, name, measurement, quantity=1):
        self.name = name
        self.measurement = measurement
        if quantity < 0:
            raise Exception("quantity can not be negative")
        self.quantity = quantity

    #define this document is on global level
    @staticmethod
    def get_ingredients():
        return [Ingredient("salt","g",10),Ingredient("sugar","g")]

    def display(self):
        return (",".join([str(self.quantity),self.measurement,self.name]))

