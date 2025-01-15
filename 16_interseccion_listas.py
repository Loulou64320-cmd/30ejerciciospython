'''Interseccion de dos listas generadas por el usuario'''

import os
os.system('cls')

print('--- Interseccion de listas ---')

lista_1 = []
lista_2 = []
interseccion = []

cantidad_datos_lista1 = int(input('Cuantos datos para la lista 1: '))

# agregamos datos a la lista 1
for i in range(cantidad_datos_lista1):
    dato = int(input(f'Ingrese dato {i+1}: '))
    lista_1.append(dato)


cantidad_datos_lista2 = int(input('Cuantos datos para la lista 2: '))

# agregamos datos a la lista 2
for i in range(cantidad_datos_lista2):
    dato = int(input(f'Ingrese dato {i+1}: '))
    lista_2.append(dato)


# comparamos las listas
for i in lista_1:
    if i in lista_2:
        interseccion.append(i)

# si la lista esta con datos imprime la interseccion caso contrario da otro mensaje
if interseccion:
    print('Interseccion de las listas es: ', interseccion)
else:
    print('No se da la interseccion....')
