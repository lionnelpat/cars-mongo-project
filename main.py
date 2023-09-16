import pymongo


myClient = pymongo.MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.8.2")

db = myClient["car_mongo_db"]
brands =  db["brands"]
models = db["models"]
cars = db["cars"]
drivers = db["drivers"]

def show_brands():

    my_brands = brands.find({},{"_id":0})
    for brand in my_brands:
        print(brand["name"])

def add_brand():
    name = input("Enter a name: ")
    description = input("Enter a description: ")
    country = input("Enter a country: ")
    location = input("Enter a location: ")

    res = brands.insert_one({
        "name": name, 
        "decription": description,
        "country": country,
        "location": location
        })
    
    print(f"new brand was inserted with _id : {res.inserted_id}") 

def update_brand():
    new_location = input("Enter new location: ")

    query = {"name": "mercedes"}
    new_values = {"$set": {"location": new_location}}

    brands.update_one(query,new_values)
    print(" brand with name mercedes was successfully updated") 

def delete_brand():
    print("delete brand") 


def menu():
    print("""
        1- to show brands 
        2- to add new brand 
        3- to update brand by name
        4- to delete brand
        5- to quit the program
        """)


menu()

choice = int(input("Enter your choice between 1 and 5: "))
while choice in range(6):
    if choice == 1: 
        show_brands()  
    elif choice == 2: 
        add_brand()
    elif choice == 3:
        update_brand()
    elif choice == 4:
        delete_brand()
    elif choice == 5:
        break
    else: 
        print("Entrez un nombre entre 1 et 5")

    menu()
    choice = int(input("Enter your choice between 1 and 5: "))   
