import re  # Libreria para poder efectuar las operaciones irregulares


class Metodos:
    def validarNum(self, num):
        try:
            entero = int(num)
            # print("Lo que escribiste es un entero")
            return True
        except:
            # print("Lo que escribiste NO es un entero")+++
            return False

    def validaCorreo(self, correo):
        arrobas = correo.count("@")

        index = correo.find("@")
        punto = correo.find(".")
        longitud = len(correo)
       # print(index)
        #print(punto)
        #print(longitud)

        user = correo[0:index]

        tipo = correo[punto+1:longitud]
        ultimo = correo[longitud-1]
        dominio = correo[index+1:longitud]
        #print("DOMINIO: ", dominio)
        puntoO = dominio.find(".")
        organizacion = dominio[0:puntoO]

        dominioPuntos = dominio.count(".")

       # print(user)
        #print("organizacion: ", organizacion)
       # print(tipo)
        # admite letras,numeros, "-._" y tambien la ñ por varias veces
        userValidacion = '^[a-zA-Z0-9._-ñ]+$'
        orgValidacion = '^[a-zA-Z0-9.]+$'
        #print("num de puntos del: ", dominioPuntos)
        #print("ultimo", ultimo)

        if arrobas == 1 and dominioPuntos <= 2 and ultimo != ".":
            # evaluar el user:
            if re.match(userValidacion, user.lower()):
                #print("user correcto")
                if re.match(orgValidacion, organizacion.lower()):
                    #print("Organizacion correcto")
                    return True
                else:
                    print("Organizacion Incorrecto")
                    return False
            else:
                print("user Incorrecto")
                return False

        else:
            print("Correo Invalido")
            return False


class Registro:
    inst = Metodos()
    salirUsuario = False
    salirProceso = False

    # pedir datos al usuario

    while not salirUsuario:

        numCorreos = (input("Ingresa la cantidad de usuarios a ingresar : "))
        valor = inst.validarNum(numCorreos)

        # print(valor)

        if valor == True:
            salirUsuario = True

    matrizUsuario = []

    i = 0
    while not salirProceso:

        while (i < int(numCorreos)):
            correoValid = False
            nombre = input("Ingresa Nombre : ")
            while not correoValid:
                correo = input("Ingresa Correo : ")
                aux = inst.validaCorreo(correo)
                # print(sla)
                if aux == True:  # se agrega el correo validado
                    matrizUsuario.append([nombre, correo])
                    # print(matrizUsuario)
                    correoValid = True

            i += 1
        salirProceso = True

    print()
    print("\tTabla resulatdos")
    print("Nombre \t\t     RFC")
    print()

    for i in range(len(matrizUsuario)):
        for j in range(len(matrizUsuario[i])):
            print(matrizUsuario[i][j], end='           ')
        print()
    print()


if __name__ == '__main__':
    Registro()
