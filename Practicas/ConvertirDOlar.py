from tkinter import *
from tkinter import messagebox


def dameConversion():
    vmonto = monto.get()
    vprecio= precio.get()



    if vmonto>0 and vprecio>0:
        conversion = vmonto / vprecio
        messagebox.showinfo(title="Ejercicio-Devolucion",message="El cambio A dolares es : S/ "+str((conversion)))
    else:
        messagebox.showinfo(title="Ejercicio-Devolucion", message="OE CTM! NO SEAS PENDEJO")








interface = Tk()
interface.geometry("500x300+100+100")
interface.title("Convertir A Dolar")
labelTitulo = Label(text="Convertir",font=("Arial",14)).pack()
labelPrecio = Label(text="Precio del Dolar ",font=("Arial",14)).place(x=10,y=40)
precio = DoubleVar()
txtIngresarPrecio = Entry(interface,textvariable=precio).place(x=270,y=48)

labelMoneda = Label(text="Monto en Soles ",font=("Arial",14)).place(x=10,y=70)
monto = DoubleVar()
txtIngresarCancelado = Entry(interface,textvariable=monto).place(x=270,y=78)

botonResultado = Button(interface,text="Calcular",command=dameConversion,font=("Arial",14)).place(x=10,y=110)
interface.mainloop()