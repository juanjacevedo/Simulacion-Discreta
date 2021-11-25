numero_filas = int(input("Ingrese el número de filas: "))
numero_columnas = int(input("Ingrese el número de columnas: "))
matriz = []

for i in range(numero_filas):
    matriz.append([])
    for j in range(numero_columnas):
        numero = int(input(
            "Ingrese el número de la matriz en la posición " + str(i) + "," + str(j) + ": "))
        matriz[i].append(numero)

print(matriz)
