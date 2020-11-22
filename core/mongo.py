from mongoengine import connect

def initialize_mongo(mongo_config):
    connect(
        host = "mongodb+srv://cluster0.yrmdx.mongodb.net/?retryWrites=true&w=majority",
        username = mongo_config["username"],
        password = mongo_config["password"],
        db = "meal_planer",
    )

    print("Connected to Mongo...")

