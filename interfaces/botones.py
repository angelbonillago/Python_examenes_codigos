from tkinter import *
"""
def imprime():
    print("le diste click a este botton")
def crearLabel():
    #Label(root,text="Label fue creada").pack()
    label=Label(root,text = "Label fue creada").pack()
"""
def dameSuma():
    num1 = float(n1.get())
    num2 = float(n2.get())
    resultado.set(num1+num2)
def dameResta():
    num1 = float(n1.get())
    num2 = float(n2.get())
    resultado.set(num1-num2)
def dameMulti():
    num1 = float(n1.get())
    num2 = float(n2.get())
    resultado.set(num1*num2)
def dameDivi():
    num1 = float(n1.get())
    num2 = float(n2.get())
    resultado.set(num1/num2)    

def borra():
    n1.set("")
    n2.set("")

def ponerDisable():
    entry1.config(state="disabled")

root = Tk()
root.title("Ventanita")

n1=StringVar()
n2=StringVar()
resultado = StringVar()

Label(root, text="Numero 1").pack()
Entry(root,justify="center",textvariable=n1).pack()
Label(root, text="Numero 2").pack()
Entry(root,justify="center",textvariable=n2).pack()

Label(root, text="Resultado").pack()
entry1= Entry(root,justify="center",textvariable=resultado,state="disabled").pack()
#entry1.config(state="disabled")


Button(root,text="Sumar",command=dameSuma).pack(side="left")
Button(root,text="Restar",command=dameResta).pack(side="left")
Button(root,text="*",command=dameMulti).pack(side="left")
Button(root,text="/",command=dameDivi).pack(side="left")
Button(root,text="Borrar",command=borra).pack(side="left")




root.mainloop()