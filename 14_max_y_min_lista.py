print('---Maximo y Minimo de una lista---')

# solicitar cuando datos queremos comparar
cantidad_datos = (int(input('Cuantos datos quieres en la lista: ')))

# creamos lista
datos = []

# agregar datos a la lista
for i in range(cantidad_datos):
    dato = int(input(f'Ingrese dato {i+1}: '))
    datos.append(dato)  # aqui se agrega dato a la lista datos

dato_mayor = max(datos)  # max funcion que permite encontrar el dato maximo
dato_menor = min(datos)  # min funcion que permite encontrar el dato minimo

# mostramos en consola con print
print('La lista de datos es: ', datos)
print(f'El valor maximo en la lista es: {dato_mayor}')
print(f'El valos minimo en la lista es: {dato_menor}')
