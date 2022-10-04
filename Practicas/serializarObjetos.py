import pickle

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

"""
coche=vehiculos("TOYOTA","PGK616")
coche1=vehiculos("NISAN","PGK606")
coche2=vehiculos("HYUNDAY","PGK676")

coches=[coche,coche1,coche2]

fichero = open("LosCarritos","wb")

pickle.dump(coches,fichero)

fichero.close()

del(fichero)
"""
fichero_abrir=open("LosCarritos","rb")
miCarros=pickle.load(fichero_abrir)
fichero_abrir.close()
for lista_coches in miCarros:
    print(lista_coches.estado())