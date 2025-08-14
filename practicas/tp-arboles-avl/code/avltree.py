class AVLTree:
	root = None

class AVLNode:
    parent = None
    leftnode = None
    rightnode = None
    key = None
    value = None
    bf = None
    height = None


"""
https://docs.google.com/document/d/19L8sag9flB_n82lsowfx3Lp3SfoAwIxlE_dzG6Rnwj0/edit?tab=t.0
"""

def mostrar_arbol(nodo, nivel=0, lado="raíz"):
    if nodo is not None:
        
        indentacion = "    " * nivel
        if nodo.parent:
            print(indentacion , " - [" + lado + "] Key:", nodo.key, ", Value:", nodo.value, ", BF:", nodo.bf, ", Height:", nodo.height, 'parentKey', nodo.parent.key)
        else:
            print(indentacion , " - [" + lado + "] Key:", nodo.key, ", Value:", nodo.value, ", BF:", nodo.bf, ", Height:", nodo.height)
        
        
        mostrar_arbol(nodo.leftnode, nivel + 1, "izquierda")
        mostrar_arbol(nodo.rightnode, nivel + 1, "derecha")



def updateHeightR(node):
    if node != None:
        updateHeightR(node.leftnode)
        updateHeightR(node.rightnode)
        if node.leftnode != None and node.rightnode != None:
            node.height = 1 + max(node.leftnode.height, node.rightnode.height)
        elif node.leftnode != None:
            node.height = 1 + node.leftnode.height
        elif node.rightnode != None:
            node.height = 1 + node.rightnode.height
        else:
            node.height = 0

def updateHeight(T):
    if T.root != None:
        T.root.height = 0
        return updateHeightR(T.root)



"""
rotateLeft(Tree,avlnode) 
Descripción: Implementa la operación rotación a la izquierda 
Entrada: Un Tree junto a un AVLnode sobre el cual se va a operar la rotación a la  izquierda
Salida: retorna la nueva raíz
"""

def rotateLeft(T, node):
    if T.root == node:
        parentNode = T.root
    else:
        parentNode = node.parent

    if node.rightnode != None:

        newRoot = node.rightnode
        ##Si la nueva raiz no tiene hijo izq
        if newRoot.leftnode == None:
            node.rightnode = None
        else:
            node.rightnode = newRoot.leftnode
            node.rightnode.parent = node 
        
        #reinicio el apuntador del nodo padre
        if node != T.root:
            if parentNode.leftnode == node:
                parentNode.leftnode = newRoot
            else:
                parentNode.rightnode = newRoot

            newRoot.parent = parentNode
        else:
            T.root = newRoot
            newRoot.parent = None

        
        newRoot.leftnode = node
        node.parent = newRoot
        updateHeight(T)
        return newRoot
        


"""
rotateRight(Tree,avlnode) 
Descripción: Implementa la operación rotación a la derecha 
Entrada: Un Tree junto a un AVLnode sobre el cual se va a operar la rotación a la  derecha
Salida: retorna la nueva raíz
"""

def rotateRight(T, node):

    if T.root == node:
        parentNode = T.root
    else:
        parentNode = node.parent

    if node.leftnode != None:

        newRoot = node.leftnode

        ##Si la nueva raiz no tiene hijo der
        if newRoot.rightnode == None:
            node.leftnode = None
        else:
            node.leftnode = newRoot.rightnode
            node.leftnode.parent = node 
        
        #reinicio el apuntador del nodo padre
        if node != T.root:
            if parentNode.leftnode == node:
                parentNode.leftnode = newRoot
            else:
                parentNode.rightnode = newRoot
            
            newRoot.parent = parentNode
        else:
            T.root = newRoot
            newRoot.parent = None
        
        newRoot.rightnode = node
        node.parent = newRoot
        updateHeight(T)
        return newRoot
        

