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

    # Caso base: llegamos al final de la palabra
    if len(element) < 1:
        node.isEndOfWord = False
        # Si no tiene hijos → se puede eliminar este nodo
        return node.children is None

    # Buscar el hijo con la letra correspondiente en la lista
    if node:
        char = element[0]
        positionChar = searchInTrie(node.children, char)

        prevNode = linkedlist.accessNode(node.children, positionChar-1)
        currentNode = linkedlist.accessNode(node.children, positionChar)

    if not currentNode:
        return False  # la palabra no existe

    # Llamada recursiva al hijo
    slicedElement = element[1:]
    should_delete_child = deleteR(node.children, slicedElement)

    if should_delete_child:
        # Eliminamos el nodo de la linked list
        if prevNode:
            prevNode.nextNode = currentNode.nextNode
        else:
            node.children = currentNode.nextNode

    # Se elimina este nodo si no es fin de palabra y no tiene hijos
    return (not node.isEndOfWord) and (node.children is None)


def delete(T, element):
    #si tenemos sol y sola y se quiere eliminar sol solo hay que sacar la flag de end en la l 
    #si tengo una palabra separada elimina desde la raiz 
    #si quiero eliminar sola solo tengo que eliminar la a

    #hago un search para ver si esta la palabra
    if search(T,element) != None:
        return deleteR(T.root, element)
    else:
        return False





"""

Ej4

Implementar un algoritmo que dado un árbol Trie T, un patrón p (prefijo) y un entero n, 
escriba todas las palabras del árbol que empiezan por p y sean de longitud n. 

findAll(T, prefijo, n)
findAll(T, 'ho', 4)

return [hola, holo]

recursivamente disminuyo en 1 n, voy verificando que que cumpla con el prefijo
devuelvo los resultados en un array

"""

def joinWord(node, prefix, n, results):
    if node.key:
        print('nodeKey', node.key)
    print('n', n)
    print('prefix', prefix)
    # base: no tiene hijos y devuelve el prefijo solo si tiene fin de palabra
    # recursion: puede seguir bajando, por cada hijo le agrego al prefijo

    if len(prefix) == n:
        print('len(prefix) == n')
        if node.isEndOfWord:
            print('entro')
            return results.append(prefix)
        else:
            return None
    
    newPrefix = prefix + node.key
        
    if node.children:
        currentNode = node.children.head

        while currentNode:
            
            joinWord(currentNode.value, newPrefix, n, results)
            currentNode = currentNode.nextNode
    elif len(newPrefix) == n:
        joinWord(node, newPrefix, n, results)


def findAllR(node, prefix, n, index, results):

    if index < n and len(prefix) > index:
        print(node.key)
        char = prefix[index]
        #print('char', char)
        #mostrarLinkedListTrie(node.children)
        positionChar = searchInTrie(node.children, char)
        #print(positionChar)

        currentNode = linkedlist.accessNode(node.children, positionChar)

        return findAllR(currentNode.value, prefix, n, index+1, results)
    
    else:
        #tengo que recorre todas las ramas y añadir las palabras a results
        print('ultimo node', node.key)
        currentNode = node.children.head
        while currentNode:
            print('currentNode', currentNode.value.key)
            wordToAdd = joinWord(currentNode.value, prefix, n, results)
            if wordToAdd:
                results.append(wordToAdd)
            currentNode = currentNode.nextNode

        return print(results)


def findAll(T, prefix, n):
    results = []

    if T.root != None:
        return findAllR(T.root, prefix, n, 0, results)
    else:
        return results



"""
Parte 2

-------------------------------------------------------------------------------

Ej4

findAll(T, prefijo, n)
findAll(T, 'ho', 4)

return [hola, holo]

recursivamente disminuyo en 1 n, voy verificando que que cumpla con el prefijo
devuelvo los resultados en un array

-------------------------------------------------------------------------------

Ej5

recorro a la misma vez los dos trie si hay alguna diferencia devuelvo false

-------------------------------------------------------------------------------

Ej6

abcd y dcba

invierto una de las cadenas y hagoi un search para la cadena invertida

-------------------------------------------------------------------------------

Ej7

autoCompletar(Trie, cadena)
autoCompletar(T, ‘groen’)
devolvería “land”, ya que podemos tener “groenlandia” o “groenlandés”

recorre desde el prefijo hasta la primera bifurcacion que haya 

recorre hasta teminar el prefijo, luego continua hasta que el node.children sea una lista con mas de 1 hijo

"""


T = Trie()
insert(T, 'hola')
insert(T, 'holo')
insert(T, 'holanda')
insert(T, 'holograma')
insert(T, 'hologramica')
insert(T, 'sol')
mostrar_trie(T.root)
print('Search: ', search(T, 'hola'))

## Falta implementar el delete
findAll(T, 'hol', 10)

#mostrar_trie(T.root)