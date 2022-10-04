"""
@author: Carlos

"""

#librerias
import os# permite hacer operaciones del Sistema Operativo como crear una carpeta,etc.
from os import listdir
from os.path import isfile, join, isdir #Para lecctura de archivos y directorios
import shutil #Libreria para mover archivos
import errno #errores de crear directorio
import send2trash  #antes de importar, se debe instalar este paquete por consola. Esto servira para poder mandar archivos a la papelera.
import zipfile #Este módulo proporciona herramientas para crear, leer, escribir, agregar y listar un archivo ZIP
#import shutil#para comprimir un directorio con archivos dentro.
from zipfile import ZipFile #para descomprimir


#variables globales
global salir
salir = False
global segundaOpcion
segundaOpcion  =0
global terceraOpcion
terceraOpcion  =0
global ruta
ruta= os.getcwd()   # coloque la direccion de su directorio, para probarlo en otros computadores.
#ruta=r'C:\Users\Angel\Desktop\\'

global extension #'.pdf','pptx'
global numDirectorios
numDirectorios=0 #Numero de directorios
global numArchivos
numArchivos=0#Numero de archivos
global rutaInicial
global nombreDirectorio



#funciones
def dameDirectorios(ruta):
    print('----------------------------------------')
    for a in listdir(ruta):
        if isdir(join(ruta,a)): #con esta condicion, me mostrara puros directorios de la ruta 
            print(a)
    print('----------------------------------------')            
def listaTodo(ruta):
    print('----------------------------------------')
    for a in listdir(ruta):
        
        print(a)   
    print('----------------------------------------') 
def listame_archivos(ruta,extension): #pdf
    a=''
    global archivosConExtension
    archivosConExtension=[]
    print('----------------------------------------')

    for a in listdir(ruta):
        if isfile(join(ruta,a)):
            if extension =='': #para listar todo
                print(a)
            else:
                punto = a.find(".")
                longitud = len(a) #tamaño de la cadena
                exten = a[punto+1:longitud]

                if exten == extension: #para listar con una extension en especifica 'pdf'
                    archivosConExtension.append(a)
                    #[libro.pdf,retos.pdf,]
                    print(a)
    print('----------------------------------------')
def muestra_archivo(ruta,nombre,nombreOriginal):
    a=''
    for a in listdir(ruta):
        if isfile(join(ruta,a)):
            if a == nombre:
                print('El nombre del archivo ',nombreOriginal,' fue modificado a : ',nombre)

def listarArchivosDirectorios():
    segundaOpcion = int(input('\n\tLISTAR\n1. Listar todo\n2. Ingresa una extension en especifico\nOpcion--> '))
    if(segundaOpcion ==1):
        listaTodo(ruta)

    elif(segundaOpcion ==2):
        extension = (input('Extension: '))  
        listame_archivos(ruta,extension.lower())

    else:
        print('Opcion invalida')

def existeArchivoDirectorio(nombreOriginal,rut,num):
    if num==1:

        if os.path.isfile(rut+'\\'+nombreOriginal):
            #print("Sí es un archivo")

            return True
        else:
            #print("No es archivo, o no existe")
            return False
    if num==3:
        if os.path.isdir(rut): #para saber si una ruta existe o no

            return True
        else:

            return False
            #1 -->archivos
    else: #2 -->directiors

        if os.path.isdir(rut+'\\'+nombreOriginal):
            #print("Sí es una carpeta")
            return True
        else:
            #print("No es una carpeta o no existe")
            return False

def cambiarNombre():
    #ruta= os.getcwd() 
    global ruta
    segundaOpcion = int(input('\n\tRENOMBRAR\n1. Archivos\n2. Directorios\nOpcion--> '))
    if(segundaOpcion ==1):
        extension=''    
        listame_archivos(ruta,extension) #mostrare los elementos que tengo en el directorio,para que el usuario vea y sepa cual cambiar
        nombreArchivo = (input('\nNombre del archivo : '))
        nuevoNombreArchivo = (input('Nuevo nombre del archivo : '))
        if(existeArchivoDirectorio(nombreArchivo,ruta,segundaOpcion)):

            os.rename(ruta+'\\'+nombreArchivo,ruta+'\\'+nuevoNombreArchivo)
            muestra_archivo(ruta,nuevoNombreArchivo,nombreArchivo)            
        else:
            print('Archivo no existe')
    elif(segundaOpcion ==2):
        dameDirectorios(ruta)
        NombreDirectorio=(input('Nombre del directorio : '))
        if(existeArchivoDirectorio(NombreDirectorio,ruta,segundaOpcion)):

            nuevoNombreDirectorio=(input('Nuevo nombre del directorio : '))
            os.rename(ruta+'\\'+NombreDirectorio,ruta+'\\'+nuevoNombreDirectorio)
            print("cambio efectuado")
        else:
            print("No es un directorio o no existe")

    else:
        print('Opcion invalida')    

