class vehiculos():

    def __init__(self, marca, modelo):

        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.arrancar = True

    def acelerar(self):
        self.acelerar = True

    def frena(self):
        self.frena = True

    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ",
              self.enmarcha, "\nAcelerando : ", self.acelera, "\nFrena: ", self.frena)


class Moto(vehiculos):
    haciendoCaballito = ""

    def caballito(self):
        self.haciendoCaballito = "Inicio del caballito"
    # Sobreescribiendo el metodo estado de la clase padre Vehiculos():

    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ",
              self.enmarcha, "\nAcelerando : ", self.acelera, "\nFrena: ", self.frena, "\n", self.haciendoCaballito)


class Furgoneta(vehiculos):
    """docstring for F"""

    def carga(self, cargar):
        self.cargado = cargar
        if self.cargado:
            print("La furgoneta esta cargada")
        else:
            print("La furgoneta No esta cargada")


class VElectricos(vehiculos):
    def __init__(self,marca,modelo):
        super().__init__(marca,modelo)
        self.autonomia = 100

    def cargarEnergia(self):
        self.cargando = True


class BicicletaElectrica(vehiculos,VElectricos):#herencia multiple
    """docstring for BicicletaElectrica"""
    pass




"""
        
miMoto = Moto("Honda", "KAWASAKY")
miMoto.caballito()
miMoto.estado()
"""
miFurgoneta = Furgoneta("NISSAN", "4*4")
miFurgoneta.arrancar()
miFurgoneta.acelerar()
miFurgoneta.estado()
miFurgoneta.carga(True)

#herencia multiple:
mibici=BicicletaElectrica("BMX","H1220")
