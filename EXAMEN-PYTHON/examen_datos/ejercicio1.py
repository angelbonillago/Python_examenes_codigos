class Pila:
    """ Representa una pila con operaciones de apilar, desapilar y
        verificar si está vacía. """

    def __init__(self):
        """ Crea una p
        ila vacía. """
        # La pila vacía se representa con una lista vacía
        self.items = []
        self.CIMA = 0
        self.ITEM_A=0
        self.ITEM_B=0

    def apilar(self, x):
        # Agrega el elemento x a la pila. """
        # Apilar es agregar al final de la lista.
        if (self.cantElementos() < 6):
            self.items.append(x)
            self.CIMA = self.CIMA+1
            #ITEM_A=self.items(x)
            #print("\nCIMA : ",(self.CIMA)+1,"\n")
        else:
            print("Desbordamiento de PILA")
            #print("Desbordamiento de PILA")
            pass

    def es_vacia(self):
        # Devuelve True si la lista está vacía, False si no. """
        return self.items == []

    def muestraPila(self):
    
        print(self.items, "\tCIMA : ", (self.CIMA), "\n")

    def desapilar(self):

        # Devuelve el elemento tope y lo elimina de la pila.
        # Si la pila está vacía levanta una excepción.
        try:
            #self.ITEM_A = self.items[self.CIMA]
           # print("ITEM_A : ",ITEM_A)
            self.CIMA = self.CIMA-1
            #self.ITEM_A=self.items[]
            return self.items.pop()

            #self.CIMA = self.CIMA-1
        except IndexError:
            print("La pila está vacía")
            self.CIMA = 0

    def cantElementos(self):
        CIMA = len(self.items)
        return CIMA
    def dameUltimoElemento(self):
        tamaño=0
        tamaño=len(self.items)
        return self.items[tamaño-1]



if __name__ == '__main__':
    # Registro()
    p = Pila()
    p.apilar(6)
    p.apilar(2)
    p.apilar(4)
    p.apilar(5)
    p.muestraPila()

    print("\tMENU\n")
    print("a) Sacar un elemento de la PILA  ( guardarlo  en  la  variable  ITEM_A )")
    ITEM_A=p.dameUltimoElemento()
    p.desapilar()
    #print("pilasacada",ITEM_A)

    p.muestraPila()

    print("b)Sacar un elemento de la PILA  ( guardarlo  en  la  variable  ITEM_B ).")
    ITEM_B=p.dameUltimoElemento()
    #print("pilasacada",ITEM_B)
    p.desapilar()
    p.muestraPila()

    print("c) Meter en la PILA  ( ITEM_C   =   ITEM_A   +  2 ).")
    ITEM_C=ITEM_A+ITEM_B
    p.apilar(ITEM_C)
    p.muestraPila()

    print("d)Meter en la PILA 2 elementos  ( ITEM_D = 3    e    ITEM_E  =  9 ).")
    ITEM_D = 3
    ITEM_E  =  9
    p.apilar(ITEM_D)
    p.apilar(ITEM_E)
    p.muestraPila()

    print("e) Meter en la PILA  (ITEM_A   -   ITEM_D).")
    x=ITEM_A - ITEM_D
    p.apilar(x)
    p.muestraPila()

    print("f) Meter en la PILA  (ITEM_F  =  8).")
    ITEM_F  =  8
    p.apilar(ITEM_F)
    p.muestraPila()

    print("g)Sacar de la Pila 2 elementos.")

    p.desapilar()
    p.desapilar()
    p.muestraPila()

    print("h)Sacar de la Pila 3 elementos.")

    p.desapilar()
    p.desapilar()
    p.desapilar()
    p.muestraPila()


    print("i) Meter en la PILA  8,  5,  1,  4  y  3")

    p.apilar(8)
    p.apilar(5)
    p.apilar(1)
    p.apilar(4)
    p.apilar(3)
    p.muestraPila()

    print("j) Sacar de la Pila  4 elementos.")

    p.desapilar()
    p.desapilar()
    p.desapilar()
    p.desapilar()
    p.muestraPila()
