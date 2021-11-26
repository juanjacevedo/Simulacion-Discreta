#Calcular el área de un circulo de  radio 1 por método Montercarlo

def AreaTrian():
    import random as rnd
    n = int(input("Ingrese el número de simulaciones: "))
    h = 0
    for i in range(n):
        x = -1 +2*rnd.random() # x = -1 + (1-(-1))*rnd()
        y = -1 + 2*rnd.random()
        if (x**2 + y**2) < 1:
            h += 1
    return "el área es: " + str(4*h/n)

print(AreaTrian())