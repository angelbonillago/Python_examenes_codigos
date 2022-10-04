"""
9. Elaborar un programa que calcule el n-ésimo término de la sucesión de los números
de Fibonacci: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...

"""
if __name__ == '__main__':

    n =int(input('Ingresa el n-simo termmino para hallar en la serie Fibonacci : '))
    if(n>0):
        print("SERIE OBTENIDA")
        n1=1
        n2=1
        if n==1:
            print('1')
        elif n==2:
            print('1','1')
        else:
            print('1')
            print(n1)
            print(n2)
            for i in range(n-3):
                total = n1 + n2
                n2=n1
                n1= total
                print(total) 
    else:

        print("no se ingresa numeros negativos!")