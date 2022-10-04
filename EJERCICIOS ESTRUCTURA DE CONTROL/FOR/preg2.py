"""
2. Elaborar un programa que calcule la suma de los cuadrados de los n primeros números
naturales: 1 + 22 + 32 +… + n2

"""
if __name__ == '__main__':
    n =int(input('Ingresa n: '))
    suma =0
    for num in range(1,n+1):
        suma +=(num*num)
    print("La suma de los",n," primeros numeros elevado al cuadrado, es: ",suma)
