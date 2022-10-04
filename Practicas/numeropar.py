#Ejercicio de condicionales
#Pide 2 numeros y ver si uno de ellos es par, o si ambos lo son:

num1 = int(input("Ingresa numero1-->"))
num2 = int(input("Ingresa numero2-->"))
if num1>0 and num2>0:

	if num1%2==0 and num2%2==0:
		print(f"Ambos son numeros pares.!")
	
	if num1 %2==0 and num2%2!=0:
		print(f"El numero {num1} es par")
	if num1 %2!=0 and num2%2==0:
		print(f"El numero {num2} es par")
else:
	print("Ingresa numeros mayores a cero")