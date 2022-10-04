# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 19:26:12 2021

@author: migda
"""
resp = 's'

estudiantes = []
datos = []
aux2 = () #tupla
puntaje = []
nombres = []

while resp == 's':
    cedula = input("Ingrese la identificación:")
    estudiante = input("Ingrese el nombre del estudiante:")
    ptos = int(input("Ingrese el puntaje obtenido:"))
       
    datos = [estudiante, ptos]
    aux2 = (cedula, datos)
    estudiantes.append(aux2)
    print('Los datos son ',estudiantes)
    del datos
    del aux2
    
    resp = input("Desea agregar otro estudiante s/n:")
   
examingreso = dict(estudiantes) 
print("Diccionario")
print(examingreso)

print("Valores")
for i in examingreso.values():
    nombres.append(i[0])
    puntaje.append(i[1])


mayor = max(puntaje)
posicion = puntaje.index(mayor)

print(f"El estudiante con mayor puntaje es:{nombres[posicion]} con {mayor}")

menor = min(puntaje)
posicion = puntaje.index(menor)
print(f"El estudiante con menor puntaje es:{nombres[posicion]} con {menor}")

promedio = sum(puntaje) / len(puntaje)
print(f"El puntaje promedio es:{promedio}")

clave = input("Ingrese la identificacion del estudiante a consultar:")
valor = examingreso.get(clave)

print(f"Nombre: {valor[0]}   Puntaje: {valor[1]}")

print("******** ESTUDIANTES QUE APROBARON**********")
for i in examingreso.values():
    if i[1] > 80:
        print(f"Nombre: {i[0]}   Puntaje: {i[1]}")







