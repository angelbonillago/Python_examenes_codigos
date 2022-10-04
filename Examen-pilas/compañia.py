if __name__ == '__main__':
    cuotaBaseA = 450
    cuotaBaseB = 150
    porBebeAlcohol = 0.10
    utilizaLentes= 0.05
    padeceEnfermedad =0.05
    masDe40años=0.20
    deLoContrario =0.10
    costoTotal = 0.0

    print('MENU\nElige el tipo de poliza\n1. cobertura amplia (A)\n2. daños a terceros (B)')
    opcion=int(input('opcion -> '))
    print('PLANES\nPersona que conduce por \n1. beber alcohol-10%\n2. utiliza lentes 5% \n3. si padece alguna enfermedad –como deficiencia cardiaca o diabetes-5%\n4. Si tiene más de 40 años- 20%\n5.  De lo contrario sólo 10%. ')
    plan =int(input('opcion -> '))
    if opcion ==1:
        print(' Cobertura amplia (A)')
        if plan ==1:
            costoTotal = cuotaBaseA + (porBebeAlcohol*cuotaBaseA)

        if plan ==2:
            costoTotal = cuotaBaseA + (utilizaLentes*cuotaBaseA)
        if plan ==3:
            costoTotal = cuotaBaseA + (padeceEnfermedad*cuotaBaseA)
            
        if plan ==4:
            costoTotal = cuotaBaseA + (masDe40años*cuotaBaseA)

        if plan ==5:
            costoTotal = cuotaBaseA + (deLoContrario*cuotaBaseA)

        print('MONTO A PAGAR POR LA PALIZA: ',costoTotal)

        

    elif(opcion==2):
        print(' Daños a terceros (B)')
        if plan ==1:
            costoTotal = cuotaBaseB + (porBebeAlcohol*cuotaBaseA)

        if plan ==2:
            costoTotal = cuotaBaseB + (utilizaLentes*cuotaBaseA)
        if plan ==3:
            costoTotal = cuotaBaseB + (padeceEnfermedad*cuotaBaseA)
            
        if plan ==4:
            costoTotal = cuotaBaseB + (masDe40años*cuotaBaseA)

        if plan ==5:
            costoTotal = cuotaBaseB + (deLoContrario*cuotaBaseA)

        print('MONTO A PAGAR POR LA PALIZA: ',costoTotal)
        
    else:
        print('La opcion ingresada no existe')


