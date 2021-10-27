# solo vamos a imprimir los numeros pares
# break y continue se pueden utilizar en todos los tipos de ciclo

def run():
    for contador in range(1000):
        if contador % 2 != 0 : # si contador modulo 2 es diferente de 0
            continue # si el if es True no ejecuta lo que esta debajo del continue
        print(contador) # solo imprimimos numero pares

    for i in range (10000):
        print(i)
        if i == 5678: # si i vale 5678 voy a cortar el ciclo y para la ejecucion del ciclo
            break

    texto = input("Escribe un texto: ")
    for letra in texto:
        if letra == "o": # si nos encontramos con la letra "o" corta el ciclo
            break
        print(letra)



if __name__ == '__main__':
    run()