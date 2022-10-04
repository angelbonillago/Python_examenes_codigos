cantidad = int(input("cantidad"))
amigos = []
scores = []
for x in range(cantidad):
	nombre= (input("Nombres"))
	edad=int(input("edad: "))
	amigos.append([nombre])
	amigos[x].append(edad)
	scores.append(edad)
	print(amigos)

print("---------------------------------")

#obtener el minimo de las notas:
minEscore = min(scores)
print((minEscore))

print(type(minEscore))
cuentala=0
for x in range(len(amigos)):
	for y in range(len(amigos[x])):
		print(amigos[x][y])
		if(minEscore==amigos[x][y]):
			cuentala=cuentala+1
			print("ingreso")
if cuentala>1:
	print("A encontrado dos numeros menores iguales")

"""
for amigo in amigos:
	print("{:5}:  {:2}".format(amigo[0],amigo[1]))

"""