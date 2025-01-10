import random
import os

os.system('cls')


def repartir_carta():
    # Generar una carta aleatoria entre 1 y 11
    return random.randint(1, 11)


def jugar_21():
    print("¡Bienvenido al juego de 21!")

    # Inicializar las manos del jugador y la casa
    mano_jugador = []
    mano_casa = []

    # Repartir dos cartas al jugador y dos cartas a la casa
    for _ in range(2):
        mano_jugador.append(repartir_carta())
        mano_casa.append(repartir_carta())

    # Mostrar las cartas del jugador y una carta de la casa
    print(f"Tu mano: {mano_jugador}, total: {sum(mano_jugador)}")
    print(f"Carta visible de la casa: {mano_casa[0]}")

    # Bucle del jugador
    while sum(mano_jugador) < 18:
        accion = input("¿Deseas pedir otra carta? (s/n): ")
        if accion.lower() == 's':
            mano_jugador.append(repartir_carta())
            print(f"Tu mano: {mano_jugador}, total: {sum(mano_jugador)}")
        else:
            break

    # Mostrar el total del jugador
    print(f"Tu total: {sum(mano_jugador)}")

    # Bucle de la casa
    while sum(mano_casa) < 17:
        mano_casa.append(repartir_carta())

    # Mostrar las cartas de la casa y el total
    print(f"Mano de la casa: {mano_casa}, total: {sum(mano_casa)}")

    # Determinar el resultado del juego
    if sum(mano_jugador) > 21:
        print("¡Te has pasado de 21! La casa gana.")
    elif sum(mano_casa) > 21 or sum(mano_jugador) > sum(mano_casa):
        print("¡Felicidades! Tú ganas.")
    elif sum(mano_jugador) == sum(mano_casa):
        print("Es un empate.")
    else:
        print("La casa gana.")


# Iniciar el juego
jugar_21()
