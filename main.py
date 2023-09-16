import pymongo


myClient = pymongo.MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.8.2")

db = myClient["car_mongo_db"]
brands =  db["brands"]
models = db["models"]
cars = db["cars"]
drivers = db["drivers"]


br = brands.insert_one({
    "name": "WV",
    "country": "germany",
    "description": "lorem ipsum dolor et",
    "location": "Berlin"
})

print(br.inserted_id)








print("Welcome to cars mongo project")