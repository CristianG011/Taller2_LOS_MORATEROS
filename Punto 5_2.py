#Forma Recursiva
def calcular_mcd(a, b):       #Definimos función para calcular el máximo común divisor de forma recursiva
  if b == 0:                  #Caso base para cuando el segundo número ingresado sea 0
        return a
  else:
        return calcular_mcd(b, a % b)   #Función recursiva que implementa el algoritmo de Euclides

def calcular_mcm(a, b):       #Definimos función para calcular el mínimo común múltiplo
    mcd = calcular_mcd(a, b)
    return (a * b) // mcd     #Como en el ejemplo anterior, la multiplicación entre los números ingresados dividido entre el máximo común divisor nos da el mínimo común múltiplo

a = int(input("Ingrese un número entero: "))
b = int(input("Ingrese otro número entero: "))
mcm = calcular_mcm(a, b)
print("El mínimo común múltiplo de los números ingresados es " + str(mcm))