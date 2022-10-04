"""
8. Elaborar un programa que calcule la suma de los números múltiplos de 3 y 7 a partir del
número 9 y finaliza en el número 45, no deben incluirse en la suma los números
comprendidos entre 21 y 27

"""
if __name__ == '__main__':
    suma=0
    for i in range(9,46):
        if(i%3==0 or i%7==0):
            if(i<21 or i>27):
                suma=suma+i
                print(i)            
    print("La suma es  : ",suma)