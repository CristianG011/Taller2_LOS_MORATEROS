def vocales(cadena):
    # Definimos una función que cuenta cuántas vocales tiene una palabra
    vocales = "A a E e I i O o U u"  # Definimos las vocales
    contador = 0  # Inicializamos el contador a 0
    for letra in cadena:  # Iteramos a través de las letras de la palabra
        if letra in vocales:  # Si la letra es una vocal
            contador += 1  # Incrementamos el contador en 1
        if contador >= 2:  # Si hay al menos 2 vocales, terminamos la función
            return True  # La función retorna True

if __name__ == "__main__":
    palabras = input("Ingrese palabras separadas por un espacio: ")  # Solicitamos al usuario ingresar palabras
    cadenas = palabras.split()  # Separamos las palabras en una lista llamada "cadenas"
    for cadena in cadenas:  # Iteramos a través de las palabras
        if vocales(cadena):  # Llamamos la función 'vocales' para cada palabra
            print(cadena)  # Imprimimos las palabras que tienen 2 o más vocales
        else:
            print("No existe")  # Imprimimos "No existe" para las palabras que no cumplen con la condición
