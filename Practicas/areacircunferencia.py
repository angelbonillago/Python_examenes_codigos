#Hallar el area y la longitud de circunferencia.

import math

radio = int(input("Radio -> "))

area = math.pi * (radio**2)
longitud = 2* math.pi*radio

print(f"El area de la circunferencia es : {area:.2f} y su longitud es : {longitud:.2f}") #el ":.2f" se usa para obtener solo 2 decimales. y se desea 3, seria ":.3f".


