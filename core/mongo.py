from mongoengine import connect

def initialize_mongo():
    # client = pymongo.MongoClient(
    #     "mongodb+srv://admin:<password>@cluster0.yrmdx.mongodb.net/<dbname>?retryWrites=true&w=majority")
    # db = client.test

    connect(
        host = "mongodb+srv://cluster0.yrmdx.mongodb.net/?retryWrites=true&w=majority",
        username = "admin",
        password = "sherryjing",
        db = "meal_planer",
    )

    print("conenect successfully")

