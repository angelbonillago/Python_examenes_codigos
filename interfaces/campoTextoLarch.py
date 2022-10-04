from tkinter import *
root = Tk()
root.title("Ventanita")
texto = Text(root)
texto.pack()
texto.config(width=30,height=10,font=("verdana",11),padx=15,pady=15,selectbackground="yellow") #30 caracteres en anchura y 10 caracteres en altura
#el selectbackground es para cuando queramos seleccionar una caantidad de texto, se tome el color que se puso, en ese caso yellow

root.mainloop()