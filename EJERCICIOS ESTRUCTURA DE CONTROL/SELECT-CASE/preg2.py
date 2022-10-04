"""
2. Escribir un programa que permita ingresar 3 notas de un estudiante e imprima cuál es su
rendimiento. El rendimiento de un estudiante se clasifica de acuerdo a lo siguiente:
BUENO: si su promedio esta entre 16 y 20
REGULAR: si su promedio esta entre 11 y 15
DEFICIENTE: si su promedio esta entre 6 y 10
PESIMO: si su promedio esta entre 0 y 5

"""
if __name__ == '__main__':
    n1 =int(input('Ingresa su nota 1: '))
    n2 =int(input('Ingresa su nota 2: '))
    n3 =int(input('Ingresa su nota 3: '))
    promedio = (n1+n2+n3)/3
   # print(promedio)
    if(promedio>=16 and promedio<=20):
        print("RENDIEMIENTO BUENO")

    elif(promedio>=11 and promedio<=15):
        print("RENDIEMIENTO REGULAR")

    elif(promedio>=6 and promedio<=10):
        print("RENDIEMIENTO DEFICIENTE")
    else:
        print("RENDIEMIENTO PESIMO")
