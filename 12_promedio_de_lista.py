import os
os.system('cls')

print('---Calcula el promedio de una lista---')

# solicitar al usuario la cantidad de elementos
cantidad_elementos = int(input('Cuantos datos quieres en la lista: '))

# crea lista de datos vacia
datos = []

for i in range(cantidad_elementos):
    dato = float(input(f'ingrese el dato {i+1}: '))
    datos.append(dato)

# calcular la suma de todos los datos en la lista
suma_total = sum(datos)

# calcula el promedio
promedio = suma_total/cantidad_elementos


print(f'el promedio de los datos de la lista es: {promedio}')
