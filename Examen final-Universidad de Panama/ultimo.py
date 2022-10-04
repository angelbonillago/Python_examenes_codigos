"""
Escriba una función perfecto(n) que determine si un número entero dado n es un 
número perfecto. Un número perfecto debe ser igual a la suma de todos sus divisores 
enteros menores que el valor del número. 
Ejemplo: 28 = 1 + 2 + 4 + 7 + 14
Escriba un programa de prueba que use la función escrita y encuentre los números 
perfectos entre 1 y 1000
"""

#Modificado por BONILLA GONZALEZ
#CODIGO : 162340B
#---------------------------------------

def perfecto(num):
    
	suma = 0
	for i in range(1,num):
		if (num % (i) == 0):
			suma += (i)
	if num == suma:
		return True
	else:
		return False



if __name__ == '__main__':
    print(perfecto(28))
