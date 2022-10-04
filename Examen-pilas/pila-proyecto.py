class Pila: #clase Pila, que contendra los metodos Insertar,mostrar,eliminar 

    def __init__(self):
        """ Se creara una pila vacía. """
        
        self.items = []# La pila vacía se representa con una lista vacía
        self.CIMA = 0 #Inicializamos la CIMA de la cola en 0

    def insertar(self, x):
        if (self.cantElementos() < 6): #Permitiremos que solo se puedan agregar 6 elementos en memoria a la Cola
            self.items.append(x)
            self.CIMA = self.CIMA+1 #cuando se agregue un nuevo valor, la CIMA aumentara de uno en uno
        else:
            print("Desbordamiento de PILA")

    def es_vacia(self):
        # Devuelve True si la lista está vacía, False si no.
        return self.items == []

    def muestraPila(self):
    
        print(self.items, "\tCIMA : ", (self.CIMA)) #Me muestra la Pila
        cantidad =self.cantElementos()
        indices =''
        for i in range(cantidad):
            indices = indices + str(i)+'  '
        print(indices+'  INDICES')

    def eliminar(self):

        # Devuelve el elemento tope y lo elimina de la pila.
        # Si la pila está vacía, se muestra que la pila esta vacía
        try:
            self.CIMA = self.CIMA-1
            return self.items.pop()
        except IndexError:
            print("La pila está vacía")
            self.CIMA = 0

    def cantElementos(self): #este metodo me dara la cantidad de elementos que va teniendo la Cola
        CIMA = len(self.items)
        return CIMA

if __name__ == '__main__':
    salir = False
    salirGeneral =False
    while not salirGeneral:
        opcion = int(input('MENU\nEscoge el tipo de estructura de datos a utilizar: \n1. Pilas\n2. Salir\nOpcion : '))
        if(opcion ==1):
            p = Pila()
            while not salir: 
                opcion = int(input('\n1. Insertar\n2. Eliminar\n3. Mostrar\n4. Regresar\nOpcion : '))
                if opcion ==1:
                    #validamos si el numero que ingresara, esta entre 1 y 99
                    numero = int(input('Insertar numero entre 1 y 99 : '))
                    if numero >0 and numero<100:
                        #Si si esta en el rango, entonces apilamos la pila
                        p.insertar(numero)
                    else:
                        print('No se puede agregar numero mayor a 99 o menor que 0')
                elif opcion ==2:
                    p.eliminar()

                elif opcion ==3:
                    p.muestraPila()

                elif opcion ==4:
                    salir =True
                else: 
                    print('opcion Incorrecta')
        elif (opcion ==2):
            print('Salir del programa')
            salirGeneral =True
        else:
            print('opcion Incorrecta')
