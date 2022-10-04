from tkinter import *
from tkinter import messagebox as mensajito

def ventana():
    window = Tk()
    window.title("Tkinter")
    frame = Frame(window).pack()
    lbl = Label(frame, text="Introduce un número").pack()
    result = Label(frame,text="").pack()
    txt = Entry(frame,width=10).pack()
    #txt.focus()
    def mensaje():
        res = int(txt.get())
        #aquí compruebas que es un número
        res = int(res) if res.isdigit() else 0
        self.result.configure(text= res)
        self.txt.delete(0, END)

    btn = Button(frame, text="Activa", bg="red",fg="white", command=mensaje)
    btn.pack()
    window.mainloop()


def main():
    ventana()

if __name__ == '__main__':
    main()