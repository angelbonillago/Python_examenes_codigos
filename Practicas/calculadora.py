#calculadora

operacion = input("Ingresa el primer caracter operacion a efectuar :->  ").lower()
operacion = operacion[0]

if operacion =="s" or operacion == "r" or operacion =="m" or operacion == "d":
	valor1 = float(input("ingresa valor a->  "))	
	valor2 = float(input("ingresa valor b->  "))	

	if operacion == "s":
		print(f"La suma es : {valor2+valor1:.2f}")
	if operacion == "r":
		print(f"La resta es : {valor1-valor2:.2f}")
	if operacion == "m":
		print(f"La multipliacion es : {valor2*valor1:.2f}")
	if operacion == "d":
		print(f"La division es : {valor1//valor2:.2f}")	


else:

	print("Ingresa una operacion valida")