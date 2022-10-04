"""
Escriba un programa para solicitar al usuario las horas y la tarifa por hora utilizando la entrada para calcular el pago bruto. 
Pague la tarifa por hora por las horas hasta 40 y 1.5 veces la tarifa por hora por todas las horas trabajadas por encima de las 40 horas. 
Use 45 horas y una tasa de 10.50 por hora para probar el programa (el pago debe ser 498.75). Debe usar input para leer una cadena y float () para convertir la cadena en un número. 
No se preocupe por el error al verificar la entrada del usuario; suponga que el usuario escribe los números correctamente.
"""

"""pedir al usuario las horas y tarifa"""

horas=  int(input("horas: "))
tarifa_hora = float(input("Tarifa por hora: "))
print(type(tarifa_hora))
pago_bruto=0.0;
if (horas>40):
	fijo = 40*tarifa_hora
	horas_extras=horas-40
	pago_bruto = fijo + (horas_extras*1.5*tarifa_hora)
	print(pago_bruto)
else:
	pago_bruto = horas*tarifa_hora
	print(pago_bruto)







