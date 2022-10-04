from tkinter import *

def seleccionar():
	monitor.config(text="{}".format(opcion.get()))
def resetear():
	opcion.set(None)
	monitor.config(text="")

root = Tk()
root.title("Ventanita")

opcion=IntVar()


Radiobutton(root,text="Opcion °1",variable=opcion,value=1,command=seleccionar).pack()
Radiobutton(root,text="Opcion °2",variable=opcion,value=2,command=seleccionar).pack()
Radiobutton(root,text="Opcion °3",variable=opcion,value=3,command=seleccionar).pack()
Radiobutton(root,text="Opcion °4",variable=opcion,value=4,command=seleccionar).pack()
#el opcion es para que solo pueda seleccionar un solo radiobutons. tambien se identifica por el value

monitor=Label(root)
monitor.pack()
Button(root,text="reiniciar",command=resetear).pack()
mainloop()







