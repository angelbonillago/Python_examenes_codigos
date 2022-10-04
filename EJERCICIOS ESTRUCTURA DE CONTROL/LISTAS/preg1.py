"""
1. Desarrolle un programa que implemente un vector de 50 elementos con números aleatorios,
y realizar lo siguiente:
✓ Mostrar el vector original.
✓ ¿Cuáles son múltiplos de 2?
✓ mostrar dichos números y cuantos son.

"""
import random
if __name__ == '__main__':
    numerosAleatorios = random.sample(range(1,100),50)
    print("✓ Mostrar el vector original.")
    print(numerosAleatorios)

    contador =0
    vector=[]
    for valor in numerosAleatorios:
        if(valor%2==0):
            contador+=1
            vector.append(valor)
    print('\n✓ mostrar dichos números y cuantos son.')     
    print('\nNumeros multiplos de 2: ',vector)
    print('Cantidad de Numeros multiplos de 2: ',contador)

