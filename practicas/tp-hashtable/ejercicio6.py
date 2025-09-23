"""
Ejercicio 6
Los nuevos códigos postales argentinos tienen la forma cddddccc, donde c indica un carácter (A - Z) y d indica un dígito 0, . . . , 9. Por ejemplo, C1024CWN es el código postal que representa a la calle XXXX a la altura 1024 en la Ciudad de Mendoza. Encontrar e implementar una función de hash apropiada para los códigos postales argentinos.

"""

def hashCodigoPostal(str):
    #agrupo los digitos y los caracteres por separado
    #calculo el ord de los caracteres y la suma de los digitos 
    #y sumo los dos resultados

    characters = ''
    digits = ''

    for i in str:
        if i.isalpha(): #si es caracter
            characters = characters + i
        elif i.isnumeric():
            digits = digits + i

    characters = characters.casefold() #convierto a minusculas
    print(characters)
    print(digits)

    sumChar = sum(ord(characters[k]) - ord('a') for k in range(4))
    sumDigits = sum(int(digits[l]) for l in range(4))

    return sumChar + sumDigits


hashCodigoPostal('C4523opf')