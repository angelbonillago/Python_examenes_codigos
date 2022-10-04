import pickle
""" aqui creo el archuvo binario
list_nombres = ["Angel","Yasmin","Alexis","Esperanza"]

fichero_binario = open("Lista_nombre","wb")

pickle.dump(list_nombres,fichero_binario)

fichero_binario.close()

del fichero_binario
"""

#AQqui el archivo creado, lo abriremos y veremos que hay dentro

fiheroAbrir = open("Lista_nombre","rb")
lista= pickle.load(fiheroAbrir)

print(lista)




