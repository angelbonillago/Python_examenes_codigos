from tkinter import *
import modulos


f = Frame(height=300,width=300)
f.pack(padx=15,pady=15)

logoimg = PhotoImage(file="josevicentecarratala.gif")
etiquetalogo = Label(f,image = logoimg)
etiquetalogo.pack(side=TOP,padx=10,pady=10)

titulo = Label(f,text="Agenda Telefónica",fg="blue",font=("Arial",24))
titulo.pack(side=TOP,padx=10,pady=10)

autor = Label(f,text="Jose Vicente Carratala")
autor.pack(side=TOP,padx=10,pady=10)

campo = Entry(f,textvariable = 5)
campo.pack(side=TOP,padx=10,pady=10)

##boton1 = Button(f,text="Listar elementos de la agenda",command=lambda:modulos.listar(int(Entry.get(campo))))
boton1 = Button(f,text="Listar elementos de la agenda")
boton1.pack(side=BOTTOM,padx=10,pady=10)

lista = Listbox(f)
lista.pack(side=TOP,padx=10,pady=10)




