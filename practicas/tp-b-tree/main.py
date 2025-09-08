import linkedlist 

class BTreeNode:
    keys = linkedlist.LinkedList()
    children = linkedlist.LinkedList()
    leaf = None

class BTree:
    root = BTreeNode()
    t = None




def showBTree(node=None, level=0):
        """Imprime el B-tree en formato jerárquico"""
        if node is None:
            node = node.root

        # mostrar las claves del nodo
        print("   " * level + "Nivel", level, "-> ", end="")
        linkedlist.mostrarLinkedList(node.keys)

        # si no es hoja, recorrer los hijos
        if not node.leaf:
            for i in range(linkedlist.length(node.children)):
                child = linkedlist.access(node.children, i)
                showBTree(child, level + 1)
                


"""
insert(BT, key)

si el nodo esta lleno hay que hacer split

si el nodo no esta lleno entonces se recorre keys y se inserta en la posicion correspondiente



"""

def insertR(node, key, t):

    if linkedlist.length(node.keys) < (2*t-1):
        currentNode = node.keys.head

        print('key', key)

        #recorro hasta la posicion anterior al mayor que key
        for n in range(0, linkedlist.length(node.keys)):
            if currentNode.nextNode: #existe el sig
                if currentNode.nextNode.value < key:
                        currentNode = currentNode.nextNode
                else: 
                    break
                

        if currentNode != None:

            print('currentNode:', currentNode.value)

            if currentNode.value < key:
                newNode = linkedlist.Node()
                newNode.value = key
                newNode.nextNode = currentNode.nextNode
                currentNode.nextNode = newNode
            else:
                linkedlist.add(node.keys, key)
        else:
            linkedlist.add(node.keys, key)

    return 

def insert(BT, key):

    if BT.root != None:
        return insertR(BT.root, key, BT.t)
    else:

        return None
    





# Crear un BTree de grado mínimo 2
btree = BTree()
btree.t = 3

# Construimos manualmente un arbol de ejemplo
"""
btree.root = BTreeNode()
btree.root.keys = [10, 20]
btree.root.leaf = False

child1 = BTreeNode()
child1.keys = [5, 7]

child2 = BTreeNode()
child2.keys = [15]

child3 = BTreeNode()
child3.keys = [25, 30]

btree.root.children = [child1, child2, child3]
"""

# Mostrar el árbol
insert(btree, 14)
insert(btree, 16)
insert(btree, 12)
showBTree(btree.root)
