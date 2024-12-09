import os # Importo modulo os

os.system('cls') # Limpia la terminal

print("---CONTADOR DE PALABRAS---")

palabra = input("Ingrese su parrafo :\n")

palabra=palabra.split() # split divide la cadena en palabras

palabra=(len(palabra)) # ICuenta el numero de palabras

print(f"El parrafo que acaba de ingresar tiene {palabra} palabras")