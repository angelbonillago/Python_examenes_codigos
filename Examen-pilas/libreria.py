if __name__ == '__main__':
    monto =0
    descuento1=0.20
    descuento2=0.15
    descuento2=0.18
    venta = int(input(('INGRESA IMPORTE DE COMPRA : ')))
    numero = int(input(('INGRESA EL NUMERO QUE SACASTE : ')))
    if(numero==1):
        monto = venta- (venta*descuento1)

    elif(numero==2):
        monto = venta- (venta*descuento2)

    elif(numero==3):
        monto = venta- (venta*descuento3)
    else:
        print('Sólo hay 3 posibilidades de números en la caja. ')
    

    print('EL IMPORTE A PAGAR ES : ',monto)