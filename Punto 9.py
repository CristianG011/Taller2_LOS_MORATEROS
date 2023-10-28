lista = []

j = int(input("Ingresa la cantidad de valores: "))
for Valores in range (j):
    Valor = float(input("Ingrese un número real: "))
    lista.append(Valor) 

def prom(lista):
    s = sum(lista)
    promed = s/len(lista)
    return promed

promedio = prom(lista)


def prommultiplicativo(lista):
    x = 1
    for valor in lista:
        x = x * valor
    p = x ** (1/len(lista))
    return p
promedioM = prommultiplicativo(lista)

def mediana(lista):
    lista.sort()
    if len(lista) % 2 == 1:
        mediana = lista[len(lista)//2]
    else:
        mediana = lista[(len(lista)//2) -1] + lista[len(lista)//2] / 2
    return mediana
mediana = mediana(lista)
def ordenasd(lista):
    ordenA = sorted(lista)
    return ordenA
ordenascendente = ordenasd(lista)

print(lista)
print(promedio)
print(promedioM)
print(mediana)
print(ordenascendente)

