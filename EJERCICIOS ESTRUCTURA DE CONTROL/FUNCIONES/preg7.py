"""
7. Diseña una función que devuelva la solución de la ecuación lineal ax + b = 0 dados a y b. Si
la ecuación tiene infinitas soluciones o no tiene solución alguna, la función lo detectará y
devolverá el valor de None.
"""

def ecuación_lineal(a,b):
    if a != 0:
        x = (-b/a)
        print('Solucion a la ecuacion ',a,'x','+',b,'=0 es :  x=%4.2f  ' %(x))
    else: 
        if a==0 and b!=0:
            print ('None') #La ecuacion no tiene solucion
        else:
            print('None')#La ecuacion tiene infinitas soluciones.

if __name__ == '__main__':
    print('Ecuación lineal ax + b = 0 ')
    a =int(input('Ingresa a : ')) 
    b =int(input('Ingresa b : ')) 

    solEcuaLineal=ecuación_lineal(a,b)
