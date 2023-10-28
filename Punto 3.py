def numeros_espejo(a, b):         #Definimos la función para hallar números espejo
    lista1 = []                   #Creamos lista 1 para los dígitos del primer número ingresado
    while a > 0:
        digitos_a = a % 10        #Se obtiene el último dígito del primer número
        a = a // 10               #Se reduce el primer número eliminando el último dígito
        lista1.append(digitos_a)  #Agrega los dígitos a la lista 1

    lista2 = []                   #Creamos lista 2 para los dígitos del segundo número
    while b > 0:
        digitos_b = b % 10        #Se obtiene el último dígito del segundo número
        b = b // 10               #Se reduce el segundo número eliminando el último dígito
        lista2.append(digitos_b)  #Agrega los dígitos a la lista 2


    if lista1[:] == lista2[::-1] or lista1[::-1] == lista2[:]:   #Si los dígitos del primer número son iguales a los dígitos del segundo número al revés o viceversa
        return "Son números espejo"                              #Se trata de números espejo
    else:
        return "No son números espejo"

if __name__ == "__main__":
    a = int(input("Ingrese un número entero: "))
    b = int(input("Ingrese otro número entero: "))
    numeros_espejo = numeros_espejo(a, b)
    print(numeros_espejo)