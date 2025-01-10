import os
os.system('cls')


def perimetro_rectangulo(base, altura):
    perimetro = (base*base)+(altura*altura)
    return perimetro


def area_rectangulo(base, altura):
    area = base*altura
    return area


base = int(input('Ingrese la base: '))
altura = int(input('Ingrese la altura: '))

perimetro = perimetro_rectangulo(base, altura)
area = area_rectangulo(base, altura)

print(f'El Perimetro del rectangulo es: {perimetro}')
print(f'El area del rectangulo es: {area}')
