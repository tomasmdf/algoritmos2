import linkedlist


class Trie:
	root = None

class TrieNode:
    parent = None
    children = None   
    key = None
    isEndOfWord = False

def mostrarLinkedListTrie(L):
    current = L.head
    print("LINKED LIST: [", end="")
    while current != None:
        if current.nextNode != None:
            print(str(current.value.key) + ", ", end="")
        else:
            print(str(current.value.key), end="")
        current = current.nextNode
    print("]")


def mostrar_trie(nodo, nivel=0, lado="raíz"):
    if nodo is not None:
        indentacion = "    " * nivel

        # Mostrar información del nodo
        if nodo.parent:
            print(indentacion, f"- [{lado}] Key: {nodo.key}, EndOfWord: {nodo.isEndOfWord}, ParentKey: {nodo.parent.key}")
        else:
            print(indentacion, f"- [{lado}] Key: {nodo.key}, EndOfWord: {nodo.isEndOfWord}")

        # Recorrer la linked list de hijos
        hijo_actual = nodo.children.head if nodo.children else None
        while hijo_actual:
            mostrar_trie(hijo_actual.value, nivel + 1, f"hijo '{hijo_actual.value.key}'")
            hijo_actual = hijo_actual.nextNode



"""
insert(T,element) 
Descripción: insert un elemento en T, siendo T un Trie.
Entrada: El Trie sobre la cual se quiere agregar el elemento (Trie)  y el valor del elemento (palabra) a  agregar.
Salida:  No hay salida definida
"""

def insertNode(node, element):
    if len(element) > 0:

        char = element[0]
        if node.children != None: #Tiene children
            currentLevel = node.children.head
            #Busco si existe el char en los children de T
            while currentLevel != None:
                if currentLevel.value.key == char: #Existe char
                    node = currentLevel.value
                    break
                currentLevel = currentLevel.nextNode
            
            if currentLevel == None: #No existe el char
                newTrieNode = TrieNode()
                newTrieNode.key = char
                newTrieNode.parent = node

                linkedlist.add(node.children, newTrieNode)
                node = newTrieNode

        else: #No tiene children
            
            node.children = linkedlist.LinkedList()
            newTrieNode = TrieNode()
            newTrieNode.key = char
            newTrieNode.parent = node

            linkedlist.add(node.children, newTrieNode)
            node = newTrieNode

        slicedElement = element[1:] #slice tiene O(1) ya que se usa el mejor caso, sacar el primer elemento
        return insertNode(node, slicedElement)
    else:
        node.isEndOfWord = True


def insert(T, element):
    if T.root != None:        
        return insertNode(T.root, element)
    else:
        #inicializo la raiz con un nodo trie con key ''
        root = TrieNode()
        root.key = None
        T.root = root
        insert(T, element)


"""
search(T,element)
Descripción: Verifica que un elemento se encuentre dentro del Trie
Entrada: El Trie sobre la cual se quiere buscar el elemento (Trie)  y el valor del elemento (palabra)
Salida: Devuelve False o True  según se encuentre el elemento.
"""
def searchInTrie(L, element):
    current = L.head
    position = 0
    while current != None:
        if current.value.key == element:
            return position
        current = current.nextNode
        position += 1
    
    return None


def searchR(node, element):
    if node.children: #tiene hijos
        if len(element) > 0: #quedan elementos por buscar

            char = element[0]
            positionChar = searchInTrie(node.children, char)
            #mostrarLinkedListTrie(node.children)

            if positionChar != None: #esta el char buscado
                nextLevelNode = linkedlist.accessNode(node.children, positionChar)
                slicedElement = element[1:]
                return searchR(nextLevelNode.value, slicedElement)
            else:
                return False

    if node.isEndOfWord == True and len(element) == 0:
        return True
    else:
        return False

def search(T, element):
    #se ejecuta mientras el access del campo children != none
    if T.root != None:
        return searchR(T.root, element)
    else:
        return False




"""
delete(T,element)
	Descripción: Elimina un elemento se encuentre dentro del Trie
Entrada: El Trie sobre la cual se quiere eliminar el elemento (Trie)  y el valor del elemento (palabra) a  eliminar.
Salida: Devuelve False o True  según se haya eliminado el elemento.
"""

def deleteR(node, element):


    

    return 




def delete(T, element):
    #si tenemos sol y sola y se quiere eliminar sol solo hay que sacar la flag de end en la l 
    #si tengo una palabra separada elimina desde la raiz 
    #si quiero eliminar sola solo tengo que eliminar la a

    #hago un search para ver si esta la palabra

    if search(T,element) != None:
        return deleteR(T.root, element)
    else:
        return False






T = Trie()
insert(T, 'hola')
insert(T, 'holanda')
insert(T, 'holograma')
insert(T, 'sol')
mostrar_trie(T.root)
print('Search: ', search(T, 'hola'))