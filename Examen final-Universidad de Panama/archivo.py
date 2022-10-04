import os
salir = False
global archivo
"""
global nombre
nombre =""
global edad
edad=0
global numMedalla
numMedalla=0
"""
global valor
valor = False
def crearArchivo():
    global archivo
    archivo=open("Y:\\trabajito\\versionPython\\archivosPython\\prueba.txt","w")
    if(os.path.isfile("prueba.txt")):
        print("Existe el archivo")
    else:
        print("No se encontró el archivo")
    
def ingresarData():
    global nombre
    global edad
    global numMedalla
    nombre = input("Ingresa nombre : ")
    edad = int(input("Ingresa edad : "))
    numMedalla=int(input("Ingresa medalla : "))

def guardarDatos():

    if archivoVacio():
        archivo=open("Y:\\trabajito\\versionPython\\archivosPython\\prueba.txt","w")
        archivo.write(nombre+",")
        archivo.write(str(edad)+",")
        archivo.write(str(numMedalla)+"\n")            

    else:
        archivo=open("Y:\\trabajito\\versionPython\\archivosPython\\prueba.txt","a")
        archivo.write(nombre+",")
        archivo.write(str(edad)+",")
        archivo.write(str(numMedalla)+"\n")   


def readinputdata():
    archivo=open("Y:\\trabajito\\versionPython\\archivosPython\\prueba.txt","r")
    #fichero=open(openx,'r')   
    lineas=archivo.readlines()
    print(lineas)
    #print(lineas[0])
    print(lineas[1])

    cadena=[]

    for line in lineas:
        cadena=list(line)
        print(cadena) 




    

 
def archivoVacio():
    
    tamano = os.path.getsize("prueba.txt")
    if(tamano ==0):
        valor =True
        return valor
    else: 
        valor =False
        return valor
# Entrada de Datos
"""
data=readinputdata("fichero.dat")
 
columna=data[:,1]
print (columna)

"""
if __name__ == '__main__':
    crearArchivo()
    print(archivoVacio())
    ingresarData()
    guardarDatos()
    ingresarData()
    guardarDatos()
    ingresarData()
    guardarDatos()
    print(archivoVacio())
    (readinputdata())
   # while not salir:
    #    dameMenu()
     #   evaluarMenu(opcion)



