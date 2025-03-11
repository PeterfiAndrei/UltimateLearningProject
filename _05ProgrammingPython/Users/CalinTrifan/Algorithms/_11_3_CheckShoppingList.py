homeFood = {
    "carrot": 5,
    "rice": -4,
    "banana": 5,
    "bread": 20,
    "cheese": -2,
    "tomato": 0,
    "potato": -3,
    "chicken": -6,
    "nuts": 18,
    "apple": 33,
    "pasta": -1,
    "yogurt": -20,
    "milk": -22,
    "fish": -10,
    "egg": 2
}
groceryFood = {
    "apple": 10,
    "milk": 0,
    "egg": 0,
    "tomato": 0,
    "potato": 55,
    "fish": 4,
    "nuts": 4,
    "shrimp": 5,
    "beef": 0,
    "banana": 12,
    "asparagus": 9,
    "orange": 22,
    "grape": 100,
    "watermelon": 2,
    "carrot": 3,
    "bread": 2,
    "yogurt": 32,
    "cheese": 22,
    "chicken": 1,
    "rice": 5,
    "pasta": 33,
    "pork": 88,
    "pepper": 1,
    "cabbage": 0,
    "spinach": 0,
    "mushroom": 0,
    "lamb": 0,
    "turkey": 23,
    "duck": 22,
    "lobster": 1,
    "crab": 4,
    "salmon": 2,
    "tuna": 5,
    "lettuce": 3,
    "cucumber": 2,
    "onion": 1,
    "garlic": 0,
    "zucchini": 66,
    "peach": 3,
    "pear": 23,
    "plum": 3,
    "cherry": 1,
    "strawberry": 0,
    "blueberry": 0,
    "raspberry": 0
}


def checkStoreStocks(home, store):
    rezultatShopping = {}
    for key, value in home.items():
        if value < 0:
            if abs(value) < store.get(key):
                rezultatShopping[key] = 0
            else:
                rezultatShopping[key] = value + store.get(key)

    return rezultatShopping


print(checkStoreStocks(homeFood, groceryFood))
