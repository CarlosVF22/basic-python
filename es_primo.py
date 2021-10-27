# un numero primo es aquel que solo puede dividirse por si mismo y por uno

def es_primo(numero):
    contador = 0 # definimos contador
    for i in range(1,numero+1): 
        if i == 1 or i == numero:
            continue
        if numero % i == 0 : #obtenemos division exacta cuando el numero sea divisible por otro numero que no sea el mismo o uno
            contador += 1 # aumentamos el contador cuando el numero no es primo
    if contador == 0:
        return True
    else :
        return False


def run():
    numero = int(input('Escribe un numero: '))
    if es_primo(numero): # si es_primo es True
        print('Es primo')
    else:
        print('No es primo')


if __name__ == '__main__':
    run()