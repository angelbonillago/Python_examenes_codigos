# Costo de un articulo .
from tkinter import *
from tkinter import messagebox


def dameCambio():
    print("Hola")
    vprecio= precio.get()
    vcancelado = cancelado.get()
    if vprecio <= vcancelado and (vprecio >0 and vcancelado>0):
        if vprecio == vcancelado:
            print("CAMBIO: S/0.00")
            messagebox.showinfo(message="El cambio es S/ 0.O0", title="Ejercicio-Devolucion")
        else:
            vcambio = vcancelado-vprecio
            print("CAMBIO:  S/", vcambio)
        messagebox.showinfo(title="Ejercicio-Devolucion",message="El cambio es S/: "+str(vcambio))
        #salir = True
    else:
        print("Debes cancelar un monto igual al precio del producto!")
        messagebox.showinfo(title="Ejercicio-Devolucion",message="Debes cancelar un monto igual al precio del producto!")





tv = 1000
radio = 350
celular = 200
salir = False
interface = Tk()
interface.geometry("500x300+100+100")
interface.title("Ejercicio2")
labelTitulo = Label(text="Calculo de cambio para un comprador",font=("Arial",14)).pack()
labelPrecio = Label(text="Precio del producto ",font=("Arial",14)).place(x=10,y=40)
precio = DoubleVar()
txtIngresarPrecio = Entry(interface,textvariable=precio).place(x=270,y=48)

labelCancelado = Label(text="Cancelado ",font=("Arial",14)).place(x=10,y=70)
cancelado = DoubleVar()
txtIngresarCancelado = Entry(interface,textvariable=cancelado).place(x=270,y=78)

botonResultado = Button(interface,text="Calcular",command=dameCambio,font=("Arial",14)).place(x=10,y=110)
interface.mainloop()
"""
while (not salir):
    precio = float(input("Ingresa el precio del producto:? "))
    cancelado = float(input("¿Cuanto a pagado el cliente?"))

    if precio <= cancelado and (precio >0 and cancelado>0):
        if precio == cancelado:
            print("CAMBIO: S/0.00")

        else:
            cambio = cancelado-precio
            print("CAMBIO:  S/", cambio)
        salir = True
    else:
        print("Debes cancelar un monto igual al precio del producto!")


"""