''' Vamos a crear la lista de colores con While '''


# os para limpiar pantalla
import os
os.system('cls')

# lista de colores
colores = []

while True:
    print('Menu Principal')
    print('1.- Ingrese color a la lista')
    print('2.- Eliminar los colores')
    print('3.- Ordenar los colores')
    print('4.- Mostrar los colores')
    print('5.- Salir')

    opcion = int(input('Elige una opcion: '))

    match opcion:
        case 1:
            datos = int(input('¿Cuantos colores quiere ingresar: ?'))
            for i in range(datos):
                color = input(f'Ingrese el color: {i+1} ')
                colores.append(color)
        case 2:
            color_a_eliminar = input('Ingrese color a eliminar: ')
            if color_a_eliminar in colores:
                colores.remove(color_a_eliminar)
                print(f'El color {
                      color_a_eliminar} se elimino satisfactoriamente')
            else:
                print('El color que desea eliminar no esta en la lista')
        case 3:
            colores.sort()
            print('La lista ha sido ordenada: ', colores)
        case 4:
            print('Lista de colores: ', colores)
        case 5:
            print('Saliendo del programa ....')
            break
