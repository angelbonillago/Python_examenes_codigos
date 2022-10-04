"""
2. Desarrolle un programa que implemente un vector de 60 elementos con números aleatorios
y permita evaluar lo siguiente:
✓ Cuántos elementos existen entre 50 y 75, ambos inclusive, se deben de visualizar los
números y también contarlos.
✓ Cuántos elementos son mayores a 80, se deben de visualizar los números y también
contarlos.
✓ Cuántos elementos son menores a 30, se deben de visualizar los números y también
contarlos.
"""

import random
if __name__ == '__main__':

    numerosAleatorios = random.sample(range(1,100),60) #Vector de 60 elementos con números aleatorios
    print('✓ Cuántos elementos existen entre 50 y 75, ambos inclusive, se deben de visualizar los números y también contarlos.')
    contador =0
    vector=[]
    for valor in numerosAleatorios:
        if(valor>49 and valor<76):
            contador+=1
            vector.append(valor)
    print('Numeros entre 50 y 75: ',vector)
    print('Cantidad de Numeros entre 50 y 75 : ',contador)

    print('\n✓ Cuántos elementos son mayores a 80, se deben de visualizar los números y también contarlos.')
    vector2=[]
    contador2=0

    for valor2 in numerosAleatorios:
        if(valor2>80):
            contador2+=1
            vector2.append(valor)
    
    print('Numeros mayores a 80 : ',vector2)
    print('Cantidad de Numeros  mayores a 80  : ',contador2)

    print('\n✓ Cuántos elementos son menores a 30, se deben de visualizar los números y también contarlos.')
    vector3=[]
    contador3=0

    for valor3 in numerosAleatorios:
        if(valor3<30):
            contador3+=1
            vector3.append(valor)

    print('Numeros menores a 30 : ',vector3)
    print('Cantidad de Numeros menores a 30  : ',contador3)