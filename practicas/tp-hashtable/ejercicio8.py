"""
Ejercicio 8
Se requiere encontrar la primera ocurrencia de un string p1...pk en uno más largo a1...aL. Implementar esta estrategia de la forma más eficiente posible con un costo computacional menor a O(K*L) (solución por fuerza bruta).  Justificar el coste en tiempo de la solución propuesta.

Ejemplo 1:
Entrada: S = ‘abracadabra’ , P = ‘cada’
Salida: 4, índice de la primera ocurrencia de P dentro de S (abracadabra)
"""

"""
-dividir S en todas las subcadenas de tamaño P posibles, ej: abra, brac, raca, etc
    -para cada subcadena de S hago la suma de caracteres ASCII y la guardo en un hashtable
        -cada nodo tiene key, value y index
            -ej: key=xxx, value=abra, index=0
            -    key=xxx, value=brac, index=1
        
        -hago h(P) y acceso a ese indice y comparo los campos values que hayan, si son iguales devuelvo el campo index

"""