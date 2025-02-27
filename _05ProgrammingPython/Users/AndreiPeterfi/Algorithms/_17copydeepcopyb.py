lista1 = ["Marcel", "Godja", "Ioana"]

lista2 = list(lista1)
lista3 = lista1
# lista2 = ["Marcel", "Godja" ,"Ioana"]
# lista 1 = [100, 200, 300]
# lista 2 = [100, 200, 300]

print(lista1 is lista2)  # False
print(lista1 is lista3)  # False
print(lista1 == lista2)

print(lista1[0] is lista2[0])
lista2[0] = "George"

# lista 2 = [400, 200, 300]
print(lista1)

lista3[0] = "aa"
print(lista1)
