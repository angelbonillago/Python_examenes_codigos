#Creo las variables.
altura = float(input("Ingrese su altura en Metros: "))
peso = float(input("Ingrese su peso en KG: "))

#Salto de línea
print("\n")

IMC = peso / altura**2

#Creo la condición.
while True:
    if IMC < 18.5:
        diagnostico = "BAJO PESO"
        break
    if (IMC > 18.5 and IMC < 24.9):
        diagnostico = "PESO NORMAL"
        break
    if (IMC > 25 and IMC < 29.9):
        diagnostico = "SOBREPESO"
        break
    if (IMC > 30 and IMC < 34.9):
        diagnostico = "OBESIDAD TIPO 1"
        break
    if (IMC > 35 and IMC < 39.9):
        diagnostico = "OBESIDAD TIPO 2"
        break
    if IMC >= 40:
        diagnostico = "OBESIDAD TIPO 3"
        break

#He instalado la libreria Tabulate.
from tabulate import tabulate

#Ordeno el código para cuando se ejecute salga como me lo piden.
tabla = [[diagnostico, IMC]]    

print(tabulate(tabla, tablefmt='grid', headers=[' IMC', ' DIAGNÓSTICO']))