from tkinter import *


root = Tk()
root.title("Ventanita")
frame =Frame(root)



label=Label(root,text = "Nombre muy largo")
label.grid(row=0,column=0,sticky="e",padx=5,pady=5)

entry =Entry(root)
entry.grid(row=0,column=1,padx=5,pady=5)
entry.config(justify="right")#Para poner el cursor en el medio o a la derecha,izquierda


label2=Label(root,text = "apellidos")
label2.grid(row=1,column=0,sticky="e",padx=5,pady=5)

entry2 =Entry(root)
entry2.grid(row=1,column=1,padx=5,pady=5)
entry2.config(justify="center")#Para poner el cursor en el medio o a la derecha,izquierda

label3=Label(root,text = "contrasena")
label3.grid(row=2,column=0,sticky="e",padx=5,pady=5)

entry3 =Entry(root)
entry3.grid(row=2,column=1,padx=5,pady=5)
entry3.config(justify="right",show=":")#Para poner el cursor en el medio o a la derecha,izquierda
#show, para las contraseñas, ahi se usaria el *,para evitar vean tu contra


root.mainloop()