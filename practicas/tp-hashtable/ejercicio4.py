"""
Ejercicio 4
Implemente un algoritmo lo más eficiente posible que devuelva True o False a la siguiente proposición: dado dos strings s1...sk  y p1...pk, se quiere encontrar si los caracteres de p1...pk corresponden a una permutación de s1...sk. Justificar el coste en tiempo de la solución propuesta.

Ejemplo 1:
Entrada: S = ‘hola’ , P = ‘ahlo’
Salida: True, ya que P es una permutación de S

Ejemplo 2:
Entrada: S = ‘hola’ , P = ‘ahdo’
Salida: Falso, ya que P tiene al caracter ‘d’ que no se encuentra en S por lo que no es una permutación de S


S= 'aade'
P= 'adee'

no es permutacion

tamaño de la diccionario ord(z) - ord(a)

suponemos que solo tenemos de entrada caracteres

convertimos a minusculas S y P, string.casefold()

"""

class permutacionChar:
    value: None
    frecuency: None

def insert(D, char):

    #print(char)
    slotToInsert = ord('z') - ord(char)

    node = permutacionChar()
    node.value = char
    node.frecuency = 1

    if D[slotToInsert]  == None or D[slotToInsert]  == 'deleted': #slot vacio
        D[slotToInsert] = node

    else:
        D[slotToInsert].frecuency += 1

    return D

def searchPermutation(D, char):
    slot = D[ord('z') - ord(char)]

    if slot == None:
        return False

    elif slot.frecuency >= 1:
        slot.frecuency = slot.frecuency - 1
        return True
            
    elif slot.frecuency < 1 :
        return False


def mostrar_diccionario(diccionario):
    """Muestra el contenido del diccionario (lista de buckets)."""
    for i, bucket in enumerate(diccionario):
        print(f"Bucket {i}: ", end="")
        if bucket is None or bucket == 'deleted':
            print("vacío")
        else:  # hay un nodo permutacionChar
            print(f"[{bucket.value} : {bucket.frecuency}]")

def isPermutation(D, s, p):

    if len(s) == len(p):
        lowercaseS = s.casefold()
        lowercaseP = p.casefold()


        for n in range(len(lowercaseS)):
            charS = lowercaseS[n]
            insert(D, charS)

        mostrar_diccionario(D)

        for k in range(len(lowercaseP)):
            
            charP = lowercaseP[k]
            if not(searchPermutation(dictionary, charP)): # no esta el char
                return False

        return True
    
    return False


dictionarySize = 1 + ord('z') - ord('a') 

dictionary = [None]*dictionarySize

print(isPermutation(dictionary, 'aade', 'adee'))

#Orden Complejidad O(len(S))


