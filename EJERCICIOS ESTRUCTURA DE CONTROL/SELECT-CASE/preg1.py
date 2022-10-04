"""
Escribir un programa que calcule el Índice de Masa Corporal de una persona
(IMC = peso [kg] / (altura [cm])²) e indique el estado en el que se encuentra esa persona en
función del valor de IMC: (revisar http://www.calculoimc.com/)

ÍNDICE MASA CORPORAL CLASIFICACIÓN
< 16.00 Infrapeso: Delgadez Severa
16.00 - 16.99 Infrapeso: Delgadez moderada
17.00 - 18.49 Infrapeso: Delgadez aceptable
18.50 - 24.99 Peso Normal
25.00 - 29.99 Sobrepeso
30.00 - 34.99 Obeso: Tipo I
35.00 - 40.00 Obeso: Tipo II
> 40.00 Obeso: Tipo III


Es importante que recuerde introducir su altura en centímetros en lugar de metros en la casilla de altura. De esta
forma, si mide 1.70 metros, deberá escribir 170 en el cuadro de altura.
"""
if __name__ == '__main__':
    altura =float(input('Ingresa su altura en cm : '))
    peso =float(input('Ingresa su peso en kg : '))
    #Hallar IMC

    imc = 0.0
    imc = (peso/pow(altura,2)) *10000
    #print(imc)

    if imc<16.00:
        print("Infrapeso: Delgadez Severa")
    elif(imc>=16 and imc <=16.99):
        print("Infrapeso: Delgadez moderada")  
    elif(imc>=17 and imc <=18.49):
        print("Infrapeso: Delgadez aceptable")
    elif(imc>=18.5 and imc <=24.99):
        print("Peso Normal")
    elif(imc>=25 and imc <=29.99):
        print("Sobrepeso")
    elif(imc>=30 and imc <=34.99):
        print("Obeso: Tipo I")
    elif(imc>=35 and imc <=40):
        print("Obeso: Tipo II")
    else:
        print("Obeso: Tipo III")                 