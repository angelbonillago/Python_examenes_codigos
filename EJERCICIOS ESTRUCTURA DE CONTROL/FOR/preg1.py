"""1. Elaborar un programa que calcule la suma de los n primeros 
números naturales."""

if __name__ == '__main__':
    n =int(input('Ingresa n: '))
    suma =0
    for num in range(1,n+1):
        suma +=num
    print("La suma de los",n," primeros numeros es: ",suma)
