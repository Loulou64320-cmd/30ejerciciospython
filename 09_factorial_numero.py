import os
os.system('cls')

"""lista = []

#solicitar al usuario que ingrese un numero
numero_factorial = int(input('Ingrese un numero para calcular factorial: '))

for i in range(numero_factorial):
    datos = i + 1
    lista.append(datos)

lista.reverse()

lista_nueva = lista.copy() 

factorial = 1
for i in range(len(lista_nueva)):
    factorial *= lista_nueva[i]


print(f'El factorial de {numero_factorial}! es {factorial}')"""

# Solicitar al usuario que ingrese un número
numero = int(input("Ingrese un número para calcular su factorial: "))

# Inicializar el factorial en 1
factorial = 1

# Calcular el factorial utilizando un bucle for
for i in range(1, numero + 1):
    factorial *= i

# Mostrar el resultado
print(f"El factorial de {numero}! es {factorial}")
