
salirProceso = False
examingreso = {}
numEstudiantes = 0
opcion = ''

while not salirProceso:
    print("\tMENU\n")
    print("i) Registrar estudiantes")
    print("ii) Consulta de estudiante con mayor puntaje")
    print("iii) Consulta de estudiante con menor puntaje")
    print("iv) Consulta de estudiante a través de la identificacion ")
    print("v) Puntaje promedio obtenido")
    print("vi) Consulta de estudiantes que aprobaron el examen")
    print("vii) Salir")
    opcion = (input("Opcion ->  "))

    if (opcion == 'i'):
        # registra estudiantes
        clave = int((input("Ingresa tu identificacion: ")))
        name = ((input("Ingresa tu nombre: ")))
        score = int((input("Ingresa tu puntaje: ")))
        examingreso.update({clave: [name, score]})
        numEstudiantes = numEstudiantes+1
        print("Diccionario  - ", examingreso)

    if (opcion == 'ii'):
        mayor = 0
        aux = 0
        mayor = examingreso[clave][1]
        index = 0
        #print("nota tomada para prueba : ",mayor)

        for iden in examingreso:
            aux = examingreso[iden][1]
         #   print("nota tomada : ",mayor)
            if(mayor <= aux):
                mayor = aux
                index = iden
        print("IDENTIFICACION\tNOMBRE\tPUNTAJE")
        print(index, "\t\t", examingreso[index]
              [0], "    ", examingreso[index][1])

    if (opcion == 'iii'):
        mayor = 0
        aux = 0
        menor = examingreso[clave][1]
        index = 0
        print("nota menor para prueba : ", menor)

        for iden in examingreso:
            aux = examingreso[iden][1]
            if(menor >= aux):
                menor = aux
                index = iden

        print("IDENTIFICACION\tNOMBRE\tPUNTAJE")
        print(index, "\t\t", examingreso[index]
              [0], "    ", examingreso[index][1])

    if (opcion == 'iv'):
        encontrado = False
        indentificador = 0

        while not encontrado:
            indentificador = int((input("Ingresa tu identificacion: ")))
            valor = []
            try:
                valor = examingreso[indentificador]
            except:
                print("No existe el identificador")
                continue
            if (valor != ''):
                print("IDENTIFICACION\tNOMBRE\tPUNTAJE")
                print(indentificador, "\t\t",
                      examingreso[indentificador][0], "    ", examingreso[indentificador][1])
                encontrado = True

    if (opcion == 'v'):
        aux = 0
        promedio = 0

        for iden in examingreso:
            aux = examingreso[iden][1]
            promedio = promedio + aux

        print("Promedio obtenido : ", round((promedio / numEstudiantes), 2))

    if (opcion == 'vi'):
        aux = 0
        print("IDENTIFICACION\tNOMBRE\tPUNTAJE")
        for iden in examingreso:
            aux = examingreso[iden][1]
            if aux >= 80:
                print(iden, "\t\t", examingreso[iden]
                      [0], "    ", examingreso[iden][1])

    if (opcion == 'vii'):
        print("SALIR DEL PROGRAMA")
        salirProceso = True


if __name__ == '__main__':
    pass
