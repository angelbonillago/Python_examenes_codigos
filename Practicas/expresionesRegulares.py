# EXPRESIONES REGULARES
import re

cadena = "Aprenderemos expresiones regulares u imprimir objetos re en Python. Python es un lenguaje interprete"
# print(re.search("Aprenderemoos",cadena))#devuelve un objeto si lo encuentra
textoAbuscar = "Python"
textoEncontrado = re.search(textoAbuscar,cadena)

print(textoEncontrado.start()) #me da el indice de donde empieza el texto encontrado
print(textoEncontrado.end())#me da el indice de donde termina el texto encontrado
print(textoEncontrado.span())#me da una tupla, del indice de donde empieza y termina el objeto encontrado. Ejm : (37,45)



textoEncontrado = re.findall(textoAbuscar,cadena) #Me dara cuantos onjetos encontrados hubo en la busquedad. Ejm : ['Python','Python']

print(textoEncontrado)

print(len(re.findall(textoAbuscar, cadena)))# Me dara cuantos onjetos encontrados hubo en la busquedad. Ejm : ['Python','Python']
