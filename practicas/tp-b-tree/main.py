
#https://docs.google.com/document/d/1CJeK9zOhkrR146I5DQzhWFTHeJ2TsT917SNWyub3rTU/edit?tab=t.0


class BTreeNode:
    def __init__(self, leaf=False):
        self.keys = []       # lista de claves (ordenadas)
        self.children = []   # lista de hijos (len(children) = len(keys)+1 si no es hoja)
        self.leaf = leaf

class BTree:
    def __init__(self, t):
        self.root = BTreeNode(leaf=True)
        self.t = t   # grado mínimo


    

    # --------------------------
    # Dividir hijo lleno
    # --------------------------
    def split_child(self, parent, i):
        t = self.t
        y = parent.children[i]
        z = BTreeNode(leaf=y.leaf)

        mid = y.keys[t-1]

        # claves
        z.keys = y.keys[t:]            # t .. 2t-2
        y.keys = y.keys[:t-1]          # 0 .. t-2

        # hijos
        if not y.leaf:
            z.children = y.children[t:]
            y.children = y.children[:t]

        parent.children.insert(i+1, z)
        parent.keys.insert(i, mid)

    def insert_non_full(self, node, key):
        i = len(node.keys)-1
        if node.leaf:
            node.keys.append(None)     # espacio
            while i >= 0 and key < node.keys[i]:
                node.keys[i+1] = node.keys[i]
                i -= 1
            node.keys[i+1] = key
        else:
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == 2*self.t - 1:
                self.split_child(node, i)
                if key > node.keys[i]:
                    i += 1
            self.insert_non_full(node.children[i], key)

    def insert(self, key):
        root = self.root
        if len(root.keys) == 2*self.t -1:
            new_root = BTreeNode(leaf=False)
            new_root.children.append(root)
            self.root = new_root
            self.split_child(new_root,0)
            self.insert_non_full(new_root,key)
        else:
            self.insert_non_full(root,key)

    
    def search(self, node, key):
        i = 0

        # buscar la primera clave mayor o igual que key
        while i < len(node.keys) and key > node.keys[i]:
            i += 1

        # caso 1: encontramos la clave
        if i < len(node.keys) and key == node.keys[i]:
            return (node.keys[i], i)   # nodo y posición de la clave dentro del nodo

        # caso 2: nodo es hoja -> no existe
        if node.leaf:
            return None

        # caso 3: bajar al hijo correspondiente
        return self.search(node.children[i], key)
    

    #Ejercicio 4 - algoritmo que devuelve la menor clave en btree
    #es el primer elemento del subarbol izq
    def minKey(self, node):

        #print('nodo actual:', node.keys[0])

        if not(node.leaf):
            return self.minKey(node.children[0])
        else:
            return node.keys[0]

    #Ejercicio 5 - algoritmo que devuelve el predecesor de un valor k, sino devuelve None
    #hago un search para verificar que el elemento esta en el btree
    #   1- btree con 1 sola key, no hay predecesor
    #   2- si k no esta en el extremo izq, el pred. esta en la posicion n-1
    #   3- k esta en el extremo izq, su pred. es el ultimo elemento del nodo parent
    #   4- en general el pred de k, es el mayor de los menores

  
    def highestOfLower(self, node):
        i = 0
        #print(node.keys)
        # voy hasta el final
        while i < len(node.keys)-1:
            i += 1

        #print('node.keys[i]', node.keys[i])
        if node.leaf:
            return node.keys[i]
        else:
            return self.highestOfLower(node.children[i+1])


    def findPredecesorR(self, node, k, keyPosition, parent):
        i = 0

        # buscar la primera clave mayor o igual que key
        while i < len(node.keys) and k > node.keys[i]:

            #Caso 2
            if i < len(node.keys)-1 and node.keys[i+1]:
                if k == node.keys[i+1] and node.leaf:
                    return node.keys[i]

            #print('node.keys[i]', node.keys[i])
            i += 1

        #print('node.keys[i]', node.keys[i])

        if i < len(node.keys) and k == node.keys[i]: #estamos en k

            if node.children:
                return self.highestOfLower(node.children[i])
            else:
                if parent and parent < k:
                    return parent
                else:
                    return None
        
        return self.findPredecesorR(node.children[i], k, keyPosition, node.keys[i-1]) 

    def findPredecesor(self, node, k):
        key = self.search(node, k)
        if key:
            keyPosition = key[1]
        #print('position:', keyPosition)

        if self.search(node, k) != None: # existe k en el btree
            return self.findPredecesorR(node, k, keyPosition, None)


    #Ejercicio 6 - Algoritmo que recibe un btree y un entero k y devuelve True si existen 2 keys tal que x+l = k
    #x-k=l
    #por cada elemento x<k hago x-k=l y busco si l esta en el btree, si existe devuelve true
    def findSum(self, node, k, root):

        i = 0
        sumFound = False

        while i < len(node.keys):
            
            if node.keys[i] < k:

                keyToSearch = k-node.keys[i]
                if self.search(root, keyToSearch) != None:
                    return True
                
            i += 1
                
        for child in node.children:
            sumFound = self.findSum(child, k, root)
            if sumFound:
                break

        return sumFound


def print_btree(node, level=0):
        print("  " * level, node.keys)
        for child in node.children:
            print_btree(child, level+1)
    

bt = BTree(t=2)  # B-tree de grado mínimo 2
for k in [10, 20, 5]:
    bt.insert(k)

print_btree(bt.root)

print(bt.search(bt.root, 4))
print('Key minima:', bt.minKey(bt.root))
print('Predecesor:', bt.findPredecesor(bt.root, 20))
print('Find Sum:', bt.findSum(bt.root, 15, bt.root))
