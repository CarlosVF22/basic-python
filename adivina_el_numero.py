import random # importando modulo random de python, trabajar con ALEATORIEDAD


def run():
    numero_aleatorio = random.randint(1,100) # accedemos a las funciones del modulo, en este caso generar un numero random entero entre 1 y 100    numero_elegido = int(input("Elige un numero del 1 al 100: "))
    numero_elegido = int(input("Elige un numero entre 1 a 100: "))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print("Intenta con un numero mas grande")
        else:
            print("Intenta con un numero mas pequeño")
        numero_elegido = int(input("elige otro numero: "))
    print("¡Ganaste!")


if __name__ == '__main__':
    run()

