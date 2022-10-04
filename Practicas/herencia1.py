class Persona():

    def __init__(self, nombre, edad, lugar_residencia):
        self.nombre = nombre
        self.edad = edad
        self.lugar_residencia = lugar_residencia

    def descripcion(self):
        print("Nombre: ", self.nombre, "\nEdad : ", self.edad,
              "\nLugar de Residencia: ", self.lugar_residencia)


class Empleado(Persona):
    """docstring for Empleado"""

    def __init__(self, salario, antiguedad, nombree, edadd, residenciaa):

        super().__init__(nombree, edadd, residenciaa)
        self.salario = salario
        self.antiguedad = antiguedad

    def descripcion(self):
        super().descripcion()
        print("Salario: ", self.salario, "\nAntiguedad: ", self.antiguedad)


antonio = Persona("Antonio", 44, "Peru")
antonio.descripcion()
print("--------------------------------------------")
"""
antonio2 = Empleado(1560, 10)
# Nos daria error, ya que al heredar, no tendriamos el nombre,edad,luagr
antonio2.descripcion()
"""

Angel = Empleado(100, 20, "Angel bonilla", 21, "Ferreñafe")
Angel.descripcion()
