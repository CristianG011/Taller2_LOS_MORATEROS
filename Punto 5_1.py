#Forma iterativa

def calcular_mcm(a, b):           #Definimos función para calcular mínimo común múltiplo
    multiplicacion = a * b        #Multiplicamos los dos números ingresados

    while b > 0:                  #Algoritmo de euclides para sacar el máximo común divisor
        residuo = a % b
        a = b
        b = residuo

    mcd = a
    mcm = multiplicacion / mcd    #El mínimo común múltiplo equivale a la multiplicación de los valores ingresados sobre el máximo común divisor

    return mcm

if __name__ == "__main__":
    a = int(input("Ingrese un número entero: "))
    b = int(input("Ingrese otro número entero: "))
    resultado = calcular_mcm(a, b)
    print("El mínimo común múltiplo de los números ingresados es " + str(resultado))