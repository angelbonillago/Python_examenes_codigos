numVentas =3
numVendedores=0
sueldoBase=0
extra =0

if __name__ == '__main__':
    numVentas =3
    numVendedores=0
    sueldoBase=0
    extra =0
    salir =False
    index =1
    i=1
    sueldoBase =100
    
    diccionarioVendedores={}
    listaVendedores=[]
    datos=[]
    aux=()
    ident =0
    totalVentas=0
    listaTotalVentas=[]
    numVendedores = int(input('Ingresa cantidad de vendedores : '))
    comisiones=[]
    while numVendedores>0:
        
        print('vendedor : ',i)
        
        venta1 =int(input('venta 1: '))
        venta2 =int(input('venta 2 : '))
        venta3 =int(input('venta 3: '))
        totalVentas=venta1+venta2+venta3
        listaTotalVentas.append(totalVentas)
        datos=[venta1,venta2,venta3]
        aux = (index,datos)
        listaVendedores.append(aux)
        diccionarioVendedores=dict(listaVendedores)
        index +=1    
        print('vendedor : ',diccionarioVendedores)
        i+=1
        comision=sueldoBase+ (0.1*totalVentas)
        comisiones.append(comision)
        numVendedores -=1
        totalVentas=0
        ident+=1
        
    vendor=1
    #print(diccionarioVendedores[1][0])
    for ox in listaTotalVentas:
        print('TOTAL VENTA DE VENDEDOR  ',vendor,' : ',ox)
        vendor+=1
    vendor=1
    for ox in comisiones:
        print('COMISION DEL VENDEDOR  ',vendor,' : ',ox)
        vendor+=1






