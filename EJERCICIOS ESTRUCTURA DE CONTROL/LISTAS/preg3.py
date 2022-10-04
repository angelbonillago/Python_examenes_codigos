"""
3. Desarrolle un programa que implemente un vector de 50 elementos con números aleatorios,
y determinar:
✓ ¿Cuáles son múltiplos de 3 y 5?
✓ mostrar dichos números y cuantos son.

"""

import random
if __name__ == '__main__':
    numerosAleatorios = random.sample(range(1,100),50) #50 aleatorios entre 1 y 100
    print("✓ Mostrar el vector original.")
    #print(numerosAleatorios)
    print('✓ ¿Cuáles son múltiplos de 3 y 5?\n')
    contador =0
    vector=[]
    for valor in numerosAleatorios:
        if(valor%15==0):
            contador+=1
            vector.append(valor)
    print('Numeros múltiplos de 3 y 5: ',vector)
    print('Cantidad de Numeros múltiplos de 3 y 5 : ',contador)    