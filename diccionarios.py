# puedo recorrer diccionarios

def run():
    mi_diccionario = { #Creamos un diccionario, es una estructura de datos
        'llave1':1, #creamos elementos
        'llave2':2,
        'llave3':3,
    }
    
    # print(mi_diccionario['llave1']) # accedemos a un elemento en particular
    # print(mi_diccionario['llave2'])
    # print(mi_diccionario['llave3'])

    poblaciones_paises ={
        'Argentina':44938712,
        'Brasil':210147125,
        'Colombia': 50372424,
    }

    # print(poblaciones_paises['Argentina'])

    # for pais in poblaciones_paises.keys(): # metodo del diccionario que devuelve las llaves
    #     print(pais)

    # for pais in poblaciones_paises.values(): # metodo del diccionario que devuelve los valores
    #     print(pais)

    for pais,poblacion in poblaciones_paises.items(): # metodo del diccionario que devuelve las llaves y el valor
        # print(pais,poblacion) #asi tambien se puede imprimir
        print (pais + ' tiene ' + str(poblacion) + ' habitantes')

if __name__ == "__main__":
    run()