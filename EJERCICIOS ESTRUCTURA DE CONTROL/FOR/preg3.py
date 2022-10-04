"""
3. Elaborar un programa que calcule la suma de los números enteros comprendidos entre n
hasta m (tener en cuenta m>n)

"""

if __name__ == '__main__':

    n =int(input('Ingresa n: '))
    m =int(input('Ingresa m: '))

    if m>n:
        print("\tSUMA DE NUMEROS comprendidos entre n hasta m")
        suma =0
        for num in range(n+1,m):
            suma +=num
        print("La suma de los números enteros comprendidos entre n hasta m, es: ",suma)

    else: 
        print("m debe ser mayor que n...")