def moverDirectorioArchivo():
    global ruta
    segundaOpcion = int(input('\n\tMOVER DE UBICACION\n1. Archivo\n2. Directorio\nOpcion--> '))
    print('Ejemplo --> C:\disco\programas')
    if(segundaOpcion ==1):
        extension=''
        #listame_archivos(ruta,extension) #muestro los archivos
        rutaInicial = (input('Ingresa la ruta inicial del archivo : '))        
        nombreArchivo=''

        if(existeArchivoDirectorio(nombreArchivo,rutaInicial,3)):
            listame_archivos(rutaInicial,extension)
            nombreArchivo = (input('Nombre de archivo a mover : '))
            rutaAmover = (input('Ingresa la ruta destino del archivo : '))
            if(existeArchivoDirectorio(nombreArchivo,rutaAmover,3)):
               # print('si existe')
                #vamos a hacer el movimiento
                shutil.move(rutaInicial+'\\'+nombreArchivo, rutaAmover+'\\'+nombreArchivo)
                print('Movimiento efectuado!!')
            else:
                print('No existe la ruta de destino ingresada')
        else:
            print('Archivo o ruta no existe')
        
    elif(segundaOpcion ==2):

        extension=''
        #listame_archivos(ruta,extension) #muestro los archivos
        rutaInicial = (input('Ingresa la ruta inicial del directorio : '))        #Y:\EXAMEN-COMPUTACION
        nombreArchivo='' 
        if(existeArchivoDirectorio(nombreArchivo,rutaInicial,3)):
            dameDirectorios(rutaInicial)       
            nombreDirectorio = (input('Nombre del directorio a mover : '))
            rutaAmover = (input('Ingresa la ruta destino del directorio : '))  
            if(existeArchivoDirectorio(nombreArchivo,rutaAmover,3)):
                #print('si existe')
                #vamos a hacer el movimiento
                shutil.move(rutaInicial+'\\'+nombreDirectorio, rutaAmover+'\\'+nombreDirectorio)
                print('Movimiento efectuado!!')
            else:
                print('No existe la ruta de destino ingresada')
        else:
            print("No es un directorio o no existe")    
    else: #3
    
        print('Opcion invalida')   

def crearDirectorio():
    global ruta
    global rutaInicial
    rutaInicial=''
    global nombreDirectorio
    nombreDirectorio=''
    print('\n\tCREAR DIRECTORIO')
    rutaInicial = (input('Ingresa la ruta donde se creara el directorio : ')) 
    extension=''
    nombreArchivo='' 
    if(existeArchivoDirectorio(nombreArchivo,rutaInicial,3)):
        #si existe la ruta
        nombreDirectorio = (input('Nombre del directorio a crear : ')) #eliminar3
        try:
            os.mkdir(rutaInicial+'\\'+nombreDirectorio)
            print('Directorio creado')
        except OSError as e:
            print('Directorio existente')
            if e.errno != errno.EEXIST:
                raise
    else:
        print("No existe la ruta!")  

def evaluarEliminacion(terceraOpcion,segundaOpcion,ruta):
    cantidadEliminar =0
    index=0
    if(segundaOpcion ==1):
        #archivos
        if terceraOpcion ==1: #para eliminar un solo archivo
            archivoEliminar = (input('Nombre del archivo a eliminar : '))
            try:               
                send2trash.send2trash(ruta+'\\'+archivoEliminar)
                print('Archivo eliminado')
            except OSError as e:
                print(f"Error:{ e.strerror}")

        else:#para eliminar varios archivos
            cantidadEliminar = int((input('Numero de archivos a eliminar :  '))) #3
            index=cantidadEliminar
            cantidadElementos(ruta) #saber cuantos elementos(archivos y directorios) tiene mi ruta
            cantidadArchivos = numArchivos 
            if cantidadArchivos<cantidadEliminar:
                print('No puedes eliminar mas archivos de los que existen')
            else:
                #listaArchivosEliminar = []
                while (cantidadEliminar>0):
                    archivoEliminar = (input('Nombre del archivo a eliminar : '))
                    if(existeArchivoDirectorio(archivoEliminar,ruta,segundaOpcion)):        
                        send2trash.send2trash(ruta+'\\'+archivoEliminar)
                        cantidadEliminar-=1 #disminuye en 1
                    else:
                        print('Nombre de archivo no existe')

                print(index,' archivos fueron eliminados')

    else:
        #directorios
        if terceraOpcion ==1: #un solo directorio
            directorioEliminar = (input('Nombre del directorio a eliminar : '))
            try:               
                send2trash.send2trash(ruta+'\\'+directorioEliminar)
                print('Directorio eliminado')
            except OSError as e:
                print(f"Error:{ e.strerror}")
        else: #varios directorios
            cantidadEliminar = int((input('Numero de directorios a eliminar :  ')))#3
            index=cantidadEliminar
            cantidadElementos(ruta) #sabre cuantos elementos(archivos y directorios) tiene mi ruta
            cantidadArchivos = numDirectorios #10
            if cantidadArchivos<cantidadEliminar:
                print('No puedes eliminar mas Directorios de los que existen')
            else:
                while(cantidadEliminar>0):
                    directorioEliminar = (input('Nombre del archivo a eliminar : '))
                    if(existeArchivoDirectorio(directorioEliminar,ruta,segundaOpcion)):        
                        send2trash.send2trash(ruta+'\\'+directorioEliminar)
                        cantidadEliminar-=1
                    else:
                        print('Nombre de archivo no existe')

                print(index,' archivos fueron eliminados')

