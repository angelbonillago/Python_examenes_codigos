"""
5. Realice un programa que determine el pago a realizar por la entrada a un espectáculo
donde se comprar “n” entradas, lo cual lo va designar la máquina, donde el costo de dos entradas 
se le descuenta el 10%, al de 3 entradas el 15% y a la compra de 4 tickets o más
se le descuenta el 20%.

"""

if __name__ == '__main__':
    numEntrada =int(input('numero de entradas : '))
    costo=20
    pago =0.0
    if numEntrada==2:
        pago =costo -(0.1*costo)
    elif numEntrada ==3:
        pago =costo -(0.15*costo)
    elif(numEntrada >=4):
        pago =costo -(0.2*costo)

    print("El pago a cancelar por las ",numEntrada, " es : ",pago)


