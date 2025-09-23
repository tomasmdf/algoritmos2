"""
Ejercicio 9
Considerar los conjuntos de enteros S = {s1, . . . , sn} y T = {t1, . . . , tm}. Implemente un algoritmo que utilice una tabla de hash para determinar si S ⊆ T (S subconjunto de T). ¿Cuál es la complejidad temporal del caso promedio del algoritmo propuesto?
"""

from dictionary import *

#algoritmo que por medio de una hashtable determina si los elementos de S estan en T

#Complejidad temporal O(len(s) + len(t))

def isSubSet(s, t):

    dicc = createDictionary(9)

    for x in t:
        insert(dicc, x, x)

    mostrar_diccionario(dicc)

    for y in s:
        if search(dicc, y) == None:
            return False
        
    return True


print(isSubSet([2,4,5], [2,3,4,5]))



