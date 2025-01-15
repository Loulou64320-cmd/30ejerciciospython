""" Juego 21 para python """

# importar libreria random
import random
import os
os.system('cls')


# funcion que reparte cartas al azar
def repartir_carta():
    return random.randint(1, 11)


# funcion para jugar
def jugar_21():
    print('Bienvenidos  al juego 21')

    mano_jugador = []
    mano_casa = []

    # repartir dos cartas al jugado y a la casa
    for i in range(2):
        mano_jugador.append(repartir_carta())
        mano_casa.append(repartir_carta())

    # mostrar cartas
    print(f'Tu mano: {mano_jugador}, total: {sum(mano_jugador)}')
    print(f'Mano visible de la casa: {mano_casa[0]}')

    # comprovamos que el jugador tenga menos de 21
    while sum(mano_jugador) < 18:
        accion = input('Desea pedir otra carta? (s/n): ')
        if accion.lower() == 's':
            mano_jugador.append(repartir_carta())
            print(f'Tu mano: {mano_jugador}, total: {sum(mano_jugador)}')
        else:
            break

    # mostrar mano del jugador
    print(f'Tu total: {sum(mano_jugador)}')

    # comprovamos manos de la casa
    while sum(mano_casa) < 17:
        mano_casa.append(repartir_carta())

    # mostrar el total de todas la casa
    print(f'Mano de la casa: {mano_casa}, total: {sum(mano_casa)}')

    # determinamos el ganador del juego
    if sum(mano_jugador) > 21:
        print('Te has pasado de 21!! La casa gana.')
    elif sum(mano_casa) > 21 or sum(mano_jugador) > sum(mano_casa):
        print('Felicidades tu ganas.')
    elif sum(mano_jugador) == sum(mano_casa):
        print('Es un empate, casa gana.')
    else:
        print('Casa gana.')


# iniciamos el juego
jugar_21()
