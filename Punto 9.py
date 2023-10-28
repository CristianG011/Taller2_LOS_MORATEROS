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

