import os
os.system('cls')

colores = []


def menu():
    print('Menu Principal')
    print('1.- Ingresar colores')
    print('2.- Eliminar un color')
    print('3.- Ordenar los colores')
    print('4.- Mostrar los colores')
    print('5.- Salir')

    opcion = int(input('Elige una opcion: '))
    return opcion


opcion = 0
while opcion != 5:
    os.system('cls')
    opcion = menu()

    while opcion == 1:
        # Ingresar color a la lista
        datos = int(input('Cuantos colores quieres ingresar: '))
        for i in range(datos):
            color = input(f'Ingrese el color {i+1}: ')
            colores.append(color)
        opcion = 0  # reinicia la opcion

    while opcion == 2:
        # Color a eliminar
        color_a_eliminar = input('Ingrese color a eliminar: ')
        if color_a_eliminar in colores:
            colores.remove(color_a_eliminar)
            print(f'El color {color_a_eliminar} ha sido eleminado ')
        else:
            print('El colo que desea eliminar no esta en la lista')
        opcion = 0

    while opcion == 3:
        # Ordenar lista
        colores.sort()
        print('La lista ha sido ordenada.')
        opcion = 0

    while opcion == 4:
        # Mostra la lista de colores
        print('Lista de colores', colores)
        opcion = 0
