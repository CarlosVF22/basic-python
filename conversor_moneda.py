# creando cadena de caracteres de varias lineas
# windows. (punto) para agregar emojis
# es importante que las funciones esten en la parte mas arriba del codigo

def conversor(tipo_pesos, valor_dolar ):
    pesos = input("Cuantos pesos " + tipo_pesos + " tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("tienes $:" + dolares + " dolares")

menu = """
    Bienvenido al conversor de moendas 💲

    1-Pesos colombianos
    2-Pesos argentinos
    3-Pesos mexicanos

    Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    conversor("Colombianos", 3875)
elif opcion == 2:
    conversor("Argentinos", 65)
elif opcion == 3:
    conversor("Mexicanos", 24)
else:
    print("Agrega una opcion valida")
