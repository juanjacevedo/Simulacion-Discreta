try:

    cantidad = int(input("Ingrese la cantidad de estudiantes: "))
    arreglo = []
    bandera = True

    while bandera:
        if len(arreglo) < cantidad:
            nombre = input("Agregue el nombre: ")
            arreglo.append(nombre)
        else:
            bandera = False
            for i in arreglo:
                print("Hola", i, end="")
                print(", bienvenido(a) al curso de simulación")

except:

    print("Ingresó un dato erroneo")