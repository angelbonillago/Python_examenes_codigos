"""
     País con mayor número de medallas. (Listar por Deporte y tipo de medalla la Cantidad de 
    medallas obtenidas) 

"""

print("\PAIS-MAYOR-MEDALLAS\n")
archivo="Y:\\trabajito\\versionPython\\archivosPython\\miarchivo.txt"
 #palabra='italia'
f = open(archivo)
lines = f.readlines()
#palabra = 'PERU'
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
    while(iterar>0):

        diccionarioCursos[ide][index] = int(diccionarioCursos[ide][index])
        iterar-=1
        index+=1
#print('Los numeros : ', diccionarioCursos)

for ide,value in diccionarioCursos.items():
    #print(ide)
    lista = diccionarioCursos[ide]
    #print('list',lista)
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






