"""
@author: Carlos
"""
import os

#variables globales

global ruta
ruta="Y:\\trabajito\\versionPython\\archivosPython\\miarchivo.txt" #al momento de ejecutarlo en otro computador, debera cambiar esta ruta por la suya
global salir
salir = False
global count
count =0
global listaDelArchivo
def registraAtleta():
    print("\tREGISTRA-ATELTA\n")
    global idAtleta
    global nombre
    global pais
    global edad
    global numMedalla
    global listaMedalla
    listaMedalla=[]
    idAtleta=(input("idAtleta :"))
    nombre = input("Ingresa nombre : ")
    pais=(input("Pais : "))
    deporte=(input("Deporte : "))
    numMedalla=int(input("Ingresa medalla : "))
    i=1
    if numMedalla >0:

        contador  = numMedalla
        while(contador>0):
            print('\tMedalla n° ',i,"\n")
            tipoMedalla=(input("Tipo de Medalla : ")) #bronce,plata,oro
            listaMedalla.append(tipoMedalla)
            contador -=1
            i +=1
            tipoMedalla=""

            StrA = ",".join(listaMedalla)
        guardarDatos(idAtleta,nombre,pais,deporte,numMedalla,StrA)

    else:
        numMedalla=0
        listaMedalla=[]
        guardarDatos(idAtleta,nombre,pais,deporte,numMedalla,listaMedalla)

def guardarDatos(ide,name,ps,depor,numM,listaM):

    if archivoVacio():
        archivo=open(ruta,"w")
        archivo.write(ide+",")
        archivo.write(name+",")
        archivo.write(ps+",")
        archivo.write(depor+",")
        archivo.write(str(numM)+",")
        archivo.write(str(listaM))

    else:
        archivo=open(ruta,"a")
        archivo.write("\n"+ide+",")
        archivo.write(name+",")
        archivo.write(ps+",")
        archivo.write(depor+",")
        archivo.write(str(numM)+",")
        archivo.write(str(listaM))


def archivoVacio():
    tamano = os.path.getsize("miarchivo.txt")
    if(tamano ==0):
        valor =True
        return valor
    else: 
        valor =False
        return valor
   
def medallaPorPais():
    """
    Consulta de Medallas obtenidas por un país X. 
    (Nombre del Atleta, Deporte y Cantidad de Medallas).
    """
    print("\MEDALLA-POR-PAIS\n")
    palabra=(input("Ingresa Pais : "))
    f = open(ruta)
    lines = f.readlines()
    print('PAIS : ',palabra)
    print("Nombre del Atleta\tDeporte\t\tCantidad de Medallas")
    for line in lines:
        palabras = line.split(',')
        #print(palabras)
        for p in palabras:
            if p==palabra:
                #print(palabras[4])
                cantMed = int(palabras[4])
                if(cantMed>=0):
                    print(palabras[1],"\t\t\t",palabras[3],"     \t   ",palabras[4])


def sumalista(listaNumeros):
   if len(listaNumeros) == 1:
        return listaNumeros[0]
   else:
        return listaNumeros[0] + sumalista(listaNumeros[1:])

def paisMayorMedallas():
    """
    País con mayor número de medallas. (Listar por Deporte y tipo de medalla la Cantidad de 
    medallas obtenidas)
    """ 
    print("\PAIS-MAYOR-MEDALLAS\n")
    f = open(ruta)
    lines = f.readlines()
    contador =0
    diccionarioCursos={}
    aux =()
    datos=[]
    listaCursos=[]
    for line in lines:
        palabras = line.split(',')
        #print(palabras)
        palabra=(palabras[2])
        totalMedalla=(palabras[4])

        if contador > 0:

            auxiliar = 0
            for i in diccionarioCursos:
                if i == palabra: # para ver si el mismo alumno se matriculara en otro curso
                    
                    diccionarioCursos[palabra].append(totalMedalla)
                    auxiliar = 1

            if auxiliar == 0: #para un nuevo alumno que no esta guardado

                datos=[totalMedalla]
                aux=(palabra,datos)
                listaCursos.append(aux)
                diccionarioCursos=dict(listaCursos)

        else:
            contador = contador + 1
            datos=[totalMedalla]
            aux=(palabra,datos)
            listaCursos.append(aux)
            diccionarioCursos=dict(listaCursos)

    #print('Los matriculados son : ', diccionarioCursos)
    del aux
        # del lista


    for ide,value in diccionarioCursos.items():
        iterar = len(diccionarioCursos[ide])
        index = 0
        while(iterar>0): #Convertir las cantidades de medalles de cada pais, de string a int

            diccionarioCursos[ide][index] = int(diccionarioCursos[ide][index])
            iterar-=1
            index+=1

    for ide,value in diccionarioCursos.items(): #con ka funcion 'sumalista', sumaremos toods los elementos de medallas que hayan para cada pais
        lista = diccionarioCursos[ide]
        print('PAIS : ',ide,' CON TOTAL DE MEDALLAS : ',sumalista(lista))
        print("Deporte\t\tCantidad de medallas\t\ttipo de medalla")
        for line in lines:
            palabras = line.split(',')
            #print(palabras)*
            if palabras[2]==ide:
                #print(palabras[4])
                cant_tipo_medalla = int(palabras[4])
                x=5
                texto=''
                while(cant_tipo_medalla>0):
                    texto =texto +','+palabras[x]
                    cant_tipo_medalla-=1
                    x+=1

                print(palabras[3],"\t\t\t",palabras[4],"\t\t\t",texto)  


