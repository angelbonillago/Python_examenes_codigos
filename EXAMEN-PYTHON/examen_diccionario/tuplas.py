#Tuplas
tupla =(1,2,3,4,"Hola",[1,7,8],20,4)

print(tupla[:3])
print(tupla.index("Hola")) #me da el indice del elemento "Hola"
print(tupla.count(4)) #buscara cuantos elementos hay del mismo valor, en este caso hay dos 4
print(4 in tupla)
print(len(tupla))


#convertir una tupla a lista
lista = list(tupla)
print(lista)

listaAux =[1,2,3,4,"Hola",[1,7,8],20,4]
tupla=tuple(listaAux)
var = 4+5
print(var)
