homeFood = {
    "carrot": True,
    "rice": True,
    "banana": True,
    "bread": False,
    "cheese": False,
    "tomato": True,
    "potato": False,
    "chicken": True,
    "nuts": True,
    "apple": False,
    "pasta": True,
    "yogurt": False,
    "milk": False,
    "fish": True,
    "egg": True,
    1: "Blana"
    }
groceryFood = {
    "apple": True,
    "milk": True,
    "egg": True,
    "tomato": False,
    "potato": True,
    "fish": True,
    "nuts": False,
    "shrimp": True,
    "beef": True,
    "banana": True,
    "asparagus": True,
    "orange": True,
    "grape": True,
    "watermelon": True,
    "carrot": False,
    "bread": False,
    "yogurt": True,
    "cheese": True,
    "chicken": True,
    "rice": True,
    "pasta": True,
    "pork": False,
    "pepper": False,
    "cabbage": True,
    "spinach": True,
    "mushroom": True,
    "lamb": True,
    "turkey": True,
    "duck": True,
    "lobster": True,
    "crab": False,
    "salmon": True,
    "tuna": True,
    "lettuce": True,
    "cucumber": True,
    "onion": True,
    "garlic": True,
    "zucchini": True,
    "peach": True,
    "pear": True,
    "plum": True,
    "cherry": True,
    "strawberry": True,
    "blueberry": True,
    "raspberry": True
}

buyingList_dict = {}
def checkAvailableStoreMissingFood(dict_homeFood, dict_storeFood):
    for key,value in dict_homeFood.items():   #Asa se parcurge cu dictionar, cu cheie-valoare
        if value == False:
            buyingList_dict[key] = dict_storeFood.get(key)
    return buyingList_dict
# print(checkAvailableStoreMissingFood(homeFood,groceryFood))
print("Missing items from home and availability in store:", dict(sorted((checkAvailableStoreMissingFood(homeFood,groceryFood).items()))))
