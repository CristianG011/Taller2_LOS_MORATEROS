#Desarrollar un programa que ingrese un número entero n y separe todos los digitos que componen el número. Pista: Utilice los operadores módulo (%) y división entera (//).

def digitos(n):                   #Definimos la función para separar los dígitos
    lista = []                    #Se crea una lista donde se almacenarán todos los dígitos
    while n > 0:
        digitos = n % 10          #Obtenemos el último dígito de n, inresado por computadora tomando el residuo de la división por 10
        n = n // 10               #Reducimos n eliminando el último dígito
        lista.append(digitos)     #Los agregamos a la lista creada

    if len(lista) == 0:           #Si la lista está vacía se devuelve el valor 0
        lista = [0]

    return lista[::-1]            #Devuelve los dígitos en el orden en el que se encuentran en el número

if __name__ == "__main__":
    n = int(input("Ingrese un número entero: "))
    digitos = digitos(n)
    print("Los dígitos del número dado son: ")
    print(digitos)