class Ejercicio2:
    #18:37

    particular =0
    autobus =0
    motobicicleta =0
    camion_cuatro_ruedas =0
    caso_contrario =0
    tipo = []
    ide = 0
    tipos = {'particular' : 1.75, 'autobus' : 3.50, 'motobicicleta': 1.00,'camion_cuatro_ruedas':5.00,'caso_contrario': 150.00}


    salirProceso = False
    # pedir datos al usuario
    print("\tCOBRO DE PEAJE DE UNA AUTOPISTA\n")
    print("\tTIPO DE VEHICULO\tPEAJE")
    print("1.Particular\tB.1.75\n2. Autobus\tB.3.50\n3. Motobicicleta\tB.1.00\n4. Camion de cuatro ruedas\tB.5.00\n5. Caso contrarioVEHICULO NO AUTORIZADO-MULTA\tB.150.00")

    while not salirProceso:

        tipo.append(input(" Selecciona el tipo de vehiculo: "))

        if(tipo[ide]=="1"):
            particular=particular+1
            print("Peaje a pagar :",tipos['particular'])
            print("1")

        if(tipo[ide]=="2"):
            autobus=autobus+1
            print("Peaje a pagar :",tipos['autobus'])
            print("2")
        if(tipo[ide]=="3"):
            motobicicleta=motobicicleta+1
            print("Peaje a pagar :",tipos['motobicicleta'])
            print("3")
        if(tipo[ide]=="4"):
            camion_cuatro_ruedas=camion_cuatro_ruedas+1
            print("Peaje a pagar :",tipos['camion_cuatro_ruedas'])
            print("4")
        if(tipo[ide]=="5"):
            caso_contrario=caso_contrario+1
            print("Peaje a pagar :",tipos['caso_contrario'])
            print("5")

        ide = ide+1

        if ide == 5:

            salirProceso=True

    #calculos
    totalCarros = autobus+caso_contrario+camion_cuatro_ruedas+motobicicleta+particular

    print("CANTIDAD DE VEHICULOS\tTIPO\t\tMONTO RECAUDADO")
    print(particular,"\t\t\tPARTICULAR\t\t",1.75*particular)
    print(autobus,"\t\t\tAUTOBUS\t\t",3.50*autobus)
    print(motobicicleta,"\t\t\tAUTOBUS\t\t",1.00*motobicicleta)
    print(camion_cuatro_ruedas,"\t\t\tAUTOBUS\t\t",5.00*camion_cuatro_ruedas)
    print(caso_contrario,"\t\t\tAUTOBUS\t\t",150.00*caso_contrario)


if __name__ == '__main__':
    Ejercicio2()