"""
calculateBalance(AVLTree) 
Descripción: Calcula el factor de balanceo de un árbol binario de búsqueda. 
Entrada: El árbol AVL  sobre el cual se quiere operar.
Salida: El árbol AVL con el valor de balanceFactor para cada subarbol

bf = altura del subarbol derecho de  ́ v − altura del subarbol izquierdo de  ́ v
"""

def calculateBalanceR(node):
    if node:
        updateHeightR(node)
        calculateBalanceR(node.leftnode)
        calculateBalanceR(node.rightnode)
        if node.leftnode != None and node.rightnode != None:
            node.bf = node.leftnode.height - node.rightnode.height
        elif node.rightnode != None:
            node.bf = -node.height
        else:
            node.bf = node.height


def calculateBalance(T):
    if T.root != None:
        return calculateBalanceR(T.root)
    



"""
reBalance(AVLTree) 
Descripción: balancea un árbol binario de búsqueda. Para esto se deberá primero calcular el balanceFactor del árbol y luego en función de esto aplicar la estrategia de rotación que corresponda.
Entrada: El árbol binario de tipo AVL  sobre el cual se quiere operar.
Salida: Un árbol binario de búsqueda balanceado. Es decir luego de esta operación se cumple que la altura (h) de su subárbol derecho e izquierdo difieren a lo sumo en una unidad.
"""


def reBalanceR(T, node):
    #mostrar_arbol(T.root)
    if node != None:
        reBalanceR(T, node.leftnode)
        reBalanceR(T, node.rightnode)
        if node.bf < -1:
            if node.rightnode and node.rightnode.bf > 0:
                rotateRight(T, node.rightnode)
                rotateLeft(T, node)
            else:
                rotateLeft(T, node)
        elif node.bf > 1:
                if node.leftnode and node.leftnode.bf < 0:
                    rotateLeft(T, node.leftnode)
                    rotateRight(T, node)
                else:
                    rotateRight(T, node)
        
        calculateBalance(T)
        updateHeight(T)



def reBalance(T):
    if T.root != None:
        return reBalanceR(T, T.root)



def searchR(node, element):

    if node == None:
        return None
    if node.value == element:
        return node.key
    searchleft = searchR(node.leftnode, element)
    if searchleft != None:
        return searchleft

    return searchR(node.rightnode, element)


def search(B, element):
    if B.root != None:
        return searchR(B.root, element)
    else:
        return None


"""
insert()
se inserta como en un bst
despues se calcula el bf de cada nodo
bf = altura del subarbol derecho de  ́ v − altura del subarbol izquierdo de  ́ v

"""
def insertR(T, currentNode, newNode):
    if currentNode.key != newNode.key:
        if newNode.key > currentNode.key:
            if currentNode.rightnode == None:
                currentNode.rightnode = newNode
                newNode.parent = currentNode
                return newNode.key
            else:
                insertR(T, currentNode.rightnode, newNode)
        else:
            if currentNode.leftnode == None:
                currentNode.leftnode = newNode
                newNode.parent = currentNode
                return newNode.key
            else:
                insertR(T, currentNode.leftnode, newNode)
        calculateBalance(T)
        reBalance(T)
    else:
        return None


def insert(T, element, key):
    newNode = AVLNode()
    newNode.key = key
    newNode.value = element
    if T.root != None:
        #mostrar_arbol(T.root)
        #print('-' * 70)
        return insertR(T, T.root, newNode)

    else:
        T.root = newNode


"""
delete(T,element)

Descripción: Elimina un elemento del TAD árbol binario.
Poscondición: Se debe desvincular el Node a eliminar.
    Entrada: el árbol binario B sobre el cual se quiere realizar la
eliminación (BinaryTree) y el valor del elemento (element) a eliminar.
    Salida: Devuelve clave (key) del elemento a eliminar. Devuelve None si
el elemento a eliminar no se encuentra.

"""

def accessNodeR(currentNode, element, key):
    if currentNode != None:
        if currentNode.value != element:
            if key < currentNode.key:
                return accessNodeR(currentNode.leftnode, element, key)
            else:
                return accessNodeR(currentNode.rightnode, element, key)
        else:
            
            return currentNode
    else:
        return None


