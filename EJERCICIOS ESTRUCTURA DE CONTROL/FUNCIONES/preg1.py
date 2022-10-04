"""""
1. Defina una función llamada area_circulo que, a partir del radio de un círculo, devuelva el
valor de su área. Recuerda que el área de un círculo es 𝜋𝑟
"""
import math
def area_circulo(radio):
    return math.pi * radio ** 2 

if __name__ == '__main__':
    radio =float(input('Ingresa el radio de un circulo : '))
    area=area_circulo(radio)
    print('El radio del circulo es : ',area)


