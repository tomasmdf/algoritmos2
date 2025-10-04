from algo1 import *
from linkedlist import *
from mystack import * 
from myqueue import *
import math

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
        #meto las aristas visitadas en un array y voy recorriendo las distintas aristas no visitadas
        vert = len(graph)
        
        visited = [False]*vert
        components = 0

        for v in range(vert):
            if not visited[v]:
                # Si el vértice no fue visitado, arranca una nueva componente
                components += 1
                stack = [v]         # usamos pila para DFS

                while stack:
                    node = stack.pop()
                    if not visited[node]:
                        visited[node] = True

                        # recorremos los vecinos en la lista de adyacencia
                        current = graph[node].head
                        while current is not None:
                            if not visited[current.value]:
                                stack.append(current.value)
                            current = current.nextNode



        return components



"""
Ejercicio 8
Implementar la función que responde a la siguiente especificación.
def convertToBFSTree(Grafo, v):
Descripción: Convierte un grafo en un árbol BFS
Entrada: Grafo con la representación de Lista de Adyacencia, v vértice que representa la raíz del árbol
Salida: Devuelve una Lista de Adyacencia con la representación BFS del grafo recibido usando v como raíz.
"""

class BFSNode:
    id = None
    color = None
    parent = None
    distance = None

"""
se usa white(recien descubierto), gray(descubierto por un vertice adyacente), black(se analizaron todos sus vertices 
adyacentes)

1- en un vertice x, lo marca como gris, y marca de blanco todos sus vertices adyacentes
me muevo a uno de sus vertices adyacentes, realizo 1, aumento en 1 la distancia
una vez analizado todos los vert. adyacentes marco el vertice x como black

sigo con los vertices grises hasta que no quede ninguno gris
"""


def convertToBFSTree(graph, v):

    return


"""
Ejercicio 9
Implementar la función que responde a la siguiente especificación.
def convertToDFSTree(Grafo, v):
Descripción: Convierte un grafo en un árbol DFS
Entrada: Grafo con la representación de Lista de Adyacencia, v vértice que representa la raíz del árbol
Salida: Devuelve una Lista de Adyacencia con la representación DFS del grafo recibido usando v como raíz.



Comienza por un vertice v cualquiera
    explora hacia abajo mientras sea posible 
        explora las aristas del vertice v que descubrio mas recientemente
            deja de lado las aristas que estan en el mismo nivel de v para despues
                cuando no puede ir mas profundo, retrocede y sigue con las aristas pendientes
                    repite hasta descubrir todos los vertices


"""


"""

Ejercicio 10
Implementar la función que responde a la siguiente especificación.
def bestRoad(Grafo, v1, v2):
Descripción: Encuentra el camino más corto, en caso de existir, entre dos vértices.
Entrada: Grafo con la representación de Lista de Adyacencia, v1 y v2 vértices del grafo.
Salida: retorna la lista de vértices que representan el camino más corto entre v1 y v2. La lista resultante contiene al inicio a v1 y al final a v2. En caso que no exista camino se retorna la lista vacía.


aplico BFS desde el vertice v1

"""



"""
Ejercicio 12
Demuestre que si el grafo G es un árbol y se le agrega una arista nueva entre cualquier par de vértices se forma exactamente un ciclo y deja de ser un árbol.

"""

#Todo arbol tiene la propiedad de tener n-1 aristas siendo n la cantidad de vertices, luego si se agrega una arista
#cualquier dejaria de cumplir esta propiedad y por lo tanto dejaria de ser arbol 


"""
Ejercicio 13
Demuestre que si la arista (u,v) no pertenece al árbol BFS, entonces los niveles de u y v difieren a lo sumo en 1.
"""

#El algoritmo BFS por cada vertice u añade todas sus vertices adyacentes, luego si no existe la arista (u,v), siempre
#sus niveles van a diferir en a lo sumo 1

#Si existe el vertice (u,v), cuando estemos en el vertice u el algoritmo de BFS va a crear un hijo de u por cada 
#vertice adyacente de u, luego los niveles de u y v difererian en menos de 1


"""
Ejercicio 14
Implementar la función que responde a la siguiente especificación.
def PRIM(Grafo): 
Descripción: Implementa el algoritmo de PRIM 
Entrada: Grafo con la representación de Matriz de Adyacencia.
Salida: retorna el árbol abarcador de costo mínimo


se forman dos conjuntos disjuntos U y V-U
    se toma un vertice a se lo envia a U
        se busca la arista con menos peso y se mueve el vertice a U, siempre se tienen en cuenta todas las aristas 
        para elegir el menor
            se repite hasta vaciar el conjunto V-U
            
"""


"""
Ejercicio 15
Implementar la función que responde a la siguiente especificación.
def KRUSKAL(Grafo): 
Descripción: Implementa el algoritmo de KRUSKAL 
Entrada: Grafo con la representación de Matriz de Adyacencia.
Salida: retorna el árbol abarcador de costo mínimo

Primero se forma un conjunto por cada vertice del grafo
    Se ordenan por peso las distintas aristas 
        por cada par (u,v) se hace findSet(u) y findSet(v), y si son distintos (unen 2 componentes conexas)
        se inserta en el conjunto bosque A y se unen las 2 componentes conexas
    
"""

"""
Ejercicio 16
Demostrar que si la arista (u,v) de costo mínimo tiene un nodo en U y otro en V - U, entonces la arista (u,v) pertenece a un árbol abarcador de costo mínimo.
"""

#si existe la arista (u,v) de costo minimo donde u pertenece a U y v a V-U, entonces la arista (u,v) 
#obligatoriamente va a pertenecer al AACM 


"""
Ejercicio 17
Sea e la arista de mayor costo de algún ciclo de G(V,A) . Demuestre que existe un árbol abarcador de costo mínimo AACM(V,A-e) que también lo es de G.
"""

#sabemos que e es la arista de mayor costo de algun ciclo de G(V,A). Al formar el AACM, se forma un arbol abarcador
#cuya suma de aristas es la menor posible, luego el AACM(V, A-e) es un AACM de G ya que e es un ciclo, es decir que 
#no se va a tomar como arista de AACM y e es del mayor costo, por lo tanto va a existir otras aristas con suma menor

"""
Ejercicio 18
Demuestre que si unimos dos AACM por un arco (arista) de costo mínimo el resultado es un nuevo AACM. (Base del funcionamiento del algoritmo de Kruskal)
"""

#

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
#print('Ejercicio-6-convertTree:', convertTree(graph))
print('Ejercicio-7-countConnections:', countConnections(graph))