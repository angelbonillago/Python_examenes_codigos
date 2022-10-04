import random

def intentos(codigo):
    #ingresaNumero = input("Ingresa el numero a adivinar:")
    numIntento = 0
    salir = False
    numIntento=numIntento+1
    #ingresaNumeroConvertido = int(ingresaNumero)
    #codigoConvertido = int(codigo)

    while (not salir):
        ingresaNumero = input("Ingresa el numero a adivinar:")
        ingresaNumeroConvertido = int(ingresaNumero)
        codigoConvertido = int(codigo)

        if codigo==ingresaNumero:
            print("FELICIDADES, ERES UN WIN PARA ADIVINAR\nNumero de intentos: ",numIntento)
            salir =True
        if (ingresaNumeroConvertido>codigoConvertido):
            print("ingresa un numero menor")
            numIntento=numIntento+1
        if(ingresaNumeroConvertido<codigoConvertido):
            print("ingresa un numero mayor")
            numIntento=numIntento+1



continuar = 1

while (continuar == 1):

    print("Bienvenido a YouMasterMind")
    dificultad = int(input("Elije la dificultad del juego:\n<1=Easy>\n<2=Hard>\n<3=Ningtmare>\n"))
    #print(opcion)

    if dificultad==1:
        cantDigito = 3
    elif dificultad ==2:
        cantDigito=4
    else:
        cantDigito=5

    print(cantDigito)
    digitos = ('0','1','2','3','4','5','6','7','8','9')    
    codigo =''
    ayuda=[]
    agrega =0
    cuentaRe=0
    salirDeEsto=0;

    #for x in range(cantDigito):

    while(cantDigito>cuentaRe):

        elegida= random.choice(digitos)
        print(elegida)

        if ((elegida =='0') and (codigo=='')):
            salirDeEsto =3
        else:
            salirDeEsto=2

        if(salirDeEsto==2):
          
            if codigo =='':
                codigo= codigo+elegida
                ayuda.append(elegida)
                cuentaRe=cuentaRe+1
            else:
                con=cuentaRe
                for y in range(0,len(ayuda)):
                    if (ayuda[y] == elegida):
                        noAgrega=2
                    else:
                        agrega=1
                        

                if (noAgrega==2):
                    cuentaRe=con

                elif(agrega ==1):
                    codigo= codigo+elegida
                    ayuda.append(elegida)
                    cuentaRe=cuentaRe+1
            noAgrega=0
            agrega=0


        else:
            pass
            
        
    print(codigo)
   




    print("\tLlego el momento de que adivines el numero\n\t\tREGLAS\n1. El numero tiene",cantDigito," digitos\n2. Los digitos no deben ser repetidos...Buena suerte!")
    
    intentos(codigo)
        

    salida = int(input("Ingresa 2 para salir del programa\nPresiona 1 para continuar:"))
    continuar=salida
    if continuar==2:
        print("GRACIAS POR PARTICIPAR")




                



        


