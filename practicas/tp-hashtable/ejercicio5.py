"""
Ejercicio 5
Implemente un algoritmo que devuelva True si la lista que recibe de entrada tiene todos sus elementos únicos, y Falso en caso contrario. Justificar el costo en tiempo de la solución propuesta.

Ejemplo 1:
Entrada: L = [1,5,12,1,2]
Salida: Falso, L no tiene todos sus elementos únicos, el 1 se repite en la 1ra y 4ta posición
"""
from dictionary import * 

def repeatsNumbers(arr):

    #por cada numero del arr primero busco si esta en la tabla
    #   si esta devuelve false
    #   si no esta lo agrego y sigo
    dictionary = createDictionary(9)

    for x in arr:
        #mostrar_diccionario(dictionary)
        if search(dictionary, x) != None:
            return False
        else:
            insert(dictionary, x, x)

    return True


print(repeatsNumbers([1,2,45,1]))
