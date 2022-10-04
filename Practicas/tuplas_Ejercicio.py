"""
Crear un programa que permita crear una tupla con 7 números (incluya: positivos, negativos, ceros, pares, impares).   
Visualice la tupla  y finalmente muestre las cantidades existentes de números positivos, negativos, ceros, pares, impares.

"""
par=0
impar =0
positivo=0
negativo=0
cero=0


tupla = ()

if __name__ == '__main__':
    #pedir 7 numeros: 
    cantidad = 7
    while(cantidad>=0):
        numero = int(input('Ingresa numero : '))
        if numero >0:
            positivo+=1
            #print ("Este número es positivo.")

        if numero<0:

            negativo-=1
            #print ("Este número es Negativo.")
            
        if numero == 0:
            #print ("Este número es par.")
            cero +=1
        elif numero%2 == 0:
            #print ("Este numero es par")
            par+=1

        elif numero%2 != 0:
            #print ("Este numero es impar")
            impar+=1
            
        tupla = tupla + (numero,)
        
        cantidad-=1
   
print (tupla)
print('Cantidad de positivos : ',positivo)
print('Cantidad de Negativos : ',negativo)
print('Cantidad de pares : ',par)
print('Cantidad de impar : ',impar)
print('Cantidad de ceros : ',cero)
