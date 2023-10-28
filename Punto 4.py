import math
def f(i: int):
    if i == 0:
        return 1
    else:
        p = 1
        for numero in range(1, i + 1):
            p *= numero
        return p
a = int(input("Ingrese número de iteraciones: "))
x = float(input("Ingrese valor x en radianes: "))
suma : float = 0
for s in range(a + 1):
    d = d = (x ** (2 * s)) / f(2 * s)
    d *= (-1) ** s
    suma += d
print(f"La aproximación de coseno de {x} es:{suma}")
print(f"El valor real del coseno de {x} es:{math.cos(x)}")
z = (abs(suma - math.cos(x))/math.cos(x))*100
print(f"El porcentaje de error es de {z}")
