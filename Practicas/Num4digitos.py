def listaDigitos(numero):
    lista=[]
    contador = 0
    while numero>=0:
        aux = numero%10
        numero = numero/10
        lista[contador] =aux
        contador=+contador
    listaInvertida = lista[::-1]
    for valores in listaInvertida:
        print(valores[listaInvertida]+"\n")





salir = False
while(not salir):
    num = int(input("Ingresa un numero de 4 digitos: "))
    #validar si tiene 4 digitos
    cant = num.count()
    if num>0:
        while(num>0):

            if cant ==4:
                listaDigitos(num)
                salir = True
            else:
        print("Ingresa un numero de 4 digitos!!")







