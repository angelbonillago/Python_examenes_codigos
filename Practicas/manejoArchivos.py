from io import open # para abrir un archivo externo
#MODO ESCRITURA

#archivoTexto = open("myfile.txt", "w") #crear un archivo para escritura "w"
#fraseAgregar = "Es un dia bueno para programar\n Vamos Angel"

#archivoTexto.write(fraseAgregar) #manipulacion de archivo, agregar datos

#archivoTexto.close() #cerrar el archivo


#MODO LECTURA 
"""
archivoTexto = open("myfile.txt","r")
#textoParaLeer = archivoTexto.read()
textoEnLinea= archivoTexto.readlines()
archivoTexto.close()

print(textoEnLinea[1])
"""
#MODO AGREGAR

#archivoTexto = open("myfile.txt","a")
#fraseAgregar = archivoTexto.write("\nSiempre ten a Dios en tu corazon")
#archivoTexto.close() 


#CURSORES 
"""
archivoTexto = open("myfile.txt","r")

#print(archivoTexto.read())
archivoTexto.seek(10)
#print("\n")
print(archivoTexto.read())

print(archivoTexto.read(12))#Leere el documento hasta la posicion 12

"""
 
archivoTexto = open("myfile.txt","r+")
lista_texto=archivoTexto.readlines() #saco todo en listas
lista_texto[1] ="Este parrafo lo agregue desde el exteriro,el rico cmd\n"
archivoTexto.seek(0) # lo pongo el cursor al inciio del archivo

archivoTexto.writelines(lista_texto)
archivoTexto.close()




