"""
11. Elaborar un programa que convierta un número entero (de cuatro dígitos) en otro
número entero, pero con las cifras que lo forman escritas al revés. Ejemplo: convertir
el número entero 1842 en el 2481.

"""
if __name__ == '__main__':

    n =int(input('Ingresa un numero de 4 digitos: '))
    invertido=0
    if n>999 and n<10000:
        tamano=len(str(n))
        for i in range(tamano):
            b=n%10
            n=n//10
            invertido=invertido*10+b
        print('Numero invertido: ',invertido)

    else: 
        print('Numero no valido!')

