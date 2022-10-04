"""4. La temperatura de un horno puede variar desde 0 hasta 100 grados centígrados y se clasifica
de acuerdo a lo siguiente:
MUY ALTA: si su valor esta entre 90oC y 100oC
ALTA: si su valor esta entre 80oC y 89oC
NORMAL: si su valor esta entre 40oC y 79oC
BAJA: si su valor esta entre 0oC y 39oC
✓ Escribir un programa que permita ingresar la temperatura del horno e imprima su
clasificación

"""

if __name__ == '__main__':
    temperatura =int(input('Ingresa la temperatura del horno: '))
   # print(temperatura)

    if(temperatura>=90 and temperatura<=100):
        print("MUY ALTA")

    elif(temperatura>=80 and temperatura<=89):
        print("ALTA")

    elif(temperatura>=40 and temperatura<=79):
        print("NORMAL")
    else:
        print("BAJA")