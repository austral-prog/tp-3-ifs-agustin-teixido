def grades():
    """
    Ejercicio 5 - Clasificar Notas

    Leer una nota (0-10) mediante input(). Clasificar la nota e imprimir:
    - "Excelente" si está entre 9 y 10
    - "Bueno" si está entre 7 y 8
    - "Regular" si está entre 5 y 6
    - "Insuficiente" si está entre 0 y 4

    Ejemplo:
        Para la entrada "9", la salida esperada es:
        Excelente

        Para la entrada "6", la salida esperada es:
        Regular

        Para la entrada "3", la salida esperada es:
        Insuficiente
    """
    pass

    nota = input("Ingrese la nota: ")

    if nota in ["9", "10"]:
        print("Excelente")
    elif nota in ["7", "8"]:
        print("Bueno")
    elif nota in ["5", "6"]:
        print("Regular")
    elif nota in ["0", "1", "2", "3", "4"]:
        print("Insuficiente")
    else:
        print("Error")



