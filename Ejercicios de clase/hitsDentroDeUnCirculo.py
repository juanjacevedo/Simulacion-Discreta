#Calcular el área de un circulo de  radio 1 por método Montercarlo

def AreaTrian():
    import random as rnd
    n = int(input("Ingrese el número de simulaciones: "))
    i = 0
    H = 0
    for i in range(n):
        x = rnd.random()
        y = rnd.random()
        if (x**2 + y**2) <= 1:
            H+=1
    return "El área es: " + str(4*H/n)

print(AreaTrian())