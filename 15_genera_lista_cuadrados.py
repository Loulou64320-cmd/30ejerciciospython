""" Vamos a crear una lista y de esta lista se generara una nueva lista con los
cuadrados de cada nuemero """

import os
os.system('cls')

print('--- Lista de cuadrados ---')

# solicitamos la cantidad de elementos
cantidad_elementos = int(input('Cauntos elementos quieres en la lista: '))

datos = []
cuadrado1 = []

for i in range(cantidad_elementos):
    dato = int(input(f'Ingrese dato {i + 1}: '))
    datos.append(dato)


cuadrado = [dato**2 for dato in datos]

for dato in datos:  # otra manera de poder hacer
    cuadrado1.append(dato**2)


print('Lista original: ', datos)
print('Lista cuadrado: ', cuadrado)
print('Lista cuadrado1: ', cuadrado1)
