homeFood = {
    "carrot": False,
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
    "egg": True
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
    "carrot": True,
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
vector = {
    0: "Andrei",
    1: "Calin"
}


def checkaVailableStoreMissingFood(dictionar1, dictionar2):
    print("dimensiunea este", len(dictionar1))

    rezultatDictionar = {}

    for food in dictionar1.items():  # asa parcurg dictionarul
        if dictionar1.get(food[0]) is False:  # asa verific daca in primul dictionar am elemente cu valoarea"false"
            rezultatDictionar[food[0]] = dictionar2.get(food[0])

            # if dictionar2.get(food[0]) == True:   # iau din dictionar cu 'get' rezultatul de la chei
            #     rezultatDictionar[food[0]] = True
            # else:
            #     rezultatDictionar[food[0]] = False

    return (rezultatDictionar)


print(checkaVailableStoreMissingFood(homeFood, groceryFood))
