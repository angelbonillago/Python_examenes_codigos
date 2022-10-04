class Metodos:

    def __init__(self):

        # La pila vacía se representa con una lista vacía
        self.simbolos = []
        self.indices = []
        self.indiceMayores = []
        self.newLista = []

    def numMayorAnueve(self, lista):
        # simbolos=[]
        # indices=[]

        for i in range(len(lista)):
            if(lista[i] == '+'):
                self.simbolos.append('+')
                self.indices.append(i)
            if(lista[i] == '-'):

                self.simbolos.append('-')
                self.indices.append(i)

            if(lista[i] == '/'):
                self.simbolos.append('/')
                self.indices.append(i)

            if(lista[i] == '*'):

                self.simbolos.append('*')
                self.indices.append(i)

            if(lista[i] == '^'):

                self.simbolos.append('^')
                self.indices.append(i)

            if(lista[i] == '('):
                self.simbolos.append('(')
                self.indices.append(i)

            if(lista[i] == ')'):
                self.simbolos.append(')')
                self.indices.append(i)

        # print(self.indices)
        valor = len(self.indices)
        # print(valor)

        for i in range(valor-1):
            posicion = self.indices[i]
            posicionS = self.indices[i+1]
            # print(i)
            if((posicion+1 == posicionS) or (posicion+2 == posicionS)):
                pass

                # print("si creo")
            else:

                # self.indiceMayores.append(i+1)
                # self.indiceMayores.append(i+2)
                self.indiceMayores.append(posicion+1)
                self.indiceMayores.append(posicion+2)
                # print("no creo")

        # print("indices mayores ", self.indiceMayores)
        numMayores = len(self.indiceMayores)
        if(numMayores > 0):
            aux = 0
            cant = numMayores/2
            # print("cantidad de ",cant)
            indice = self.indiceMayores[aux]
            y = 0

            while(y < (len(lista))):
                if(y == self.indiceMayores[aux]):
                    # print("entra al if despues del cant...")
                    nuevo = lista[y]+lista[y+1]
                    self.newLista.append(nuevo)
                    y = y+2
                    cant = cant-1
                    if(cant > 0):
                        aux = aux+2
                    # print("Nuevo" ,nuevo)
                    # print("i" ,y)

                else:
                    # print("i a meter a la matriz ",y)
                    self.newLista.append(lista[y])
                    # print("agrego1")
                    y = y+1
            return True
        else:
            return False

    def dameNewLista(self):
        return print("Nueva lista ", self.newLista)

    def dameOperaciones(self, lista):
        if(self.numMayorAnueve(lista)):
            self.operaciones(self.newLista)
        else:
            self.operaciones(self.lista)

    def operaciones(self, lista):
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
                        #print("tamaño de la cadena : ",count)
                        
                        for x in range(count):
                            valorderecorrido=cadena[ayuda]
                            if(valorderecorrido=='('): 
                                #no agregues nada
                                
                                x=count
                            else:
                                #print("agregue a expresione le valor : ",valorderecorrido)
                                expresion.append(valorderecorrido)
                                #print("NUEVA expresion : ",expresion)
                                ayuda=ayuda-1

                        #eliminar expresiones
                        #print('cadena antes de eliminarse valores',cadena)
                        count=len(cadena)
                        #print("tamaño de la cadena antes de eliminar : ",count)
                        ayuda = count-1
                        contadorParentesis=0

                        #cantidad a eliminar
                        indice_ =0
                        for j in range(len(cadena)):
                            if(cadena[j]=='('):
                                indice=j

                        for x in range(indice,count):

                            valorderecorrido=cadena[ayuda]
                            #print('Valor a eliminar :',valorderecorrido)
                            cadena.pop(ayuda)
                            #print('Nueva cadena :',cadena)                    
                            ayuda=ayuda-1

        
                    else:
                        signo = lista[i]
                        pesoExpresion = pesos_expresion[signo]
                        pesoCadena= pesos_cadena[valorCadena]
                        if(pesoExpresion>=pesoCadena):
                            valorCadena=signo
                            cadena.append(signo)
                            #print("Agregue a la cadena", signo)
                        else:

                            valorExpresion=signo
                            expresion.append(signo)
                            #print("Agregue a la expresion", signo)


        #print("Expresion : ",expresion)
        cadena=''
        for i in range(len(expresion)):
            cadena = cadena+expresion[i]
        print(cadena)



            

        #print("cadena", cadena)
                


if __name__ == '__main__':
    p = Metodos()
    eistring = input('Ingrese Operacion sin espacios: ')
    EI = list(eistring.upper())
    print(EI)
    #print("tamaño de lista : ", len(EI))
    # print(p.numMayorAnueve(EI))
    # p.dameNewLista()
    p.dameOperaciones(EI)
