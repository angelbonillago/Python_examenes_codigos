salirProceso = False
medicamentos = {}
opcion = ''

while not salirProceso:
    print("\n\tMENU")
    print("1) Registrar medicamentos en el inventario")
    print("2) Consulta medicamentos de un laboratorio X(Listar nombre y cantidad)")
    print("3) Consultar los laboratorios que proveen un medicamento X")
    print("4) Consultar medicamentos cuya cantidad esta por debajo de una cantidad X ")
    print("5) Salir")
    opcion = (input("Opcion ->  "))

    if (opcion == '1'):
        # registra estudiantes
        clave = int((input("Ingresa clave del medicamento : ")))
        name = ((input("Nombre : ")))
        laboratorio = ((input("Laboratorio : ")))
        cantidad = int((input("Cantidad: ")))
        medicamentos.update({clave: [name,laboratorio,cantidad]})
        print("Medicamentos  - ", medicamentos)

    if (opcion == '4'):
        mayor = 0
        cantidadX =0
        aux = 0
        index = 0
        cantidadIndices =[]
        cantidadX = int((input("Ingresa cantidad : ")))

        for iden in medicamentos:
            aux = medicamentos[iden][2]
            if(cantidadX > aux):
                #menor = aux
                cantidadIndices.append(iden)
        print("Clave\tNombre\tLaboratorio\tCantidad")
        for iden in cantidadIndices:

            print(iden, "        ", medicamentos[iden][0], "        ", medicamentos[iden][1],"        ",medicamentos[iden][2])


    if (opcion == '2'):
        indentificador = 0
        listaDeIndices =[]
        #contadorLab =''
        contadorLab =0
        indentificador = (input("Ingresa Laboratorio : "))

        for iden in medicamentos:
            aux = medicamentos[iden][1]
            if (aux==indentificador):
                contadorLab=contadorLab+1 #Si hay varios lab
                listaDeIndices.append(iden)
        print("Nombre\tCantidad")
                
        for ident in listaDeIndices:
            print(medicamentos[ident][0], "    ", medicamentos[ident][2])


    if (opcion == '3'):
        indentificador = ''
        listaDeIndices =[]
        contadorLab =0
        indentificador = (input("Ingresa Medicamento : "))

        for iden in medicamentos:
            aux = medicamentos[iden][0]
            if (aux==indentificador):
                contadorLab=contadorLab+1 #Si hay varios lab
                listaDeIndices.append(iden)
        print("Laboratorio")
                
        for ident in listaDeIndices:
            print(medicamentos[ident][1])

    if (opcion == '5'):
        print("SALIR DEL PROGRAMA")
        salirProceso = True


if __name__ == '__main__':
    pass
