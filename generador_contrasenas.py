import random

def generar_contrasena():
    MAYUS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    MINUS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    CHARS = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']

    characters = MAYUS + MINUS + NUMS + CHARS # creamos una lista que contenga todas las lista ya creadas

    contrasena = [] # guardamos caracteres elegidos al azar

    for i in range(15): # con el rango definimos la cantidad de caracteres que queremos en la contraseña
        characters_random = random.choice(characters) # funcion especial del modulo random, eligo caracter al azar de toda la lista
        contrasena.append(characters_random) # agregamos a contrasena el character random generado

    contrasena = ''.join(contrasena) # convirtiendo una lista a un string, con comillas simples ''
    return contrasena

def run():
    contrasena = generar_contrasena()
    print("Tu nueva contraseña es: " + contrasena)


if __name__ == '__main__':
    run()