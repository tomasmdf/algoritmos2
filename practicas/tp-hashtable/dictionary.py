from algo1 import *


class dictionaryNode:
    value = None
    key = None

"""
insert(D, key, value)
Descripción: Inserta un key en una posición determinada por la función de hash (1)  en el diccionario (dictionary). Resolver colisiones por encadenamiento.
Entrada: el diccionario sobre el cual se quiere realizar la inserción  y el valor del key a insertar. 
Salida: Devuelve D
"""


"""
search(D,key)
	Descripción: Busca un key en el diccionario
Entrada: El diccionario sobre el cual se quiere realizar la búsqueda (dictionary) y el valor del key a buscar.
Salida: Devuelve el value de la key.  Devuelve None si el key no se encuentra.
"""


"""
delete(D,key)
Descripción: Elimina un key en la posición determinada por la función de hash (1) del diccionario (dictionary) 
Poscondición: Se debe marcar como None  el key a eliminar.  
Entrada: El diccionario sobre el se quiere realizar la eliminación  y el valor del key que se va a eliminar.
Salida: Devuelve D
"""



dictionary = Array(9,None)