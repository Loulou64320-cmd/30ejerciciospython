import os

os.system('cls')

# Definir Constates

precio_dolar = 0.27
precio_euro = 0.26
precio_yoan = 1.95

# Definir Funciones


def sol_a_dolar(moneda):
    return moneda*precio_dolar


def sol_a_euro(moneda):
    return moneda*precio_euro


def sol_a_yuan(moneda):
    return moneda*precio_yoan


print('--- CONVERSOR DE MONEDA ---\n')


while True:
    print('1.- De Sol a Dolar')
    print('2.- De Sol a Euro')
    print('3.- De sol a Yuan')
    print('4.- Salir del conversor')

    opcion = float(input('\tIngrese su opcion y presione ENTER : '))

    match opcion:
        case 1:
            print('\tEleccion 1 de Sol a Dolar')
        case 2:
            print('\tEleccion 2 de Sol a Euro')
        case 3:
            print('\tEleccion 3 de Sol a Yuan')
        case 4:
            print('\tEsta saliendo del colversor ....')
            break
        case _:
            print('\tIngrese una opcion valida')

    moneda = int(input('\t\tIngrese su moneda a cambiar :'))

    match opcion:
        case 1:
            resultado = sol_a_dolar(moneda)
            print(f'\t\t\t{moneda} es {resultado} Dolar(es)')
        case 2:
            resultado = sol_a_euro(moneda)
            print(f'\t\t\t{moneda} es {resultado} Euro(s)')
        case 3:
            resultado = sol_a_yuan(moneda)
            print(f'\t\t\t{moneda} es {resultado} Yoan(es)')