def accessNode(B, element):
    nodeKey = search(B, element)

    if B.root != None and nodeKey != None:
        
        return accessNodeR(B.root, element, nodeKey)
    else:
        return None


def linkNodes(B, parent, son, nodeToLink):

    if parent != None:
            
        if parent.leftnode == son:
            parent.leftnode = nodeToLink
        else:
            parent.rightnode = nodeToLink

    else:
        B.root = nodeToLink


def searchHighestLowestNode(nodeToDelete):
    currentNode = nodeToDelete.rightnode

    while currentNode.leftnode != None:
        currentNode = currentNode.leftnode
    
    return currentNode


def delete(T, element):

    nodeToDelete = accessNode(T, element)
    
    if nodeToDelete != None:
        parentNode = nodeToDelete.parent
        if nodeToDelete.leftnode == None and nodeToDelete.rightnode == None: #Es una hoja
            nodeToLink = None

        elif nodeToDelete.leftnode != None and nodeToDelete.rightnode == None: #Es una rama con una hoja a la izq
            nodeToLink = nodeToDelete.leftnode
            
        elif nodeToDelete.rightnode != None and nodeToDelete.leftnode == None: #Es una rama con una hoja a la der
            nodeToLink = nodeToDelete.rightnode

        else: #Es una rama con hojas en los dos lados
            highestLowestNode = searchHighestLowestNode(nodeToDelete)
            if nodeToDelete.rightnode != highestLowestNode:
                highestLowestNode.parent.leftnode = None # desvinculo el menor de los mayores
                highestLowestNode.rightnode = nodeToDelete.rightnode
            else:
                nodeToDelete.rightnode = None
            highestLowestNode.leftnode = nodeToDelete.leftnode 
            nodeToLink = highestLowestNode

        linkNodes(T, parentNode, nodeToDelete, nodeToLink)
        calculateBalance(T)
        reBalance(T)
        return nodeToDelete.key
    else:
        return None






def joinAVL(A, x, B):


    """
    Sean A y B dos AVL de m y n nodos respectivamente y sea x un key cualquiera de forma tal que para todo key a ∈ A y para todo key b ∈ B se cumple que a < x < b. Plantear un algoritmo O(log n + log m) que devuelva un AVL que contenga los key de A, el key x y los key de B.

    1er caso: 
        A,B tienen la misma altura, luego x va a ser la raiz de A como rama izquierda y B como rama derecha
    2do caso: 
        A es mas grande que B, recorro A por el subarbol derecho hasta que tenga un arbol de altura similar a B, 
        inserto x con B como rama derecha y el subarbol de A como rama izquierda
    3do caso: 
        B es mas grande que A, recorro B por el subarbol izquierdo hasta que tenga un arbol de altura similar a A, 
        inserto x con A como rama izquierda y el subarbol de B como rama derecha

    Como en el caso 1 el arbol resultante ya resulta balanceado, en los casos 2 y 3 el arbol resultante puede estar desbalanceado 
    entonces tenemos que subir apartir de x balanceando el arbol, logrando una complejidad temporal de O(log n) o O(log m) dependiendo en que arbol se aplica el balanceo
    """

    return 





def pathToBranch(T):

    """
    Considere una rama truncada en un AVL como un camino simple desde la raíz hacia un nodo que tenga una referencia None (que le falte algún hijo). Demuestre que la mínima longitud (cantidad de aristas) que puede tener una rama truncada  en un AVL de altura h es h/2 (tomando la parte entera por abajo). 



    """


    return 


t = AVLTree()

insert(t, 'hola', 20)
insert(t, 'hola1', 60)
insert(t, 'hola2', 100)
insert(t, 'hola3', 120)
insert(t, 'hola4', 80)
insert(t, 'hola5', 70)
##insert(t, 'hola2', 7)
mostrar_arbol(t.root)
print('-' * 70)
delete(t, 'hola4')
mostrar_arbol(t.root)
