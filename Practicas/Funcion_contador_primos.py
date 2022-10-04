
"""
1. Escriba una función conteo(n) que entregue la cantidad de divisores enteros positivos 
que tiene un número entero dado n. Escriba un programa de prueba que use la función 
escrita para encontrar cual número entre 1 y 100 tiene más divisores enteros.
"""

#Modificado por BONILLA GONZALEZ
#CODIGO : 162340B
#---------------------------------------

def dameConteo(n):
    contador = 0
    for i in range(1, n+1):
        if n % i == 0:
            print(i)

if __name__ == '__main__':

    n= int(input('Escriba un numero entre 1 y 100 para saber sus divisores positivos : '))
    dameConteo(n)
