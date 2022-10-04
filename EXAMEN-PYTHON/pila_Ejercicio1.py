class Pila:
    """ Representa una pila con operaciones de apilar, desapilar y
        verificar si está vacía. """

    def __init__(self):
        """ Crea una p
        ila vacía. """
        # La pila vacía se representa con una lista vacía
        self.items = []
        self.CIMA = 0

    def apilar(self, x):
        # Agrega el elemento x a la pila. """
        # Apilar es agregar al final de la lista.
        if (self.cantElementos() < 8):
            self.items.append(x)
            self.CIMA = self.CIMA+1
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
            self.CIMA = self.CIMA-1
            return self.items.pop()
            #self.CIMA = self.CIMA-1
        except IndexError:
            print("La pila está vacía")
            self.CIMA = 0

    def cantElementos(self):
        CIMA = len(self.items)
        return CIMA


if __name__ == '__main__':
    print('MENU\n')

    # Registro()
    p = Pila()
    p.apilar('A')
    p.apilar('B')
    p.apilar('C')
    p.apilar('D')
    p.muestraPila()

    print("\tMENU\n")
    print("a) Meter E, F, G y H")
    p.apilar('E')
    p.apilar('F')
    p.apilar('G')
    p.apilar('H')
    p.muestraPila()

    print("b) Meter la letra J")
    p.apilar('J')
    p.muestraPila()

    print("c)Sacar 6 elementos")
    p.desapilar()
    p.desapilar()
    p.desapilar()
    p.desapilar()
    p.desapilar()
    p.desapilar()
    p.muestraPila()

    print("d)Meter las letras K y L")

    p.apilar('K')
    p.apilar('L')
    p.muestraPila()

    print("e)Sacar 5 elementos")

    p.desapilar()
    p.desapilar()
    p.desapilar()
    p.desapilar()
    p.desapilar()
    p.muestraPila()

    print("f)Meter M, N, O, P, Q, R y S")
    p.apilar('M')
    p.apilar('N')
    p.apilar('O')
    p.apilar('P')
    p.apilar('Q')
    p.apilar('R')
    p.apilar('S')
    p.muestraPila()

    print("g) Meter T y X")

    p.apilar('T')
    p.apilar('X')
    p.muestraPila()

    print("h)Sacar 8 elementos")

    p.desapilar()
    p.desapilar()
    p.desapilar()
    p.desapilar()
    p.desapilar()
    p.desapilar()
    p.desapilar()
    p.desapilar()
    p.muestraPila()


