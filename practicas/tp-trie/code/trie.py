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
        if nodo.children:
            hijo_actual = nodo.children.head
        else:
            hijo_actual = None

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

def deleteR(node, element, prevNode):

    if node.key:
        print(node.key)

    # Caso base: llegamos al final de la palabra
    if len(element) < 1:
        node.isEndOfWord = False
        
        return node.children is None # Si no tiene hijos entonces se puede eliminar este nodo

    canDeleteChild = False  

    # Buscar el hijo con la letra correspondiente en la lista
    if node.children:
        mostrarLinkedListTrie(node.children)
        char = element[0]
        positionChar = searchInTrie(node.children, char)

        prevNode = linkedlist.accessNode(node.children, positionChar-1)
        if prevNode:
            print('prevNode', prevNode.value.key)
        currentNode = linkedlist.accessNode(node.children, positionChar)

        # Llamada recursiva al hijo
        slicedElement = element[1:]
        canDeleteChild = deleteR(currentNode.value, slicedElement, prevNode)


    if canDeleteChild:
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
    if search(T,element):
        return deleteR(T.root, element, None)
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

    newPrefix = prefix + node.key #agrega el char del nodo actual

    if len(newPrefix) == n:
        if node.isEndOfWord:
            return results.append(newPrefix)
        else:
            return None

    if node.children and len(newPrefix) < n:

        currentNode = node.children.head
        while currentNode:
            joinWord(currentNode.value, newPrefix, n, results)
            currentNode = currentNode.nextNode

    elif len(newPrefix) == n and not(node.children):
        joinWord(node, newPrefix, n, results)


def findAllR(node, prefix, n, index, results):

    if index < n and len(prefix) > index:
        char = prefix[index]
        positionChar = searchInTrie(node.children, char)

        if positionChar != None:
            currentNode = linkedlist.accessNode(node.children, positionChar)
            return findAllR(currentNode.value, prefix, n, index+1, results)
        else:
            return None
    
    else:
        #tengo que recorre todas las ramas y añadir las palabras a results
        currentNode = node.children.head
        while currentNode:
            wordToAdd = joinWord(currentNode.value, prefix, n, results)
            if wordToAdd:
                results.append(wordToAdd)
            currentNode = currentNode.nextNode

        return results


def findAll(T, prefix, n):
    results = []

    if T.root != None:
        return findAllR(T.root, prefix, n, 0, results)
    else:
        return results


"""
Ej5

Implementar un algoritmo que dado los Trie T1 y T2 devuelva True si estos pertenecen al mismo documento y False en caso contrario. Se considera que un  Trie pertenece al mismo documento cuando:
Ambos Trie sean iguales (esto se debe cumplir)
El Trie T1 contiene un subconjunto de las palabras del Trie T2 
Si la implementación está basada en LinkedList, considerar el caso donde las palabras hayan sido insertadas en un orden diferente.

En otras palabras, analizar si todas las palabras de T1 se encuentran en T2. 

recorro a la misma vez los dos trie si hay alguna diferencia devuelvo false
"""

def findAllWordsInTrieR(node, word, results):

    if node.key:
        newWord = word + node.key
    else:
        newWord = ''

    if node.isEndOfWord:
        results.append(newWord)

    if node.children:
        currentNode = node.children.head

        while currentNode:
            findAllWordsInTrieR(currentNode.value, newWord, results)
            currentNode = currentNode.nextNode
    else:
        return results

    return results

def findAllWordsInTrie(T):
    if T.root != None:
        return findAllWordsInTrieR(T.root, '', [])
    else:
        return []


def areEqualTrie(T1, T2):
    #busco todas las palabras de T1
    #recorro el array buscando todas las palabras en T2

    wordsArrays = findAllWordsInTrie(T1)
    #print('palabras a buscar en T2', wordsArrays)

    for x in wordsArrays:
        if not(search(T2, x)):
            return False
        
    return True


