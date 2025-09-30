from linkedlist import *
""""
push(S,element)
Descripción: Agrega un elemento al comienzo de S, siendo S una
estructura de tipo LinkedList
Entrada: La pila S sobre la cual se quiere agregar el elemento
(LinkedList) y el valor del elemento (element) a agregar.
Salida: No hay salida definida
"""
"""
Los elementos se van apilando uno arriba del otro, entonces push crea un nuevo nodo con el elemento a añadir y se lo asigna al head
"""


def push(S, element):
    NewNode = Node()
    NewNode.value = element
    currentNode = S.head
    S.head = NewNode
    NewNode.nextNode = currentNode




"""
pop(S)
Descripción: extrae el primer elemento de la pila S, siendo S
una estructura de tipo LinkedList
Poscondición: Se debe desvincular el Node a eliminar.
Entrada: la pila S (Linkedlist) sobre el cual se quiere realizar
la eliminación
Salida: Devuelve el elemento eliminado. Devuelve None si la pila
está vacía.
"""

def pop(S):
    if S.head!=None:
        element = S.head.value  
        currentNode=S.head.nextNode
        S.head=currentNode
        return element
    else:
        return None