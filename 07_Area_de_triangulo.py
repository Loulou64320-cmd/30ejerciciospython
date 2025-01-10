def area_triangulo(base, altura):
    area = (base*altura)/2
    return area


base = int(input('Ingrese base: '))
altura = int(input('Ingrese altura: '))

resultado = int(area_triangulo(base, altura))

print(f'El area del triangulo es: {resultado}')
