# def imprimir_mensaje():
#     print ("mensaje especial: ")
#     print("estoy aprendiendo a usar funciones")

# imprimir_mensaje()
# imprimir_mensaje()
# imprimir_mensaje()


def conversacion(mensaje):
    print("hola")
    print("como estas")
    print(mensaje)
    print("adios")

opcion = int(input("Elige una opcion (1,2,3): "))
if opcion == 1:
    conversacion("elegiste opcion 1")
elif opcion ==2:
    conversacion("elegiste opcion 2")
elif opcion ==3:
    conversacion("elegiste opcion 3")
else:
    print("Elige una opcion correcta")

