# conjuntos
# el conjunto es un conjunto de elementos desordenados, y permite tener elementos unicos.
'''

conunto = set()  # con este metodo indico que es un conjunto vacio y luego podre agregar o dejarlo ahi
conunto = {1, 3, 78, "hola"}
conunto.add(45)
conunto.add(45)
conunto.add(45)
conunto.add("242")
conunto.add("nos vamos") # metodo add,para agregar un valor
conunto.add(False)
# Al momento de agregar,no lo hace al final del conunto,si no, en orden aleatorio.
 
#para eliminar un valor

#conunto.discard(False)

if "241" in conunto:
	print("Entonces el valor 242,si esta en el conjuto")
else:
	print("busca con otro valor")

print(conunto)

'''
#Operaciones con conjuntos:

print("Operaciones con conjutos")

conjA = {1,2,45,67}
conjB = {2,45,7,8,8}
print(conjA,"  \n",conjB)
#union de conjuntos
conjC = conjA | conjB
print("Union de conjuntos : ",conjC) 




