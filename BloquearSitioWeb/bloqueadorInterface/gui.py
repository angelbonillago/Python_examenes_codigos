from tkinter import *
from tkinter.ttk import *
from logica_block import *

window = Tk()
objeto = Logica()

window.title("Block procastination")

window.geometry('550x200')

lbl = Label(window, text="Ingresa tu hora de inicio de trabajo: ")

lbl.grid(column=0, row=0)

lbl2 = Label(window, text="Ingresa tu hora de fin de trabajo: ")

lbl2.grid(column=0, row=1)
"""
txt = Entry(window,width=10)
txt2 = Entry(window,width=10)

txt.grid(column=1, row=0)
txt2.grid(column=1, row=1)
"""
combo = Combobox(window)

combo['values']= (1, 2, 3, 4, 5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24)

combo.current(0) #set the selected item

combo.grid(column=1, row=0)

combo1 = Combobox(window)

inicio = combo.get()

combo1['values']= (1, 2, 3, 4, 5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24)

combo1.current(0) #set the selected item

combo1.grid(column=1, row=1)

fin = combo1.get()

#objeto.comparaHorario(inicio,fin)
btnGuardar=Button(window, text="Guardar Horario")
btnEditar=Button(window, text="Editar Horario")
btnGuardar.grid(column=3, row=1)
btnEditar.grid(column=4, row=1)

#btn = Button(window, text="Click Me", command=clicked)

#btn.grid(column=2, row=0)

lbl3 = Label(window, text="Inicio:  ")

lbl3.grid(column=0, row=2)

lbl4 = Label(window, text="Fin:  ")

lbl4.grid(column=0, row=3)

window.mainloop()