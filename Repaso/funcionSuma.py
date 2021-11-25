def suma(*valores):
    total = 0

    for i in valores:
        total += i
    
    return total

print(suma(2,4,5)) #Se puede ingresar la cantidad de numeros que se quiera: suma(numero_1, numero_2, numero_3, ..., numero_n )
