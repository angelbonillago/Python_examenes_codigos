"""
6. Defina una función que, dados dos parámetros b y x, devuelva el valor de logb(x), es decir,
el logaritmo en base b de x.

"""
import math

def log(b,x):
    return math.log(x,b)


if __name__ == '__main__':
    print("Logaritmo en base b de x")
    b =int(input('Ingresa b : ')) #
    x =int(input('Ingresa x : ')) #

    logHallado = log(b,x)
    print('El logaritmo en base ',b, ' de', x,' es : ',round(logHallado,2))
