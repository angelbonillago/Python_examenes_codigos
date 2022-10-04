"""

10. Elaborar un programa que calcule la exponencial de un número real a
La serie se puede aproximar con la siguiente formula:

"""
if __name__ == '__main__':
    n =int(input('Ingresa a para calcular la exponencial : '))
    total=0.0
    numerador=0
    denominador=2
    aux=0.0
    
    s=3
    subtotal=0.0
    if n==1:
        print(n)
    if n==2:
        print("1 + ",n)
        print(3)
    if n>2:
        #print("1 + ",n)
        for i in range(n-2):
            fact=1
            elevado = i+2
            numerador = n**elevado               
            for d in range(1,s):
                fact = fact*d
            denominador=fact
            #fact+=1
            s=s+1
            aux=numerador/denominador
            total= total+aux
        subtotal=total +1+n
        print("SUMA : ",subtotal)    

            



  

