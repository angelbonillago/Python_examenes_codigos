# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 20:52:18 2021

@author: migda
"""

from datetime import date
from datetime import datetime

#Día actual
nombres =[]
fechacreacion = []




today = date.today()

#Fecha actual
now = datetime.now()

print(today)
print(now)

print("El día actual es {}".format(today.day))
print("El mes actual es {}".format(today.month))
print("El año actual es {}".format(today.year))

