from tkinter import *

def seleccionar():
    cadena =""
    if(leche.get()):
        print("Con leche")
        cadena+=" Con leche"
    else:
        print(" Sin leche")
        cadena+="Sin leche"
    if(azucar.get()):
        print("con azucar")
        cadena+=" con azucar"
    else:
        print("Y sin azucar")
        cadena+=" y sin azucar"

    monitor.config(text=cadena)
"""
def seleccionar():
    monitor.config(text="{}".format(opcion.get()))
def resetear():
    opcion.set(None)
    monitor.config(text="")
"""

root = Tk()
root.title("Ventanita")
#root.config(bd=15) #borde de 15pixeles
leche = IntVar()
azucar = IntVar()

frame=Frame(root)
frame.pack(side="left")
Label(frame,text="Como queres el cafe?").pack()
Checkbutton(frame,text="Con leche",variable=leche,onvalue=1,offvalue=0,command=seleccionar).pack()
Checkbutton(frame,text="Con azucar",variable=azucar,onvalue=1,offvalue=0,command=seleccionar).pack()

monitor=Label(frame)
monitor.pack()

root.mainloop()
