import os
os.system('cls')

suma_total = 0

print('--- Suma de 1 hasta valor deseado ---')

valor_final = int(input('Ingrese el valor final '))

for i in range(1, valor_final):
    suma_total += i

print(f'La suma de todos los numeros desde 1 hasta el numero final {
      valor_final} es: {suma_total}')
