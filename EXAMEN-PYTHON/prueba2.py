lista = ['5', '+', '(', '(', '15', '-', '6', '*', '3', ')', '+', '(', '16', '/', '2', '^', '3', ')', ')', '*', '2']
print(lista)
expresion =[]
cadena = []
signos = list('+(/*-)^')
pesos_cadena = {')' : -1, '(' : 0, '+': 1,'-':1,'*':2,'/':2,'^':3}
pesos_expresion = {')' : -1, '(' : 5, '+': 1,'-':1,'*':2,'/':2,'^':4}
numero =''
valorCadena=''
signo=''
valorExpresion=''
pesoExpresion=0
pesoCadena=0
count=0
ayuda = 0
valorderecorrido=''

for i in range(len(lista)):
    if(not(lista[i] in signos)):
        #agrego el numero a la expresion
        numero = lista[i]
        expresion.append(numero)

    else:
        if(len(cadena)==0):
            if(lista[i] != ')'):
                valorCadena=lista[i]
                cadena.append(valorCadena)
        else:
            if(lista[i]==')'):
                #recorro la cadena para encontrar el ultimo '('
                count=len(cadena)
                ayuda = count-1
                print("tamaño de la cadena : ",count)
                
                for x in range(count):
                    valorderecorrido=cadena[ayuda]
                    if(valorderecorrido=='('): 
                        #no agregues nada
                        
                        x=count
                    else:
                        print("agregue a expresione le valor : ",valorderecorrido)
                        expresion.append(valorderecorrido)
                        print("NUEVA expresion : ",expresion)
                        ayuda=ayuda-1

                #eliminar expresiones
                print('cadena antes de eliminarse valores',cadena)
                count=len(cadena)
                print("tamaño de la cadena antes de eliminar : ",count)
                ayuda = count-1
                contadorParentesis=0

                #cantidad a eliminar
                indice_ =0
                for j in range(len(cadena)):
                    if(cadena[j]=='('):
                        indice=j

                for x in range(indice,count):

                    valorderecorrido=cadena[ayuda]
                    print('Valor a eliminar :',valorderecorrido)
                    cadena.pop(ayuda)
                    print('Nueva cadena :',cadena)                    
                    ayuda=ayuda-1

 
            else:
                signo = lista[i]
                pesoExpresion = pesos_expresion[signo]
                pesoCadena= pesos_cadena[valorCadena]
                if(pesoExpresion>=pesoCadena):
                    valorCadena=signo
                    cadena.append(signo)
                    print("Agregue a la cadena", signo)
                else:

                    valorExpresion=signo
                    expresion.append(signo)
                    print("Agregue a la expresion", signo)


print("Expresion : ",expresion)
print("cadena", cadena)

