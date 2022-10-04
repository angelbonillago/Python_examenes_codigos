class Ejercicio1:
    #Niveles
    malo =0
    regular =0
    bueno =0
    excelente =0
    usuario=14

    niveles = {'malo' : 1, 'regular' : 2, 'bueno': 3,'excelente':4 }
    nivel =[]
    

    #Mostrar cantidad de personas que cayeron en los niveles

    salirProceso = False

    # pedir datos al usuario
    print("\tACEPTACION DE LAS MODIFICACIONES REALIZADAS A LA CAFETERIA DE LA UNIVERSIDAD\n")
    while not salirProceso:

        print("1.Malo\n2. Regular\n3. Bueno\n4. Excelente")

        nivel.append(input(" Ingresa el nivel: "))
      #  valor = inst.validarNum(numCorreos)

        #for i in range(len(nivel)):
         #   print(nivel[i], end='           ')
        #print("\n")..

        if (len(nivel) ==usuario):
          salirProceso=True

    #ver cuantos pertenecen a cada nivel
    for i in range(len(nivel)):
      if nivel[i]=="1":
        malo=malo+1
        #print("entro al malo")
      if (nivel[i]=="2"):
        regular=regular+1
        #print("entro al regular")

      if (nivel[i]=="3"):
        bueno=bueno+1
        #print("entro al bueno")

      if (nivel[i]=="4"):
        excelente=excelente+1
       # print("entro al excelente")
       # myRoundNumber = round(myNumber, 2)

    print("CANTIDAD DE PERSONAS\tNIVEL\tPORCENTAJE%")
    print(malo,"\tMALO\t",round(((malo/usuario)*100),2),"%")
    print(regular,"\tREGULAR\t",round(((regular/usuario)*100),2),"%")
    print(bueno,"\tBUENO\t",round(((bueno/usuario)*100),2),"%")
    print(excelente,"\tEXCELENTE\t",round(((excelente/usuario)*100),2),"%")

if __name__ == '__main__':
    Ejercicio1()