def cantidadElementos(ruta):
    global numDirectorios
    global numArchivos
    numArchivos=0
    numDirectorios=0
    for a in listdir(ruta):
        if isfile(join(ruta,a)): #es arichivo
            numArchivos+=1
            #print('ARCHIVOS: ',numArchivos)
        else: #es directorio
            #print('ARCHIVOS: ',numArchivos)
            numDirectorios+=1
    #print('ARCHIVOS: ',numArchivos)
    #print('Directorios: ',numDirectorios)

def borrarArchivosDirectorios():
    global ruta
    segundaOpcion = int(input('\n\tBORRAR-ARCHIVOS-DIRECTORIO\n1. Archivos\n2. Directorios\nOpcion--> '))
    if(segundaOpcion ==1):
        extension=''
        listame_archivos(ruta,extension)
        terceraOpcion = int(input('1. Archivo\n2. Archivos\nOpcion--> '))
        
        if (terceraOpcion >0 and terceraOpcion <3):
            evaluarEliminacion(terceraOpcion,segundaOpcion,ruta)
        else:
            print('Opcion invalida')

    elif(segundaOpcion ==2):
        dameDirectorios(ruta)
        terceraOpcion = int(input('1. Directorio\n2. Directorios\nOpcion--> '))
        if (terceraOpcion >0 and terceraOpcion <3):
            evaluarEliminacion(terceraOpcion,segundaOpcion,ruta)
        else:
            print('Opcion invalida')

    else:
        print('Opcion invalida')

def crearZip():
    global ruta 
    segundaOpcion = int(input('\n\tCREAR ZIP\n1. Lista de archivos\n2. Directorio\nOpcion--> '))
    if(segundaOpcion ==1):
        evaluarZip(segundaOpcion,ruta)
                
    elif(segundaOpcion ==2):

        evaluarZip(segundaOpcion,ruta)
    else:
        print('Opcion invalida')    
def evaluarZip(segundaOpcion,ruta):
    if(segundaOpcion ==1):
        extension = (input('Ingresa extension de archivos para agregar a un Zip : ')) #pdf #pptx
        listame_archivos(ruta,extension)

        nombreZip = input('Ejemplo de nombres de archivos .Zip--> elementos.zip\nNombre del Zip: ') #solodocumentos.zip
        if(not existeArchivoDirectorio(nombreZip,ruta,segundaOpcion)):
            with zipfile.ZipFile(nombreZip,'w') as archivoZip:
                for i in archivosConExtension:#(ya tengo todos los archivos con extension especifa(pdf))  i=c:\direc\carta.pdf
                    archivoZip.write(i)

            archivoZip.close()
        else:
            print('Nombre de Zip, ya existente, usa otro!')

    else:

        dameDirectorios(ruta) #mostrar al usuario los directorios que existen
        nombreDirectorio = (input('Ingresa nombre de directorio a comprimir: '))
        nombreDirectorioZip = (input('Ingresa nombre de directorio : ')) #nuevo

        if(existeZip(ruta,nombreDirectorioZip)):
            #with zipfile.ZipFile(nombreDirectorio,'w') as archivoZip:
            #archivoZip.write(nombreDirectorio)

            archivoZip = shutil.make_archive(nombreDirectorioZip, "zip",ruta+ "\\",nombreDirectorio)
            print("Creado el directorio comprimido:", nombreDirectorioZip)


        else:
            print('Nombre de Zip, ya existente, usa otro!')

