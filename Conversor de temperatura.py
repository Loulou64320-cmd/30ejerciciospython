import os

os.system('cls') 

def celsius_a_fahrenheit(grado_convertir):
    return ((grado_convertir * 9 ) /5 ) + 32

def celsius_a_kelvin(grado_convertir):
    return grado_convertir + 273.15

def fahrenheit_a_kelvin(grado_convertir):
    return (((grado_convertir - 32) * 5) / 9 ) + 273.15

def fahrenheit_a_celcius(grado_convertir):
    return ((grado_convertir - 32) * 5) / 9

def kelvin_a_fahrenheit(grado_convertir):
    return (((grado_convertir - 273.15) * 9) / 5) + 32

def kelvin_a_celsius(grado_convertir):
    return(grado_convertir - 273.15)

print("---CONVERSOR DE TEMPERATURA---")

while True:
    print("\nElija una opcion : ")
    print("---------------- ")
    print("1.- Convierte de celsius a fahreheit y kelvin")
    print("2.- Convierte de fahrenheit a kelvin y celsius")
    print("3.- Convierte de kelvin a fahrenheit y celsius")
    print("4.- Salir")

    opcion=int(input("\nIngrese una opcion y presione ENTER ")) 
    os.system('cls')
    
    match opcion:
        case 1:
            print("Usted a elegido la opciom : ")
            print("Convierte de celsius a fahreheit y kelvin")
        case 2:
            print("Usted a elejido la opcion : ")
            print("Convierte de fahrenheit a kelvin y celsius")
        case 3:
            print("Usted a elejido la opcion : ")
            print("Convierte de kelvin a celsius y fahrenheit")
        case 4:
            print("Usted ha elejido salir ")
            break
        case _:
            print("Vuelva a intentarlo, elija una opcion ")
        
    grado_convertir = float (input("\n\tIngrese el grado a convertir : "))
    
    match opcion:
        case 1:
            resultado1 = round(celsius_a_fahrenheit(grado_convertir), 2)
            resultado2 = round(celsius_a_kelvin(grado_convertir), 2)
            print(f"{grado_convertir} grados celsius a fahrenheit es : {resultado1}")
            print(f"{grado_convertir} grados celsius a kelvin es : {resultado2}")
        case 2:
            resultado1 = round(fahrenheit_a_kelvin(grado_convertir), 2)
            resultado2 = round(fahrenheit_a_celcius(grado_convertir), 2)
            print(f"{grado_convertir} grados fahrenheit a kelvin es : {resultado1}")
            print(f"{grado_convertir} grados fahrenheit a celsius es : {resultado2}")
        case 3:
            resultado1 = round(kelvin_a_celsius(grado_convertir), 2)
            resultado2 = round(kelvin_a_fahrenheit(grado_convertir), 2)
            print(f"{grado_convertir} grados kelvin a celsius es : {resultado1}")
            print(f"{grado_convertir} grados kelvin a fahrenheit : {resultado2}")