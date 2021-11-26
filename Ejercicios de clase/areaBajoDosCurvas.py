#Calcular el área bajo las curvas y = 1-x**2 ^ y = x**2 con c en el intervalo (0,1)

import random as rnd 
def AreaBajoLascurvas():
    n = int(input("Ingrese el número de simulaciones: "))

    h = 0

    for i in range(n):
        x = rnd.random()
        y = rnd.random()
        if y <= (1-x**2) and y <= x**2:
            h+=1
    return h/n


print(AreaBajoLascurvas())