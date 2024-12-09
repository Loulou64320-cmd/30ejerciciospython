import random # Import modulo random
import string # Importa string
import os

def generar_contraseña(longitud_de_contraseña):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    contraseña = ''.join(random.choice(caracteres) for i in range(longitud_de_contraseña))
    
    return contraseña

os.system('cls') 

print("\n--- GENERA CONTRASEÑA ALEATORIA ---")

longitud_de_contraseña = int(input("\n\tIngrese la longitud para su contraseña : "))

contraseña = generar_contraseña(longitud_de_contraseña)
print(f"\tContraseña generada : {contraseña}")