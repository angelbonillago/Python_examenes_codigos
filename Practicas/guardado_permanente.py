import pickle

class Persona():

	def __init__(self,nombre,edad,genero):
		self.nombre =nombre
		self.edad=edad
		self.genero=genero

		print("Se creo una persona Nueva llamada : ",self.nombre)

	def __str__(self):
		return "{}  {}  {}".format(self.nombre,self.genero,self.edad)
class listaPersonas():

	lista_personas=[]
	def __init__(self):
		fichbpersona=open("ficherExterno","ab+")
		fichbpersona.seek(0)#cursor al inicio del archivo
		self.lista_personas=pickle.load()	



	def agregarPersonas(self,objetoPersona):
		self.lista_personas.append(objetoPersona)
	def dameListaPersona(self):
		for c in self.lista_personas:
			print(c)

objPersonas = listaPersonas()
persona1 = Persona("Angel",22,"MASCULINO")
objPersonas.agregarPersonas(persona1)
persona2=Persona("Yasmin",23,"MAMACITA")
objPersonas.agregarPersonas(persona2)
persona3 = Persona("Esperanza",23,"RICA")
objPersonas.agregarPersonas(persona3)
persona4 = Persona("Alexis",22,"LEON")
objPersonas.agregarPersonas(persona4)


objPersonas.dameListaPersona()



