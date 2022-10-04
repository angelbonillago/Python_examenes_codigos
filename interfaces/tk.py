from tkinter import *


root = Tk()
root.title("Ventana")
root.resizable(1,1)

frame = Frame(root,width=500,height=500)
frame.pack(fill="both",expand=1)
#frame.config(width=500,height=500)
frame.config(cursor="pirate")
frame.config(bg="yellow")
frame.config(bd=25)
frame.config(relief="sunken")

root.config(cursor="arrow")
root.config(bg="blue")
root.config(bd=15)
root.config(relief="ridge")

root.mainloop()

#print("Este es una prueba")
