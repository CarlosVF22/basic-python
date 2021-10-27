def factorial(numero):
    factorial_total = 1
    while numero >1:
        factorial_total = factorial_total*numero
        numero = numero - 1
    return factorial_total


def teorema_wilson(numero):
    numero = numero-1
    resultado = factorial(numero)
    resultado = resultado + 1
    numero = numero + 1
    if resultado % numero == 0:
        return True
    else:
        return False


def run():
    numero = int(input("ingresa un numero: "))
    if teorema_wilson(numero): # si es_primo es True
        print('Es primo')
    else:
        print('No es primo')


if __name__ == '__main__':
    run()