"""
Escriba un programa de prueba que use la función primo y encuentre dos números 
enteros aleatorios menores que 100 tales que su suma sea también un número primo.
"""

#Modificado por BONILLA GONZALEZ
#CODIGO : 162340B
#---------------------------------------
from random import *
def primo(n):

    c=0
    for i in range(1,n+1):
        if n%i==0:
            c=c+1
    if c>2:
        return False
    else:
        return True
def efectuar():
    encontro= False
    while not encontro:
        aleatorioUno = randint(1,100) #ramdom del 1 al 100
        aleatorioDos=randint(1,100)
        suma = aleatorioUno+aleatorioDos
        if(primo(suma)):
            encontro =True
    print('Los numeros son',aleatorioUno,' y ',aleatorioDos,' Sumandolos, da el numero primo : ',suma)
if __name__ == '__main__':
    efectuar()


