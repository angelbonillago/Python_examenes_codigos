"""
4. Elaborar un programa que calcular el factorial de un número dado (El programa solo
admite datos entre 3 y 8)


"""

if __name__ == '__main__':
    n =int(input('Ingresa un numero entre 3 y 8 para calcular su factorial : '))
    if(n>2 and n<9):
        factorial=1
        for i in range(1,n+1):
            factorial=factorial*i
        print("el factorial de",n," es: ",factorial)
    else:
        print("Debe ingresar numeros en el rango indicado!")
