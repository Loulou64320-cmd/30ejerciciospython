import random
import os

os.system('cls')

print('--- ADIVINA UN NUMERO GENERADO AL AZAR ---')

print('\nAdivina numero entre 1 y 10')


def numero_aleatorio(mi_numero):
    numero_aleatorio = random.randint(1, 10)
    return numero_aleatorio


mi_numero = int(input('\tIngrese su numero : '))

resultado = numero_aleatorio(mi_numero)


if numero_aleatorio == mi_numero:
    print('\t\tFelicitaciones encontraste el numero ')
    print(f'\t\tEl numero era {resultado}')
else:
    print('\t\tLo siento no lo encontraste ')
    print(f'\t\tEl numero era {resultado}')
