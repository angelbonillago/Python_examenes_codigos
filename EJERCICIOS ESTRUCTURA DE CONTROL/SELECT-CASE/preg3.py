"""
3. Si se compra 100 unidades o más de un artículo se obtiene un descuento del 40%, si se
compra desde 26 hasta 99 el descuento es de 20%, si se compra desde 10 hasta 25 el
descuento es del 12%. Para cantidades menores no hay descuento.
✓ Escribir un programa que permita ingresar el costo unitario del articulo y la cantidad de
unidades compradas e imprima el monto a pagar.

"""
if __name__ == '__main__':
    precioUnidad =int(input('Ingresa costo unitario del articulo : '))
    unidades =int(input('Ingresa unidades compradas : '))
    precioTotal = 0.0
    if(unidades>=100):
        precioTotal= precioUnidad-(0.4*precioUnidad)
        precioTotal = precioTotal *unidades

    elif(unidades>=26 and unidades<=99):
        precioTotal= precioUnidad-(0.2*precioUnidad)
        precioTotal = precioTotal *unidades

    elif(unidades>=10 and unidades<=25):
        precioTotal= precioUnidad-(0.12*precioUnidad)
        precioTotal = precioTotal *unidades
    else:
        print("Para cantidades menores no hay descuento")
    
    print("El monto a pagar es :",precioTotal)