def  AreaBajoLasCurvas():
    import random as rnd
    n = int(input("Ingrese el número de simulaciones:"))

    h = 0
    for i in range(n):
        x = rnd.random()
        y = rnd.random()
        if x < (0.5)**0.5:
            if y <= x**2:
                h+=1
        else:
            if y <= 1-x**2:
                h+=1
    return h/n

print(AreaBajoLasCurvas())