def medallasPorAtletaPorDeporte():
        
    """ 
    Consultar las Medallas obtenidas por un Atleta X en un Deporte X
    """
    print("\MEDALLA-POR-ATLETA-DEPORTE\n")
    #archivo="Y:\\trabajito\\versionPython\\archivosPython\\miarchivo.txt"
    #palabra='italia'
    f = open(ruta)
    lines = f.readlines()
    mostrarAtletas()
    idAt=(input("idAtleta :"))
    deport=(input("Deporte : "))
    print('NOMBRE\t\tCantidad Medallas')
    for line in lines:
        palabras = line.split(',')
        #print(palabras)
        if palabras[0]==idAt and palabras[3]==deport:
            print(palabras[1],"\t\t\t","     \t",palabras[4])  

def listarPorDeporte():
    """ 
    5. Listar para un deporte X(atleta, país, tipo de medalla).
    """
    
    print("\LISTAR-POR-DEPORTE\n")
    mostrarAtletas()
    deport=input(("Ingresa Deporte : "))
    #archivo="Y:\\trabajito\\versionPython\\archivosPython\\miarchivo.txt"
    f = open(ruta)
    lines = f.readlines()
    print('NOMBRE\t\t\tPais\t\t\tTipo Medallas') 
    for line in lines:
        palabras = line.split(',')
        #print(palabras)*
        if palabras[3]==deport:
            #print(palabras[4])
            cant_tipo_medalla = int(palabras[4])
            x=5
            texto=''
            while(cant_tipo_medalla>0):
                texto =texto +','+palabras[x]
                cant_tipo_medalla-=1
                x+=1

            print(palabras[1],"\t\t\t",   palabras[2]  ,"    \t\t",texto)  


def mostrarAtletas():
    #archivo="Y:\\trabajito\\versionPython\\archivosPython\\miarchivo.txt"
    #palabra='italia'
    f = open(ruta)
    lines = f.readlines()
    contador =0
    print("ID del Atleta\t\tDeporte")
    for line in lines:
        palabras = line.split(',')
        print(palabras[0],"\t\t"," \t  ",palabras[3])
        

def evaluarMenu(op):

    if op == 1:
        registraAtleta()

    elif op == 2:
        medallaPorPais()
        
    elif op == 3:
        paisMayorMedallas() #falta
        
    elif op == 4:
        medallasPorAtletaPorDeporte()
        pass
    elif op == 5:
        listarPorDeporte()
        pass
    elif op == 6:
        salirDelPrograma()
   

    else:
        print('opcion Invalido')


def salirDelPrograma():
    global salir
    salir = True
    print("Saliste del programa! ")

def dameMenu():
    global opcion
    print("\n\tMENU-ACADEMIA\n1. Registro de Atletas\n2. Consulta de Medallas obtenidas por un país X. (Nombre del Atleta, Deporte y Cantidad de Medallas).\n3. País con mayor número de medallas. (Listar por Deporte y tipo de medalla la Cantidad de medallas obtenidas).\n4. Consultar las Medallas obtenidas por un Atleta X en un Deporte X.\n5. Listar para un deporte X(atleta, país, tipo de medalla).\n6. Salir\n")
    opcion = int(input("Opcion ->  "))

if __name__ == '__main__':
    while not salir:
        dameMenu()
        evaluarMenu(opcion)