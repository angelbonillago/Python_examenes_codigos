from tkinter import *
from tkinter import messagebox as mensajito

def mensaje():
    #mensajito.showinfo("Hola","HABLA PE ")
    #mensajito.showwarning("Alerta","tu no eres un admin ")
    #mensajito.showerror("error","Error inesperado, cambia de vida")
    mensajito.askquestion("Salir","Estas seguro que quieres salir?")




root=Tk()


Button(root,text="Dame",command=mensaje).pack()
root.mainloop()
