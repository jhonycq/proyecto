animales = []
animales1 = {'especie':'elefante', 'población':500,'ubicación':'brazil'}

cantidad_de_animales = int(input('Ingrese la cantidad de animales que desea agregar: '))
                              
for c in range(cantidad_de_animales):
    Especie = input('ingrese la especie que desea añadir a la lista: ')
    Población  = int(input('ingrese el número de población de la especie: '))
    Ubicación = input('ingrese Pais o Continente: ')
    Agregar_especie = {'especie':Especie, 'población':Población,'ubicación':Ubicación}
    animales.append(Agregar_especie)
        
    if Población >= 1 and Población <= 10000:
        print('Especie en vias de extinción !!')
    
    elif Población >= 10000:
        print('Especie fuera de peligro de extinción !!')
    
    elif Población == 0:
        print('Animal extinto !!')

    else:
        print('La cantidad de poblacion ingresado es incorrecto !!')

    for lista_de_animales in animales:
            print(lista_de_animales)