from math import *

"""
Ejercicio 3
Considerar una tabla hash de tamaño m = 1000 y una función de hash correspondiente al método de la multiplicación donde A = (sqrt(5)-1)/2). Calcular las ubicaciones para las claves 61,62,63,64 y 65.
"""

def hashMultiplicacion(key, m):
    A = (sqrt(5)-1)/2

    return floor(m*(key*A - floor(key*A)))

for n in range(61, 66):
    print('n:', n, ', slot:', hashMultiplicacion(n, 1000))

"""
n: 61 , slot: 700
n: 62 , slot: 318
n: 63 , slot: 936
n: 64 , slot: 554
n: 65 , slot: 172
"""