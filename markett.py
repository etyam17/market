

def pedir_opcion_valida(mensaje, opciones_validas):
    opcion = input(mensaje)
    while opcion not in opciones_validas:
        print("Opción inválida, intenta de nuevo.")
        opcion = input(mensaje)
    return opcion


def mostrar_menu(titulo, nombres, precios):

    print(f"*-----------{titulo}-----------*")

    opciones_validas = []
    for i in range(len(nombres)):
        numero = i + 1
        print(f"{numero}.{nombres[i]}______________${precios[i]}")
        opciones_validas.append(str(numero))

    print("*-----------------------------*")

    opcion = pedir_opcion_valida("Ingresa tu pedido: ", opciones_validas)

    indice = int(opcion) - 1
    return precios[indice], nombres[indice]


def main():
    categorias = {
        "1": ("LACTEOS", ["Leche", "Queso", "Yogurt", "Mantequilla"], [1, 2, 2, 3]),
        "2": ("EMBUTIDOS", ["Jamón", "Salchicha", "Chorizo", "Mortadela"], [3, 2, 3, 2]),
        "3": ("SNACKS", ["Dorito", "Galleta", "Canguil", "Chocolates"], [1, 1, 1, 2]),
        "4": ("VERDURAS", ["Zanahorias", "Lechuga", "Tomates", "Pepino"], [1, 1, 1, 1]),
        "5": ("FRUTAS", ["Manzana", "Uvas", "Fresas", "Naranjas"], [2, 2, 3, 2]),
    }

    nombres_menu_principal = {
        "1": "Lacteos",
        "2": "Embutidos",
        "3": "Snacks",
        "4": "Verduras",
        "5": "Frutas",
    }

    orden = []
    total = 0
    salir = False

    print("*--------------------------------*")
    print("*---BIENVENIDO A DIEGOS MARKET---*")
    print("*--------------------------------*")
    nombre = input("Cual es tu nombre? ")

    while not salir:
        print(f"Bienvenido/a {nombre}")
        print("Que deseas ordenar?")
        print("*--------------MENU--------------*")
        for clave in categorias:
            print(f"{clave}.{nombres_menu_principal[clave]}")
        print("*---------------------------------*")

        categoria = pedir_opcion_valida("> ", list(categorias.keys()))
        titulo, nombres, precios = categorias[categoria]

        factura, detalle = mostrar_menu(titulo, nombres, precios)

        total += factura
        orden.append(detalle)

        continuar = input("¿Desea pedir algo más? (y , n) ")
        if continuar == "n":
            salir = True

    print("*-----------FACTURA-----------*")
    print("Esto esta en tu carrito")

    for producto in orden:
        print(producto + ",", end=" ")
    print()

    print("Tu total es: $", total)
    print(f"Gracias por tu compra {nombre}")
    print("*-----------------------------*")


if __name__ == "__main__":
    main()
