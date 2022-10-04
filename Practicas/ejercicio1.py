# Introducir usuario
salida = False

while (not salida):

    nombre = input("Dame tu nombre de usuario: ")
    numLetras = len(nombre)
    print(numLetras)

    if numLetras > 5 and numLetras < 13:
        salida = True
        retorno = True

    else:
        print("El nombre deberia tener de 6 a 12 caracteres")
