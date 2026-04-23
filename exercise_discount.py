def discount():
    """
    Ejercicio 9 (Integrador) - Sistema de Descuentos

    Crear un sistema de descuentos para una tienda. Leer mediante input():
    1. El precio unitario de un producto (decimal)
    2. La cantidad de unidades a comprar (entero)

    Calcular el total aplicando los siguientes descuentos según la cantidad:
    - Si compra 10 o más unidades: 20% de descuento
    - Si compra entre 5 y 9 unidades: 10% de descuento
    - Si compra menos de 5 unidades: sin descuento

    Imprimir:
    1. El subtotal (precio × cantidad)
    2. El porcentaje de descuento aplicado
    3. El monto del descuento
    4. El total final

    Ejemplo:
        Para las entradas "100" y "12", la salida esperada es:
        Subtotal: 1200.0
        Descuento aplicado: 20%
        Monto de descuento: 240.0
        Total final: 960.0
    """

    #presio = float(input("Ingrese el precio del producto: "))
    presio = float(input())
    #cantidad = int(input("Ingrese la cantidad: "))
    cantidad = int(input())
    descuento = 0

    if cantidad >= 10:
        descuento = 0.20
    elif cantidad >= 5 and cantidad <= 9:
        descuento = 0.10
    elif cantidad <= 5:
        descuento = 0
    else:
        print("Error")

    subtotal = presio * cantidad
    print(f"Subtotal: {subtotal}")

    if descuento == 0.20:
        print("Descuento aplicado: 20%")
    elif descuento == 0.10:
        print("Descuento aplicado: 10%")
    elif descuento == 0:
        print("Descuento aplicado: 0%")
    else:
        print("Error 2")

    mon_des = subtotal * descuento
    print(f"Monto de descuento: {mon_des}")

    print(f"Total final: {subtotal - mon_des}")

#discount()