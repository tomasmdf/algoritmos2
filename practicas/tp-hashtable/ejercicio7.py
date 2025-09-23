"""
Ejercicio 7
Implemente un algoritmo para realizar la compresión básica de cadenas utilizando el recuento de caracteres repetidos. Por ejemplo, la cadena ‘aabcccccaaa’ se convertiría en ‘a2blc5a3’. Si la cadena "comprimida" no se vuelve más pequeña que la cadena original, su método debería devolver la cadena original. Puedes asumir que la cadena sólo tiene letras mayúsculas y minúsculas (a - z, A - Z). Justificar el costo en tiempo de la solución propuesta.
"""

#recorro la cadena hasta que no se repita el caracter
# [aa, b, ccccc, aaa]
#por cada elemento del arr calculo la suma del orden


def compressString(str):

    cont = 1
    resultStr = ''

    for x in range(1,len(str)):
        print('str[x]', str[x])
        print('cont', cont)

        if str[x] == str[x-1]:
            cont += 1

        elif str[x] != str[x-1]:
            resultStr = resultStr + str[x-1] + cont.__str__()
            cont = 1

    resultStr = resultStr + str[x] + cont.__str__()

    if len(resultStr) > len(str):
        return str
    else:
        return resultStr


print(compressString('aaaaamms'))