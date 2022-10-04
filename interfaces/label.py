from tkinter import *


root = Tk()
root.title("Ventana")
root.resizable(1,1)

frame = Frame(root,width=500,height=500)
frame.pack()
#frame.config(width=500,height=500)
label = Label(frame,text ="Soy angel bonilla")
#label.pack()
label.place(x=200,y=250)




root.mainloop()