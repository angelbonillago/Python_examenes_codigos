"""
12. Escribir un programa que permita convertir de número decimal a binario, el número
debe ser generado aleatoriamente.

"""

import random

if __name__ == '__main__':
    n = random.randint(1,100) #numero de 2 cifras
    print("NUMERO ALEATORIO GENERADO : ",n)
    binario = ""
    for salir in range(500):
        #Conversion a binario

        residuo = int(n % 2)
        n = int(n / 2)
        binario = str(residuo) + binario        
        if n>0:
            pass
        else:
            break


    print("El numero convertido a binario es :  ",binario)



