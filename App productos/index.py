from tkinter import ttk 
from tkinter import * 
import sqlite3


class Producto:
    """docstring for Producto"""

    db_name= 'midata.db' 



    def __init__(self, window):
        self.wind = window
        self.wind.title("Prodcutos en general")
        
        #creating a Frame container
        frame = LabelFrame(self.wind,text="Register a new Product: ")
        frame.grid(row=0,column=0,columnspan=3,pady=20)
        #nameInput
        Label(frame,text="Name: ").grid(row=1,column=0)
        self.name = Entry(frame)
        self.name.focus()
        self.name.grid(row=1,column=1)


        #price input
        precio = IntVar()
        Label(frame,text="Price : ").grid(row=2,column=0)
        self.price = Entry(frame)
        self.price.grid(row=2,column=1) 
        ttk.Button(frame,text="save product",command=self.add_product).grid(row=3,columnspan=2,sticky=W+E)
        #MENSAJE DE AGREGADO
        self.mensaje = Label(text='',fg='red')
        self.mensaje.grid(row=3,column=0,columnspan=2,sticky=W+E)


        #table
        self.tree=ttk.Treeview(column=2,height=10)
        self.tree.grid(row=4,column=0,columnspan=2)

        self.tree.heading('#0',text="Price of Product",anchor=CENTER)
        self.tree.heading('#1',text="Name of Product",anchor=CENTER)#encabezados de las columnas
        #self.tree.heading('#2',text="Price of Product",anchor=CENTER)

        ttk.Button(text='Eliminar',command=self.delete_product).grid(row=5,column=0,sticky=W+E)
        ttk.Button(text='Actualizar',command=self.edit_product).grid(row=5,column=1,sticky=W+E)

        self.get_product()


    def run_query(self,query,parameters=()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query,parameters)
            conn.commit()
        return result

    def get_product(self):

        #cleaning table
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        #quering data   
        query='SELECT * FROM product ORDER BY name DESC'
        db_rows= self.run_query(query)
        print(db_rows)
        val=0
        for row in db_rows:
            print(row)
            self.tree.insert('',0,text=row[1],values=row[2])
            val=val+1

       

    def validation(self):
        return len(self.name.get()) !=0 and len(self.price.get()) !=0

    def add_product(self):
        if self.validation():
            
            print(self.name.get())
            print(self.price.get())
            query='INSERT INTO product values(NULL,?,?)'
            parameters = (self.name.get(),self.price.get())
            self.run_query(query,parameters)
            #print("datos guardados con estilo")
            self.mensaje['text']='Producto {} fue agregado de manera correcta'.format(self.name.get())
            self.name.delete(0, END)
            self.price.delete(0, END)

        else:
            print("product is required")
            self.mensaje['text']='nombre y precio son necesarios'
            self.name.delete(0, END)
            self.price.delete(0, END)

        self.get_product()



    def delete_product(self):

        self.mensaje['text']=''
        try:
            self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            self.mensaje['text']='Por favor, seleccionar un records'
            return
        self.mensaje['text']=''
        name=self.tree.item(self.tree.selection())['text']
        query = 'DELETE FROM product WHERE name=?'  
        self.run_query(query,(name,))
        self.mensaje['text']='record {} deleted succesddfully'.format(name)
        self.get_product()    

    def edit_product(self):
        self.mensaje['text']=''
        try:
            self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            self.mensaje['text']='Por favor, seleccionar un records'
            return
        name= self.tree.item(self.tree.selection())['text']
        price = self.tree.item(self.tree.selection())['values'][0] #nombre del precio del prodcuto que el usuario esta que selecciona
        self.ventanaEdit = Toplevel()#para crear una ventana encima
        self.ventanaEdit.title("Edit Product")

        #antiguo nombre
        Label(self.ventanaEdit,text='Nombre antiguo:').grid(row=0,column=1)
        Entry(self.ventanaEdit,textvariable=StringVar(self.ventanaEdit,value=name),state='disabled').grid(row=0,column=2)
        #nombre nuevo
        Label(self.ventanaEdit,text='Nombre Nuevo:').grid(row=1,column=1)
        newName=Entry(self.ventanaEdit)
        newName.grid(row=1,column=2)
        newName.focus()

        #antiguo precio
        Label(self.ventanaEdit,text='Precio antiguo:').grid(row=2,column=1)
        Entry(self.ventanaEdit,textvariable=DoubleVar(self.ventanaEdit,value=price),state='disabled').grid(row=2,column=2)
        #precio nuevo
        Label(self.ventanaEdit,text='Precio Nuevo:').grid(row=3,column=1)
        newPrice=Entry(self.ventanaEdit)
        newPrice.grid(row=3,column=2)
        Button(self.ventanaEdit,text='Actualiza',command=lambda:self.edit_registro(newName.get(),name,newPrice.get(),price)).grid(row=4,column=2,sticky=W+E)

    def edit_registro(self,nuevoNombre,nombre,nuevoPrecio,precio):
        query='UPDATE product SET name=?,price=? WHERE name=? AND price=?'
        parameters=(nuevoNombre,nuevoPrecio,nombre,precio)
        self.run_query(query,parameters)
        self.ventanaEdit.destroy()#cerrando la ventana
        self.mensaje['text']="Records {} updated Succesfully".format(nombre)
        self.get_product()


if __name__=='__main__':
    window=Tk()
    aplicacion=Producto(window)
    window.mainloop()

