import os  # libreria os para limpiar pantalla
os.system('cls')  # limpia pantalla

# crear una lista colores
colores = []

# funcion menu


def menu():
    print('\nMenu')
    print('1.-Ingresar colores')
    print('2.-Eliminar un color')
    print('3.-Ordenar los colores')
    print('4.-Muestra los colores')
    print('5.-Salir')
    opcion = int(input('Elige una opcion: '))
    return opcion


while True:
    opcion = menu()

    if opcion == 1:
        # ingresa color a la lista
        datos = int(input('¿Cuantos colores quieres ingresar?: '))
        for i in range(datos):
            color = input(f'Ingrese el color {i + 1}: ')
            colores.append(color)
    elif opcion == 2:
        # eliminar un color
        color_a_eliminar = input('Ingrese el color a eliminar: ')
        if color_a_eliminar in colores:
            colores.remove(color_a_eliminar)
            print(f'el color {
                  color_a_eliminar} ha sido eliminado satisfactoriamente')
        else:
            print(f'El color que desea eleminar no esta en la lista')
    elif opcion == 3:
        # ordena la lista de colores
        colores.sort()
        print('La lista de colores ha sido ordenada. ')
    elif opcion == 4:
        # mostrar la lista de colores
        print('lista de colores', colores)
    elif opcion == 5:
        print('Saliendo del programa ....')
        break
    else:
        print('Elija una opcion valida ')


print('Programa finalizado. ')
