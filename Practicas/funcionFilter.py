'''def filtro(elemento):
	return (elemento > 0)


lista = [-1, -5, -8, 0, 25, 15, 47, 7, -23]
lista2 = filter(filtro, lista)



print(lista)
print(*lista2)

'''
def filtro_vocales(parametro):
    list_vocales = ['a', 'i', 'o', 'e', 'u']
    #iteraciones = parametro
    numvocales = list_vocales.len()
    indice = 0

    while numvocales > 0:

		iteraciones = parametro
  		while iteraciones > 0 :

        	if list_vocales[indice] == parametro :
            	return list_vocales[indice]
        	else:
        		iteraciones = -1
    	indice = +1
    	numvocales = -1



list_parametros = ['x', 'c', 's', 'e', 'q', 'z', 'a', 'o', 'ñ', 'n']
lista2 = filter(filtro_vocales, list_parametros)

print(list_parametros)
print(*lista2)
