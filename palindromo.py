# correr linea por linea es una mala practica
# crear una funcion que corra el programa es una buena practica
# siempre dejar dos espacios entre cada funcion

def palindromo(palabra):
    palabra = palabra.replace(" ", "") # quitando los espacios
    palabra = palabra.lower() # palabra a minusculas
    palabra_invertida = palabra[::-1] # palabra invertida
    if palabra == palabra_invertida: # comparando ambas palabras
        return True
    else:
        return False


def run():
    palabra = input("escribe una palabra: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print("Es palindromo")
    else:
        print("no es palindromo")


# Creando el entry point
if __name__ == "__main__":
    run()