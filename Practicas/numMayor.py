#Pide 3 numeros y dume cual es el mayor.

num1= int(input("Ingresa numero a->  "))
num2= int(input("Ingresa numero b->  "))
num3= int(input("Ingresa numero c->  "))

#ahora hallaremos el mayor.

if num1>=num2:
	aux = num1
	if aux >= num3:
		print(f"\nEl numero mayor es: {aux}")

elif num2>=num3:
	print(f"\nEl numero mayor es: {num2}")
else:
	print(f"\nEl numero mayor es: {num3}")

print("fin of th program")