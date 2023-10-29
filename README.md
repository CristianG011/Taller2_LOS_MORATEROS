# LOS MORATEROS (EL MEJOR GRUPO) PRESENTA...
Una producción de: Cristian Andres Gómez, juan Estaban Molina y Paula Isabella Moreno
# TALLER 2
![395309186_861858485377350_369559280493977603_n](https://github.com/CristianG011/Taller2_LOS_MORATEROS/assets/142249435/24a2c97f-7e82-4b2a-9dfc-f402bef839fe)
# Punto 1
Desarrollar un programa que ingrese un número entero n y separe todos los digitos que componen el número. **Pista:** Utilice los operadores módulo (%) y división entera (//).
```python
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
```
# Punto 2
Desarrollar un programa que ingrese un número flotante n y separe su parte entera de la parte decimal, y luego entregue los dígitos tanto de la parte entera como de la decimal.
```python
def digitos_flotantes():
    n = float(input("Ingrese un número flotante: "))

    entero = int(n)                #Convierte la parte entera del flotante a tipo entero
    decimal = n - entero           #Saca la parte decimal del flotante

    lista1 = []                    #Crea una lista para los dígitos de la parte entera
    while entero > 0:
        digitos = entero % 10      #Obtiene el último dígito de la parte entera
        entero = entero // 10      #Reduce la parte entera eliminando el último dígito
        lista1.append(digitos)     #Agrega los dígitos a la lista 1

    if len(lista1) == 0:           #Si la lista está vacía se devuelve el valor 0
        lista1 = [0]

    lista2 = []                    #Crea una lista para la parte decimal

    while decimal < 1:
        decimal *= 10              #Multiplica de forma iterativa la parte decimal por 10 hasta que sea mayor o igual a 1

    while decimal != int(decimal):
        lista2.append(int(decimal) % 10)  #Obtiene el último dígito de la parte decimal
        decimal = decimal * 10            #Reduce la parte decimal eliminando el último dígito

    if not lista2:
        lista2 = [0]                      #Si la lista está vacía devuelve el valor 0


    print("Los dígitos de la parte entera son:")
    print(lista1[::-1])
    print("Los dígitos de la parte decimal son:")
    print(lista2)

if __name__ == "__main__":
    digitos_flotantes()
```
# Punto 3
Desarrollar un programa que permita ingresar dos números enteros y determinar si se tratan de números espejos, definiendo números espejos como dos números a y b tales que a se lee de izquierda a derecha igual que se lee b de derecha a izquierda, y viceversa.
```python
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

```
# Punto 4
Diseñar una función que permita calcular una aproximación de la función coseno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Taylor. **nota:** use *math* para traer la función coseno y mostrar la diferencia entre el valor real y la aproximación. Calcule con cuántos términos de la serie (i.e: cuáles valores de n), se tienen errores del 10%, 1%, 0.1% y 0.001%.
$$cos(x) \approx cos(x,n) \approx \sum_{i=0}^{n} (-1)^i \frac{x^{2i}}{(2i)!}$$
```python
import math
def f(i: int):                     #para facilitar las cosas, creo una función que será el factorial
    if i == 0:                     #Se sabe que el factorial de cero es uno, por lo tanto le ordeno a la función que me retorne el 1
        return 1
    else:
        p = 1                      #Variable para ir aumentando por cada ciclo 
        for numero in range(1, i + 1): #Sabemos que el rango va hasta n-1 entonces le sumamos uno, de está forma trabajamos la función desde 1 gasta i+1
            p *= numero                #P, inicia siendo uno, y por cada ciclo toma el siguiente valor a multiplicar; De está forma sigue creciendo el valor hasta i+1
        return p                       #Retornamos el último valor
a = int(input("Ingrese número de iteraciones: ")) #Hasta dónde llega la sumatoría (n)
x = float(input("Ingrese valor x en radianes: ")) #Sabemos que los radianes toman valores relacionados con PI, para obtener una aproximación adecuada recomiendo hagar números menores a 4
suma : float = 0                  #Variable que va creciendo con el ciclo 
for s in range(a + 1):            #Para cada número que está en a+1 se va a cumplir el siguiente ciclo 
    d = d = (x ** (2 * s)) / f(2 * s)             #Acá pasan 2 cosas; Numerador, operación básica. Denominador, COMO ES EL FACTORIAL, vamos a meter el valor en la función y así queda la división
    d *= (-1) ** s                #Operación básica
    suma += d                     #Ahora si, se suma, y así susivamente hasta "a" terminos 
print(f"La aproximación de coseno de {x} es:{suma}")       #Imprima la aproximación
print(f"El valor real del coseno de {x} es:{math.cos(x)}") #Imprima el valor exacto 
z = abs((abs(suma - math.cos(x))/math.cos(x))*100)         #Compruebe la diferencia 
print(f"El porcentaje de error es de {z}")                 # Cuál es esa diferencia 
#Y se acabo ;D
```
# Punto 5
Desarrollar un programa que permita determinar el Minimo Comun Multiplo de dos numeros enteros. Abordar el problema desde una perpectiva tanto iterativa como recursiva. **Pista:** Puede ser de utilidad chequear el [Algoritmo de Euclides](https://es.wikipedia.org/wiki/Algoritmo_de_Euclides) para el cálculo del Máximo Común Divisor, y revisar cómo se relaciona este último con el Mínimo Común Múltiplo.
```python
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
```
```python
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
```
# Punto 6
Desarrollar un programa que determine si en una lista existen o no elementos repetidos. **Pista:** Maneje valores booleanos y utilice el operador *in*.
```python
def elementos_repetidos(lista):    #Definimos función para encontrar elementos repetidos
    for i in lista:
        if lista.count(i) > 1:     #Al evaluar cada elemento en la lista, si se encuentra más de una vez entonces hay repetidos
            return True            #Si es así returna True
    return False                   #Si no retorna False

if __name__ == "__main__":
    lista = []                     #Creamos la lista donde irán los números
    while True:
        entrada = input("Ingrese un número entero para el primer arreglo (Vacío para terminar): ")
        if not entrada:            #Cuando dejen de ingresarse números por computadora
            break                  #Deja de mostrar mensaje 
        numeros = int(entrada)     #Los números ingresados se convierten a entero
        lista.append(numeros)      #Agregamos los números ingresados a la lista

    if elementos_repetidos(lista): 
        print("Hay elementos repetidos")
    else:
        print("No hay elementos repetidos")

```
# Punto 7
Desarrollar un programa que determine si en una lista se encuentra
una cadena de caracteres con dos o más vocales. Si la cadena existe debe imprimirla y si no existe debe imprimir 'No existe'.
```python
def vocales(cadena):
    # Definimos una función que cuenta cuántas vocales tiene una palabra
    vocales = "A a E e I i O o U u"     # Definimos las vocales
    contador = 0                        # Inicializamos el contador a 0
    for letra in cadena:                # Iteramos a través de las letras de la palabra
        if letra in vocales:            # Si la letra es una vocal
            contador += 1               # Incrementamos el contador en 1
        if contador >= 2:               # Si hay al menos 2 vocales, terminamos la función
            return True                 # La función retorna True

if __name__ == "__main__":
    palabras = input("Ingrese palabras separadas por un espacio: ")  # Solicitamos al usuario ingresar palabras
    cadenas = palabras.split()          # Separamos las palabras en una lista llamada "cadenas"
    for cadena in cadenas:              # Iteramos a través de las palabras
        if vocales(cadena):             # Llamamos la función 'vocales' para cada palabra
            print(cadena)               # Imprimimos las palabras que tienen 2 o más vocales
        else:
            print("No existe")          # Imprimimos "No existe" para las palabras que no cumplen con la condición

```
# Punto 8
Desarrollar un programa que dadas dos listas determine que elementos tiene la primer lista que no tenga la segunda lista. 
```python
#Para este código voy a utilizar 2 listas vacias a las cuales, iré añadiendo n términos y una tercera a la cual voy a añadir los terminos iguales 
lista1 = []
lista2 = []
lista3 = []
j = int(input("Ingrese la cantidad de valores: "))   #Cuántas palabras o números vas a usar 
for Valores in range (j):                            #Ahora, según la cantidad que elegiste, vamos hacer esa cantidad de veces el ciclo, para añadir esa cantidad de terminos(El código está adaptado para que puedas elegir no poner nada)
    Valor = (input("Ingrese un número o palabra: ")) # Está es obvia xD
    lista1.append(Valor)                             #IMPORTANTE CON EL APPEND ES QUE SE METEN O INTRODUCEN LOS VALORES EN LA LISTA 
x = int(input("Ingrese la cantidad de valores: "))   #Repitis
for Valores1 in range (x):
    Valor2 = (input("Ingrese un número o palabra: "))
    lista2.append(Valor2)
for x in lista1:            #Listo tenemos 2 listas, ahora hagamos un ciclo, para cada valor en la lista 1; 
  if x in lista2:           #ahora si, x está en la lista 2, 
    lista3.append(x)        #Lo vas a meter en la lista 3, si no pos no
print(f"{lista1}")          #Para que se vea bonito, imprime la lista uno y dos
print(f"{lista2}")
print(f"{lista3}")          #Y ahora las que tienen de semejanzas
#Y se acabo ;D
```
# Punto 9
Resolver el punto 7 del [taller 1](https://github.com/fegonzalez7/pdc_unal_clase8) usando operaciones con vectores.
```python
lista = []                                                #Creo la primera lista vacia

j = int(input("Ingrese la cantidad de valores: "))        #Cuántas palabras o números vas a usar
for Valores in range (j):                                 #Ahora, según la cantidad que elegiste, vamos hacer esa cantidad de veces el ciclo, para añadir esa cantidad de terminos(El código está adaptado para que puedas elegir no poner nada)
    Valor = float(input("Ingrese un número real: "))
    lista.append(Valor)                                   #IMPORTANTE CON EL APPEND ES QUE SE METEN O INTRODUCEN LOS VALORES EN LA LISTA

def prom(lista):                                          #Primera función, está será usada para el promedio, con los números de "lista"
    s = sum(lista)                                        #S, variable que va a tomar el valor de la suma de la lista con el comando sum
    promed = s/len(lista)                                 #Ahora divido la suma por la cantidad de valores dentro de la lista,(el comando len cuenta la cantidad de valores dentro de una lista)
    return promed                                         #Retorne el promedio

promedio = prom(lista)                                    #Defino que promedio va a ser igual los números dentro de la lista en la función(O sea mete los valores de la lista en la funcion y trabaja,vago)



def prommultiplicativo(lista):                            #Segunda función, está será usada para el promedio multiplicativo
    x = 1                                                 #Voy a usar un ciclo, en ese caso la variable que va cambiando según cada ciclo,(inicia en uno)
    for valor in lista:                                   #Para cada número en la lista
        x = x * valor                                     #Vamos a multiplicar el número anterior entregado por el valor actual del ciclo
    p = x ** (1/len(lista))                               #Ahora le sacamos raíz de la cantidad de numeros ingresados al resultado
    return p                                              #Retorne el promedio multiplicativo
promedioM = prommultiplicativo(lista)                     #Defino que promedio va a ser igual los números dentro de la lista en la función(O sea mete los valores de la lista en la funcion y trabaja)

def mediana(lista):                                                         #Tercera función, está será usada para la mediana
    lista.sort()                                                            #ordena la lista, si es impar el valor es el del medio, sino es el promedio de los 2 valores del medio
    if len(lista) % 2 == 1:                                                 #divide en 2, si es igual a 1 entonces dio impar entonces                                                  
        mediana = lista[len(lista)//2]                                      #Se hace la operación para que tome el valor que está en medio
    else:                                                                   #Es par, entonces
        mediana = lista[(len(lista)//2) -1] + lista[len(lista)//2] / 2      #Hacer el promedio de los valores en medio(sumas los 2 y luego los divides en 2)
    return mediana                                                          #Retorna la mediana 
mediana = mediana(lista)                                                    
def ordenasd(lista):                                      #Cuarta función, con ella voy a ordenar los valores
    ordenA = sorted(lista)                                #Está es muy simple, con sort ordenamos la función
    return ordenA                                         #Y ahora retorna la función ordenada 
ordenascendente = ordenasd(lista)
def ordendes(lista):                                      #Quinta, está la usaré para invertir la función anterior
    ordenD = sorted(lista)                                #Como es muy parecido el proceso simplemente la ordeno
    ordenD = lista[::-1]                                  #Y acá se invierte(Estaer egg: No me acordaba como hacer está vrg* en el parcial ;v)
    return ordenD                                         #Retorne la función ordenada e invertida  
ordendescendente = ordendes(lista)
                                                          #Imprimimos todo :D, a ver si sirve,y si sirve >:)  
print(lista)
print(promedio)
print(promedioM)
print(mediana)
print(ordenascendente)
print(ordendescendente)
#Y se acabo ;D
```
# Punto 10
Suponga que se tiene una lista A con ciertos números enteros. Desarrolle una función que, independientemente de los números que se encuentran en la lista A, tome aquellos números que son múltiplos de 3 y los guarde en una lista nueva, la cual debe ser **retornada** por la función. Implemente la perspectiva de un *patrón de acumulación* y también de *comprensión de listas*. **Desafío:** Si ya lo logró, inténtelo ahora sin utilizar el módulo (%). **Pista:** Un número es multiplo de 3 si la suma de sus dígitos también lo es, ¿verdad?
```python
#Comprensión de listas

def multiplos_3():       #Definimos la función para calcular los múltiplos de 3
    lista = []           #Creamos la lista donde irán todos los números ingresados
    while True:
        entrada = input("Ingrese un número entero para el primer arreglo (Vacío para terminar): ")
        if not entrada:  #Si dejan de ingresarse números por computadora
            break        #Deja de mostrar mensaje
        numeros = int(entrada)   #Convierte los números a enteros
        lista.append(numeros)    #Agregamos los números ingresados a la lista

    return lista            

if __name__ == "__main__":
    lista = multiplos_3()       

    lista_multiplos = []                #Creamos otra lista donde irán los múltiplos de 3
    for i in lista:                     #Para cada valor i en la lista
        if i % 3 == 0:                  #Evaluamos si el residuo de la división entre este y 3 es 0
            lista_multiplos.append(i)   #Si es así se agrega a la lista de múltiplos de 3

    print(lista)

    if lista_multiplos:
        print("Los múltiplos de 3 de la lista son: " + str(lista_multiplos))
    else:
        print("Ningún número es múltiplo de 3")
```
```python
#Patrón de acumulación

def multiplos_3():        #Definimos la función para encontrar múltiplos de 3
    lista = []            #Creamos la lista donde irán los números ingresados
    while True:
        entrada = input("Ingrese un número entero para el primer arreglo (Vacío para terminar): ")
        if not entrada:             #Si dejan de ingresarse números por computadora 
            break                   #Deja de mostrar mensaje
        numeros = int(entrada)      #Convierte los números ingresados a enteros
        lista.append(numeros)       #Se agregan los números a la lista
    return lista

if __name__ == "__main__":
    lista = multiplos_3()

    lista_multiplos = []                 #Se crea la lista donde irán los múltiplos de 3
    for i in lista:                      #Para cada valor i dentro de la lista
        num = i                          #Añadimos i a la variable num
        while num >= 3:                  #Siempre cuando se cumpla que num es mayor o igual a 3
            num -= 3                     #Resta iterativamente dicho valor de 3 en 3
        if num == 0:
            lista_multiplos.append(i)    #Si el valor llega a 0 añade los valores a la lista creada para los múltiplos de 3

    if lista_multiplos:
        print("Los múltiplos de 3 de la lista son: " + str(lista_multiplos))
    else:
        print("Ningún número es múltiplo de 3")
```
