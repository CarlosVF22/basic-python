# imprimir todas las potencias de 2 hasta llegar al numero mil

def run():
    LIMITE = 1000000 # definimos el limite CONSTANTE

    contador = 0 # definimos el valor inicial del contador
    potencia_2 = 2 ** contador # definimos el valor incial del resultado de la potencia
    while potencia_2 < LIMITE: # mientras la potencia_2 sea menor al limite EJECUTE
        print("2 elevado a " + str(contador) + " es igual a: " + str(potencia_2))
        contador = contador + 1 # aumentamos el contador
        potencia_2 = 2 ** contador # nuevo resultado de la potencia_2


if __name__ == "__main__":
    run()