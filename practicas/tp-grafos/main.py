from algo1 import *
from linkedlist import *
from mystack import * 

#Vertex = vertices, Edges: Aristas

def printGraph(G):
    tam = len(G)
    for n in range(0, tam):
        currentNode = G[n].head
        print("Conexiones del vertice:", n)
        print("[", end="")
        
        while currentNode != None:

            if currentNode.nextNode != None:
                print(str(currentNode.value) + ", ", end="")
            else:
                print(str(currentNode.value), end="")
            currentNode = currentNode.nextNode

        print("]")

"""
Ejercicio 1

def createGraph(List, List) 
Descripción: Implementa la operación crear grafo
Entrada: LinkedList con la lista de vértices y LinkedList con la lista de aristas donde por cada par de elementos representa una conexión entre dos vértices.
Salida: retorna el nuevo grafo

"""

def createGraph(vert, edges):
    #vert = linkedlist con los vertices
    #edges = linkedlist con los pares (vi,vj)

    size = length(vert)
    #Crea grafo por lista de adyacencia
    Graph = Array(size,LinkedList())

    #inicializa el grafo
    for n in range(0,size):
        Graph[n] = LinkedList() 

    #(A,B)
    currentNode = edges.head
    while currentNode != None:
        add(Graph[currentNode.value[0]], currentNode.value[1])
        add(Graph[currentNode.value[1]], currentNode.value[0])
        currentNode = currentNode.nextNode

    return Graph


"""
Ejercicio 2
Implementar la función que responde a la siguiente especificación.

def existPath(Grafo, v1, v2): 
Descripción: Implementa la operación existe camino que busca si existe un camino entre los vértices v1 y v2 
Entrada: Grafo con la representación de Lista de Adyacencia, v1 y v2 vértices en el grafo.
Salida: retorna True si existe camino entre v1 y v2, False en caso contrario.

Empiezo por el vertice destino, meto en una pila los vertices por visitar y en otro arr los visitados
hago pop() por cada elemento de la pila y dentro de cada vertice verifico si es el vertice de origen, si no es
repito el procedimiento
"""



def existPathR(graph, initialVert, actualVert, stack, visitedArr):

    if length(stack) > 0:
        actualVert = pop(stack)

        visitedArr.append(actualVert)

        #mostrarLinkedList(stack)
        #print('actualVert', actualVert)

        #se encontro un camino
        if actualVert == initialVert:
            return True
        elif length(stack) >= 0:

            if graph[actualVert]:
                currentNode = graph[actualVert].head

                #print(mostrarLinkedList(graph[actualVert]))
                while currentNode != None:
                    if search(stack, currentNode.value) == None and not(currentNode.value in visitedArr):
                        push(stack, currentNode.value)

                    currentNode = currentNode.nextNode

                return existPathR(graph, initialVert, actualVert, stack, visitedArr)


    return False

def existPath(graph, initialVert, finalVert):

    stack = LinkedList()

    currentNode = graph[finalVert].head

    while currentNode != None:
        push(stack, currentNode.value)
        currentNode = currentNode.nextNode
        
    #mostrarLinkedList(stack)

    return existPathR(graph, initialVert, finalVert, stack, [finalVert])




"""
Ejercicio 3
Implementar la función que responde a la siguiente especificación.
def isConnected(Grafo): 
Descripción: Implementa la operación es conexo 
Entrada: Grafo con la representación de Lista de Adyacencia.
Salida: retorna True si existe camino entre todo par de vértices, False en caso contrario.

por cada vertice ejecuta existsPath() mientras se devuelva true
"""

def isConnected(graph):
    #print(len(graph))
    for i in range(len(graph)-1):
        for j in range(i+1, len(graph)):
            if existPath(graph, i, j) != True:
                return False
            
    return True

"""
Ejercicio 4
Implementar la función que responde a la siguiente especificación.
def isTree(Grafo): 
Descripción: Implementa la operación es árbol 
Entrada: Grafo con la representación de Lista de Adyacencia.
Salida: retorna True si el grafo es un árbol.

Condicion suficiente para que sea arbol

Es conexo y tiene n-1 aristas, siendo n la cantidad de vertices

si isConnected devuelve true 
    len(graph) - 1 es la cantidad de aristas que tiene que tener para ser arbol


"""

