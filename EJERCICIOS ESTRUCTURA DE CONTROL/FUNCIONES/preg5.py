
"""
5. Defina una función que, dado el valor de los tres lados de un triángulo, devuelva la longitud
de su perímetro.

"""

def longitu_perimetro(lado1,lado2,lado3):
    return (lado1+lado2+lado3)

if __name__ == '__main__':
    print("LONGITUD DEL PERIMETRO DE UN TRIANGULO")
    lado1 =float(input('Ingresa lado 1 : ')) #
    lado2 =float(input('Ingresa lado 2 : ')) #
    lado3 =float(input('Ingresa lado 3 : ')) #

    longPerimetro=longitu_perimetro(lado1,lado2,lado3)
    print('EL PERIMETRO DEL TRIANGULO ES : ',longPerimetro)




