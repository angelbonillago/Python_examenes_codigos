from tkinter import *

root = Tk()
root.title("Ventanita")

mainPrincipal=Menu(root)
root.config(menu=mainPrincipal)

archivoMenu= Menu(mainPrincipal,tearoff=0)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Abrir")
archivoMenu.add_command(label="cerrar")
archivoMenu.add_separator()
archivoMenu.add_command(label='Salir',command=root.quit)

editarMenu= Menu(mainPrincipal,tearoff=0)
editarMenu.add_command(label='Cortar')
editarMenu.add_command(label='Copiar')
editarMenu.add_command(label='Pegar')

ayudaMenu= Menu(mainPrincipal,tearoff=0)
ayudaMenu.add_command(label='Ayuda')
ayudaMenu.add_separator()
ayudaMenu.add_command(label='acerca de ')


#para evitar que aparezca el "--",cuando el submenu no tiene nada, se coloca tearoff =0, y ya no saldra nada

mainPrincipal.add_cascade(label="Archivo",menu=archivoMenu)
mainPrincipal.add_cascade(label="Editar",menu=editarMenu)
mainPrincipal.add_cascade(label="Ayuda",menu=ayudaMenu)

root.mainloop()