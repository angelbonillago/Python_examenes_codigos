class coche():

    def __init__(self):
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4
        self.__enmarcha = False

    def imprimir(self):

        print(f"El largo de chassis es : {self.__largoChasis}\nEl ancho es : {self.__largoChasis}")

    def arrancar(self):
        valor = int(input("Ingresa la velocidad"))

        if valor > 0:
            self.__enmarcha = True
        else:
            self.__enmarcha = False

    def estado(self):
        if self.__enmarcha:
            print("El carro esta en marcha")
        else:
            print("El carro esta detenido")

    def revisionInterno(self):

        print("Haremos el chequeo interno--")
    def arrancarCarro(sel,arrancar):
        self.__enmarcha=arrancar
        if (self.__enmarcha):
            return "El carro esta en marcha"
        else:
            return ""





miCarro = coche()
miCarro.imprimir()
miCarro.arrancar()
miCarro.estado()
