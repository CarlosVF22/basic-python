valorDolar = 3800
valorPeso = 0.00026
moneda_inicial = int(input("Escoge la moneda que tienes y quieres convertir: (1)Cop , (2)Dolares: "))
monto_inicial = float(input("introduce la cantidad de dinero: "))
if (moneda_inicial == 1):
    valorConvertido = monto_inicial/valorDolar
    monto_inicial = str(monto_inicial)
    valorConvertido = round(valorConvertido,2)
    valorConvertido = str(valorConvertido)
    print("El valor de tus "+monto_inicial+" en dolares es: $" + valorConvertido)
elif(moneda_inicial ==2):
    valorConvertido = monto_inicial*valorDolar
    monto_inicial = str(monto_inicial)
    valorConvertido = str(valorConvertido)
    print("El valor de tus "+monto_inicial+" en Cop es: " + valorConvertido)
else:
    print("no introdujiste un numero valido")
