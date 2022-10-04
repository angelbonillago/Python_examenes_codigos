class coche():
    def dezplazamiento(self):
        print("Me desplazare usando 4 llantas")


class moto():
    def dezplazamiento(self):
        print("Me dezplazare usando 2 llantas")


class camion():
    def dezplazamiento(self):
        print("Me dezplazare usando 6 llantas")


class bicicleta():
    def dezplazamiento(self):
        print("Me dezplazare usando 1 llantas")


vehiculo = moto()
vehiculo.dezplazamiento()


def dezplazamientoVehiculo(ObjetoVehiculo):
    ObjetoVehiculo.dezplazamiento()


mivehiculo = camion()
dezplazamientoVehiculo(mivehiculo)

mivehiculo2 = moto()
dezplazamientoVehiculo(mivehiculo2)

mivehiculo3 = bicicleta()
dezplazamientoVehiculo(mivehiculo3)
