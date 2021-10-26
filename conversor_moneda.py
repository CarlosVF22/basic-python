# creando cadena de caracteres de varias lineas
#windows. (punto) para agregar emojis
menu = """
    Bienvenido al conversor de moendas 💲

    1-Pesos colombianos
    2-Pesos argentinos
    3-Pesos mexicanos

    Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    pesos = input("Cuantos pesos Colombianos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 3875
    dolares = pesos / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("tienes $:" + dolares + " dolares")
elif opcion == 2:
    pesos = input("Cuantos pesos Argentinos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 65
    dolares = pesos / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("tienes $:" + dolares + " dolares")
elif opcion == 3:
    pesos = input("Cuantos pesos Mexicanos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 24
    dolares = pesos / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("tienes $:" + dolares + " dolares")
else:
    print("Agrega una opcion valida")