"""
Ej6

Implemente un algoritmo que dado el Trie T devuelva True si existen en el documento T dos cadenas invertidas. 
Dos cadenas son invertidas si se leen de izquierda a derecha y contiene los mismos caracteres que si se lee 
de derecha a izquierda, ej: abcd y dcba son cadenas invertidas, gfdsa y asdfg son cadenas invertidas, 
sin embargo abcd y dcka no son invertidas ya que difieren en un carácter

abcd y dcba

invierto una de las cadenas y hagoi un search para la cadena invertida
"""

#busco todas las palabras y las meto en un array 
#busco en el array si hay una palindromo
# - parto a la mitad el string y comparo 

def existsPalindromo(T):
    if T.root != None:
        
        wordsInTrie = findAllWordsInTrie(T)

        for x in wordsInTrie:
            invertedString = x[::-1] # O(n)
            if wordsInTrie.__contains__(invertedString):
                return True
        
        return False
        
    else:
        return False


"""

Ej7

Un corrector ortográfico interactivo utiliza un Trie para representar las palabras de su diccionario. Queremos 
añadir una función de auto-completar (al estilo de la tecla TAB en Linux): cuando estamos a medio escribir una 
palabra, si sólo existe una forma correcta de continuarla entonces debemos indicarlo. 

Implementar la función autoCompletar(Trie, cadena) dentro del módulo trie.py, que dado el árbol Trie T y 
la cadena  devuelve la forma de auto-completar la palabra. Por ejemplo, para la llamada autoCompletar(T, ‘groen’) 
devolvería “land”, ya que podemos tener “groenlandia” o “groenlandés” (en este ejemplo la palabra groenlandia y 
groenlandés pertenecen al documento que representa el Trie). Si hay varias formas o ninguna, devolvería la cadena 
vacía. Por ejemplo, autoCompletar(T, ma’) devolvería “” (cadena vacia) si T presenta las cadenas “madera” y “mama”

autoCompletar(Trie, cadena)
autoCompletar(T, ‘groen’)
devolvería “land”, ya que podemos tener “groenlandia” o “groenlandés”

recorre desde el prefijo hasta la primera bifurcacion que haya 

recorre hasta teminar el prefijo, luego continua hasta que el node.children sea una lista con mas de 1 hijo

"""

def autoCompletarR(node, prefix, index):

    if index < len(prefix):
        #print(node.key)
        char = prefix[index]
        positionChar = searchInTrie(node.children, char)
        currentNode = linkedlist.accessNode(node.children, positionChar)
        return autoCompletarR(currentNode.value, prefix, index+1)
    
    else:
        #tengo que recorre la rama hasta que el children tenga mas de 1 hijo
        if node.children:
            currentNode = node.children.head
            if linkedlist.length(node.children) <= 1:
                if index == len(prefix):
                    return autoCompletarR(currentNode.value, prefix, index+1)
                else:
                    return autoCompletarR(currentNode.value, prefix + node.key, index+1)
            else:

                if index == len(prefix):
                    return prefix
                else:
                    return prefix + node.key



def autoCompletar(T, prefix):
    if T.root != None:
        return autoCompletarR(T.root, prefix, 0)
    else:
        return ''





T = Trie()
"""

insert(T, 'holanda')

insert(T, 'radar')
insert(T, 'abcd')
insert(T, 'groenlandia')
insert(T, 'groenlandes')
insert(T, 'cdba')
"""

insert(T, 'sol')
insert(T, 'hola')
insert(T, 'holo')
insert(T, 'holograma')
insert(T, 'hologramica')
mostrar_trie(T.root)


M = Trie()
insert(M, 'hola')
insert(M, 'holo')


delete(T, 'sol')
mostrar_trie(T.root)

"""

print('Search: ', search(T, 'ba')) #✅
print('findAll:', findAll(T, 'gro', 11)) #✅
print('areEqualTrie:', areEqualTrie(T, M)) #✅
print('existsPalindromo:',  existsPalindromo(T)) #✅
print('autoCompletar:', autoCompletar(T, 'ho')) #✅
"""

#mostrar_trie(T.root)