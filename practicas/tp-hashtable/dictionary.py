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

    if D[slotToInsert]  == None or D[slotToInsert]  == 'deleted': #slot vacio
        D[slotToInsert] = node

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

    #print(type(slot) is list)

    if type(slot) is list:
        for n in range(0, len(slot)):
            if slot[n].key == key:
                return slot[n].value
            
    elif slot != None and slot != 'deleted':

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

    slot = D[hashResto(key, len(D))]

    if type(slot) is list:
        for n in range(0, len(slot)):
            if slot[n].key == key:

                if len(slot) == 1:
                    D[hashResto(key, len(D))] = None
                else:
                    slot.remove(slot[n])
                break

    elif slot != None:
        if slot.key == key:
            print(slot.value)
            D[hashResto(key, len(D))] = 'deleted'

    return D



def mostrar_diccionario(diccionario):
    """Muestra el contenido del diccionario (lista de buckets con dictionaryNode)."""
    for i, bucket in enumerate(diccionario):
        print(f"Bucket {i}: ", end="")
        if bucket is None or bucket == 'deleted':
            print("vacío")
        elif isinstance(bucket, list):
            for node in bucket:
                print(f"[{node.key} : {node.value}]", end=" ")
            print()
        else:  # es un solo dictionaryNode
            print(f"[{bucket.key} : {bucket.value}]")




"""m=9
dictionary = createDictionary(9)
insert(dictionary, 2, 'casa')
insert(dictionary, 5, 'cason')
insert(dictionary, 6, 'casota')
insert(dictionary, 11, 'choza')
insert(dictionary, 21, 'chazo')
insert(dictionary, 20, 'cha3o')
#mostrar_diccionario(dictionary)

delete(dictionary, 6)
delete(dictionary, 2)
delete(dictionary, 11)
#delete(dictionary, 20)
mostrar_diccionario(dictionary)


print(search(dictionary, 5))"""