def isTree(graph):
    #es arbol si es conexo y tiene n-1 aristas

    if isConnected(graph) == True:

        edgesNeeded = len(graph) - 1
        edgesArr = []

        for n in range(len(graph)-1):
            #print('n', n)
            #mostrarLinkedList(graph[n])

            currentNode = graph[n].head

            while currentNode != None:

                if ((n,currentNode.value) not in edgesArr) and ((currentNode.value,n) not in edgesArr):
                    edgesArr.append((n,currentNode.value))

                currentNode = currentNode.nextNode

        #print(edgesArr)

        if len(edgesArr) == edgesNeeded:
            return True

    return False


"""
Ejercicio 5 
Implementar la función que responde a la siguiente especificación.
def isComplete(Grafo): 
Descripción: Implementa la operación es completo 
Entrada: Grafo con la representación de Lista de Adyacencia.
Salida: retorna True si el grafo es completo.

Nota: Tener en cuenta que  un grafo es completo cuando existe una arista entre todo par de vértices.

para que sea completo todas las columnas tiene que ser de tamaño n-1, ya que no contienen ciclos

"""

def isComplete(graph):
    for i in range(len(graph)):
        if length(graph[i]) != len(graph)-1:
            return False
    return True


"""
Ejercicio 6
Implementar una función que dado un grafo devuelva una lista de aristas que si se eliminan el grafo se convierte en un árbol. Respetar la siguiente especificación. 

def convertTree(Grafo)
Descripción: Implementa la operación es convertir a árbol 
Entrada: Grafo con la representación de Lista de Adyacencia.
Salida: LinkedList de las aristas que se pueden eliminar y el grafo resultante se convierte en un árbol.

si ya es un arbol devuelve []

uso bfs

y devuelvo los arcos de retroceso

"""

def findUnnecesaryBranches(graph, branchesToDelete, TuplesArr):

    if not(isTree(graph)):

        for n in range(len(graph)-1):
            current = graph[n].head
            
            while current != None:

                edge = (min(n, current.value), max(n, current.value))

                if edge not in TuplesArr and search(branchesToDelete, edge) == None:

                    if any(t[0] == n for t in TuplesArr): # si ya existe alguna tupla (n,_)
                        add(branchesToDelete, edge)
                    else:
                        TuplesArr.append(edge)

                current = current.nextNode

    #print('tuples', TuplesArr)
    
    return mostrarLinkedList(branchesToDelete)


def convertTree(graph):
    return findUnnecesaryBranches(graph, LinkedList(), [])




"""
Ejercicio 7
Implementar la función que responde a la siguiente especificación.
def countConnections(Grafo):
Descripción: Implementa la operación cantidad de componentes conexas 
Entrada: Grafo con la representación de Lista de Adyacencia.
Salida: retorna el número de componentes conexas que componen el grafo.


Ejemplo

# Componente 1
(0,1), (1,2), (2,0)

# Componente 2
(3,4)

# El vértice 5 queda solo

en este caso tiene 3 componentes conexas


"""

def countConnections(graph):

    if isConnected(graph): # si es conexo tiene 1 componente conexa
        return 1
    else:
        #me fijo si desde n puedo ir a un nodo mayor (n+x) si no sumo 1 y empiezo desde cero
        
        return 



"""

GRAFO CONEXO




"""

"""

GRAFO NO CONEXO 

Componente 1:   0 — 1
                  \ |
                    2

Componente 2:   3 — 4

Componente 3:   5


vertices = LinkedList()
add(vertices, 5)
add(vertices, 4)
add(vertices, 3)
add(vertices, 2)
add(vertices, 1)
add(vertices, 0)

edges = LinkedList()
# componente 1
add(edges, (0,1))
add(edges, (1,2))
add(edges, (2,0))

# componente 2
add(edges, (3,4))

"""




vertices = LinkedList()
add(vertices,4)
add(vertices,3)
add(vertices,2)
add(vertices,1)
add(vertices,0)


edges = LinkedList()
"""add(edges, (0,1))
add(edges, (0,4))
add(edges, (1,2))
add(edges, (1,3))
add(edges, (1,4))
add(edges, (2,3))
add(edges, (3,4))"""
add(edges, (1,2))
add(edges, (0,2))
add(edges, (0,1))

graph = createGraph(vertices, edges)

printGraph(graph)
print('-'*20)
print('len(graph):', len(graph))
print('Ejercicio-2-existPath:', existPath(graph, 0, 2))
print('Ejercicio-3-isConnected:', isConnected(graph))
print('Ejercicio-4-isTree:', isTree(graph))
print('Ejercicio-5-isComplete:', isComplete(graph))
print('Ejercicio-6-convertTree:', convertTree(graph))
print('Ejercicio-7-countConnections:', countConnections(graph))