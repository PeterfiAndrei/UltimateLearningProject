import copy
#######String
####cum se fac arrayurile
#fprint
# lista1 = ["Andrei","Calin","Radu"]
# lista2 = lista1
# lista3 = lista1.copy()
# lista4 = copy.deepcopy(lista1)

print("---------------------")
lista5 = [["Andrei","Calin"],["Calin","Alex"],["Andrei","Alex"]]
# O100      = [ t1   , t2    , t3   ]
# 0100      = [e1.e2 , e3.e4 , e5.e6]

#Copy
# O200      = [ t1   , t2    , t3   ]
# 01        = [e1.e2 , e3.e4 , e5.e6]

#DeepCopy
# O300      = [ t7   , t8    , t9     ]
# 01      = [e7.e8 , e9e10 , e11.e12]

# == -> inseamna are aceleasi valori
# is -> inseamna ca au aceasi referinta

listaSimpla = ["a","b","c","d"]

listaSimpla2 = listaSimpla
print(listaSimpla2 == listaSimpla) #True
print(listaSimpla2 is listaSimpla) #True

#modificam lista 2
listaSimpla2[1] = "zz"
#afisam lista 1
print(listaSimpla) # am stricat si lista 1
listaSimpla3 = list(listaSimpla) #Se creaza o lista noua(de nivel1)
print(listaSimpla3 == listaSimpla) #True
print(listaSimpla3 is listaSimpla) #False
listaSimpla3[3] = "qq"
print(listaSimpla)


listaSimpla4 = listaSimpla.copy()
listaSimpla4[0] = "ww"
print(listaSimpla)






listaComplexa = [["Andrei","Calin","Blana"],["Calin","Alex"],["Andrei","Alex"]]
listaComplexa2 = copy.copy(listaComplexa)
print(listaComplexa == listaComplexa2) #True
print(listaComplexa is listaComplexa2) #False
# listaComplexa2[0][0] = "zz"
# listaComplexa2[0] = ["Luca","Luca","Luca"]
# print(listaComplexa)
print(listaComplexa[0] == listaComplexa2[0])
print(listaComplexa is listaComplexa2)          #False, verifica adresa  variabilei
print(listaComplexa[0] is listaComplexa2[0])    #True,










# 02-copy = [ t1 , t2 , t3 ]
# lista7 = lista5
# lista6 = copy.copy(lista5)
#
# print(lista5 == lista6) #True
# print(lista5 is lista6) #False
# print(lista5 is lista7) #True
#


# print(lista1 == lista2)         #True, verifica daca contin aceleasi elemente
# print(lista1 is lista2)         #True, pointeaza spre acelasi loc in memorie
#
# print(lista1 == lista3)         #True, au aceleasi valori
# print(lista1 is lista3)         #True


######################

# lista7 = copy.copy(lista5)
# print("7",lista5 is lista7)
#
# #   5->>100->>501,502,503
# #   7->>101->>501,502,503
# #  d7->>101-->601,602,603
#
#
# print(lista5)
# print(lista7)
# print("liste:",lista5 is lista7)               #False,
# print("elemente:",lista5[0] is lista7[0])
# lista5[0][0] ="Rares"
# print(lista7)
# print(lista5)



