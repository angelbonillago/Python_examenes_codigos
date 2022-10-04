# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 20:58:31 2021

@author: migda
"""

"""
Clave:     Laboratorio, Medicamento, Existencia, Anaquel
0909       MK, Loratadina, 20, 2
1023	      MK, Diclofenaco, 30,2
2345       Pharma, Loratadina, 25,3

CLAVE                 VALOR
LABORATORIO   MK, MK, PHARMA, BAYER, PHARMA, GSK
CLAVE                   0909, 1023,2345,8425,2100,2578
MEDICAMENTOS  Loratadina, Diclofenaco, Loratadina, Aspirina, Acetaminofen, Panadol
"""
resp = 's'
medicina = []

while resp.lower() =='s':
    clave = input("Ingrese la clave:")
    laboratorio = input("Laboratorio:")
    medicamento = input("Medicamento:")
    

    valores = [laboratorio, medicamento]
    aux2 = (clave, valores)    
    medicina.append(aux2)
    del valores
    del aux2
    
    resp = input("Desea agregar otro estudiante s/n:")
   
inventario = dict(medicina) 
print(inventario)

# Recorrer los valores
temp = []
for x in inventario.values():
    print(x)

med = input("Ingrese el medicamento:")

for pos,x in enumerate(inventario.values()):
    if x[1] == med:
       print (x[0])




resp = 's'
#Modelo 2
claves = []
laboratorios = []
medicamentos = []
while resp.lower() =='s':
    claves.append(input("Ingrese la clave:"))
    laboratorios.append(input("Laboratorio:"))
    medicamentos.append(input("Medicamento:"))
    

    resp = input("Desea agregar otro estudiante s/n:")
   
inv = dict({"ClAVE":claves,
                    "LABORATORIO": laboratorios,
                    "MEDICAMENTO": medicamentos           
                   }) 


print(inv)

temp.clear()

for x in inv['LABORATORIO']:
    print(x)

med = input("Ingrese el medicamento:")

for pos,x in enumerate(inv['MEDICAMENTO']):
    if x == med:
        print(inv['LABORATORIO'][pos])