def existeZip(ruta,nombreZip):
    x=0
    punto2=nombreZip.find(".")
    nombreZip=nombreZip[0:punto2]
    #print(nombreZip)    
    for a in listdir(ruta):
        if isfile(join(ruta,a)):
            punto = a.find(".")
            nombre = a[0:punto]

            longitud = len(a) #tamaño de la cadena
            exten = a[punto+1:longitud]
            #print(exten)
            #print(nombre)

            if exten == 'zip' and nombre ==nombreZip :
                x=1
                #print(exten)
                #print(nombre)
                #print(a)
    if x==1:
        return False
    else:
        return True

def evaluarDescomprimirZip(segundaOpcion,ruta):
   
    extension='zip'
    listame_archivos(ruta,extension)
    zipDescomprimir = input('Ejemplo de nombres de archivos .Zip--> nombreZip.zip\nNombre de zip a descomprimir : ')
    if (not existeZip(ruta,zipDescomprimir)):
        if segundaOpcion==1:
            with ZipFile(ruta+'\\'+zipDescomprimir, 'r') as zip:
                zip.extractall()   #extraer todo
                print('Archivo descomprimido')           
        else:
            #print('Opcion2')
            #crear nuevo directorio
            crearDirectorio() #creo otro nuevo directorio
            rutaOp=rutaInicial+'\\'+nombreDirectorio+'\\' #-> 'C:\programa\directorio'
            with ZipFile(ruta+'\\'+zipDescomprimir, 'r') as zip:
                zip.extractall(rutaOp)  #especifico la ruta donde voy a descomprimir el .zip
                print('Archivo descomprimido')
    else:
        print('Archivo .zip no existe!')

def descomprimeZip():
    global ruta 
    segundaOpcion = int(input('\n\tDESCOMPRIMIR ZIP\n1. En el directorio actual\n2. Crear nuevo directorio y descomprimir alli\nOpcion--> '))
    if(segundaOpcion ==1):
        evaluarDescomprimirZip(segundaOpcion,ruta)
                
    elif(segundaOpcion ==2):
        evaluarDescomprimirZip(segundaOpcion,ruta)
        
    else:
        print('Opcion invalida')    

def evaluarDirectorioActual(segundaOpcion):
    global ruta
    if(segundaOpcion ==1):
        print('Directorio actual donde esta el usuario: ',os.getcwd()) 
        
    else: #2
        #cambiarse de directorio
        nuevaRutaDirectorio = (input('Ingresa nueva ruta de directorio: ')) #Y:\EXAMEN-COMPUTACION
        #nombreOriginal,rut,num
        if(existeArchivoDirectorio('',nuevaRutaDirectorio,3)):
            #ruta si existe y ahora debemos hacer el cambio
            #print('Si existe') 
            #actualizo la nueva ruta
            os.chdir(nuevaRutaDirectorio) #se actualiza la nueva ruta
            print('Directorio actual donde esta el usuario: ',os.getcwd())
            ruta = os.getcwd()

        else:
            print('No existe la ruta ingresada')  

def directorioActual():
    global ruta 
    segundaOpcion = int(input('\n\tDIRECTORIO-ACUTAL-CAMBIARSE\n1. Mostrar directorio actual\n2. Cambiarse de directorio \nOpcion--> '))
    if(segundaOpcion ==1):
        evaluarDirectorioActual(segundaOpcion)
                
    elif(segundaOpcion ==2):
        evaluarDirectorioActual(segundaOpcion)
    else:
        print('Opcion invalida')      

    
def evaluarMenu(op): #3
    if op == 1:
        listarArchivosDirectorios()

    elif op == 2:
        cambiarNombre()
        
    elif op == 3:
        moverDirectorioArchivo() 
        
    elif op == 4:
        crearDirectorio()
        
    elif op == 5:
        borrarArchivosDirectorios()
        
    elif op == 6:
        crearZip()
        pass
    elif op == 7:
        descomprimeZip()
        pass
    elif op == 8:
        directorioActual() 
        pass
    elif op == 9:
        salirDelPrograma()

    else:
        print('opcion Invalido')


def salirDelPrograma():
    global salir
    salir = True
    print("Saliste del programa! ")

def dameMenu():
    global opcion
    print("\n\tMENU\n1. Listar los archivos en un directorio\n2. Renombrar archivo o directorios\n3. Mover de ubicación un archivo o directorio \n4. Crear directorios .\n5. Borrar archivos o directorios y enviarlos a la papelera de reciclaje\n6. Crear un archivo zip a partir de una lista de archivos o de un directorio X. \n7. Descomprimir un archivo zip  \n8. Mostrar el directorio actual y permitir cambiarse de directorio\n9. Salir")
    opcion = int(input("Opcion ->  "))

if __name__ == '__main__':
    while not salir:

        dameMenu()
        evaluarMenu(opcion)



