from algo1 import *
from linkedlist import *

"""
enqueue(Q,element)

Descripción: Agrega un elemento al comienzo de Q, siendo Q una
estructura de tipo LinkedList.
Entrada: La cola Q (LinkedList) sobre la cual se quiere agregar
el elemento y el valor del elemento (element) a agregar.
Salida: No hay salida definida.
"""

def enqueue(Q, element):
    add(Q, element)

"""
dequeue(Q)

Descripción: extrae el último elemento de la cola Q, siendo Q
una estructura de tipo LinkedList.
Poscondición: Se debe desvincular el Node a eliminar.
Entrada: la cola Q (Linkedlist) sobre el cual se quiere realizar
la eliminación.
Salida: Devuelve el elemento de la cola. Devuelve None si la
cola está vacía.
"""

def dequeue(Q):

    value = None

    if Q.head != None and length(Q) > 1:
        currentNode = Q.head
        while currentNode.nextNode.nextNode != None:
            currentNode = currentNode.nextNode
        
        value = currentNode.nextNode.value
        currentNode.nextNode = None

    elif Q.head != None and length(Q) == 1:

        value = Q.head.value
        Q.head = None   


    return value