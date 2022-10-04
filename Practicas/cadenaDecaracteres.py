#cadenaDecaracteres.py

cadena= "video NUMERO 33-METODOS DE LAS CADENAS!"

print(cadena.lower()) #convierte el strign a minuscula

print(cadena.capitalize())

edad = input("Dame tu edad : ")

while(edad.isdigit()==False):
	print("ooh tu no tienes mamita?, introduce un valor numerico")
	edad = input("Dame tu edad : ")

if int(edad)>18:
	print("Ya tienes barba,Pasa!")
else:
	print("Cuando seas pepon, entras!")


