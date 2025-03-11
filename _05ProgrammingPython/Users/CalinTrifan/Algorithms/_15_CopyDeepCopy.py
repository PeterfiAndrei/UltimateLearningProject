import copy

lista1 = ["matei", "george", "ionut", "marcel"]

lista2 = lista1

print(lista1 == lista2)
print(lista1 is lista2)

lista2.append("mihai")
print("lista1:", lista1)
print("lista2:", lista2)
print("***********************")

#############################################################################

lista3 = copy.copy(lista1)

print(lista3 == lista1)  # true pentru ca compara elementele din lista
print(lista3 is lista1)  # false pentru ca 'copy' a creat o lista noua in alta parte( la o alta adresa )
lista3.append("vlad")
print("lista1:", lista1)
print("lista3:", lista3)
print("***********************")

#############################################################################

lista4 = copy.deepcopy(lista1)
print(lista4 == lista1)  # true pentru ca compara elementele din lista
print(lista4 is lista1)  # false desi au acelasi valori ( au adresele adreselor  diferite )

#############################################################################
