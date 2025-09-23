from algo1 import *


class dictionaryNode:
    value = None
    key = None
    

def hashResto(key, m):

    if type(key) is str:
        if len(key) == 1:
            return ord(key) % m
        else:
            return len(key) % m

    return key % m


#crea dictionario de tamaño m con listas de python
def createDictionary(m):
    dictionary = [None]*m

    return dictionary


"""
insert(D, key, value)
Descripción: Inserta un key en una posición determinada por la función de hash (1)  en el diccionario (dictionary). Resolver colisiones por encadenamiento.
Entrada: el diccionario sobre el cual se quiere realizar la inserción  y el valor del key a insertar. 
Salida: Devuelve D
"""

def insert(D, key, value):

    slotToInsert = hashResto(key, len(D))

    node = dictionaryNode()
    node.key = key
    node.value = value

    if D[slotToInsert]  == None: #slot vacio
        D[slotToInsert] = key

    elif type(D[slotToInsert]) is list: #si hay mas de un elemento en el slot
        D[slotToInsert].append(node)

    else:
        D[slotToInsert] = [D[slotToInsert]] 
        D[slotToInsert].append(node)

    return D

"""
search(D,key)
	Descripción: Busca un key en el diccionario
Entrada: El diccionario sobre el cual se quiere realizar la búsqueda (dictionary) y el valor del key a buscar.
Salida: Devuelve el value de la key.  Devuelve None si el key no se encuentra.
"""

def search(D, key):
    slot = D[hashResto(key, len(D))]

    if type(slot) is list:
        for n in range(0, len(slot)):
            if slot[n] == key:
                return slot[n].value
            
    if slot != None:

        if slot.key == key:
            return slot.value
        
    return None


"""
delete(D,key)
Descripción: Elimina un key en la posición determinada por la función de hash (1) del diccionario (dictionary) 
Poscondición: Se debe marcar como None  el key a eliminar.  
Entrada: El diccionario sobre el se quiere realizar la eliminación  y el valor del key que se va a eliminar.
Salida: Devuelve D
"""


def delete(D, key):
    return 




m=9
dictionary = createDictionary(9)

print(len("ke"))