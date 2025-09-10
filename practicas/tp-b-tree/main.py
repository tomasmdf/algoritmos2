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

        # la clave media está en y.keys[t-1]
        mid = y.keys[t-1]

        # z recibe las últimas t-1 claves de y
        z.keys = y.keys[t:]   
        y.keys = y.keys[:t-1]

        # si no es hoja, también repartir hijos
        if not y.leaf:
            z.children = y.children[t:]
            y.children = y.children[:t]

        # insertar z como hijo del padre
        parent.children.insert(i+1, z)

        # subir la clave media al padre
        parent.keys.insert(i, mid)


    # --------------------------
    # Insertar en nodo no lleno
    # --------------------------
    def insert_non_full(self, node, key):
        i = len(node.keys) - 1

        if node.leaf:
            # insertar en posición correcta en keys
            node.keys.append(key)
            node.keys.sort()
        else:
            # encontrar hijo adecuado
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1

            # si el hijo está lleno → dividir
            if len(node.children[i].keys) == 2*self.t - 1:
                self.split_child(node, i)
                if key > node.keys[i]:
                    i += 1

            self.insert_non_full(node.children[i], key)

    # --------------------------
    # Insertar en el árbol
    # --------------------------
    def insert(self, key):
        root = self.root
        if len(root.keys) == 2*self.t - 1:
            # raíz llena → crecer altura
            new_root = BTreeNode(leaf=False)
            new_root.children.append(root)
            self.root = new_root
            self.split_child(new_root, 0)
            self.insert_non_full(new_root, key)
        else:
            self.insert_non_full(root, key)

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

    def findPredecesorR(self, node, k, keyPosition):

        if keyPosition == 0 : # estamos en caso 1, 3 o 4
            return 

        if keyPosition > 0: # estamos en 2
            #retornar el elemento n keyposition - 1
            return 




        return

    def findPredecesor(self, node, k):
        keyPosition = self.search(node, k)[1]
        print('position:', keyPosition)

        if self.search(node, k) != None: # existe k en el btree
            return self.findPredecesorR(node, k, keyPosition)







        
    

bt = BTree(t=2)  # B-tree de grado mínimo 2
for k in [10, 20, 5, 6, 12, 30, 7, 17, 1]:
    bt.insert(k)

print(bt.root.keys)        # claves de la raíz
print([child.keys for child in bt.root.children])  # claves de los hijos

print(bt.search(bt.root, 4))
print('Key minima:', bt.minKey(bt.root))
print('Predecesor:', bt.findPredecesor(bt.root, 7))
