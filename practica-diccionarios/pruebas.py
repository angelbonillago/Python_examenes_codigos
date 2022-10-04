"""
x=''
lista=[]
aux=()
datoss=[]
dicionario ={x:[lista]}
contador =5
while(contador>0):
    x =(input("Clave : "))
    nota ='-'
    codCurso=(input("Codigo : "))

    lista =[codCurso,nota]
    aux=(x,lista)
    datoss.append(aux)
    dicionario=dict(datoss)
    #dicionario[x].append(lista)
    contador=contador-1

#dicionario ={'1': [[1, "-"]], '2': [2, '-']}
print(dicionario)

clave='1'

for i in dicionario:
    if(i==clave):
        datos = [2,"-"]
        dicionario[clave].append(datos)


print(dicionario[clave])
print(dicionario[clave][0][0])
global listaMatriculados
listaMatriculados=[]
"""

global auxiliar
auxiliar =0

global contador
contador =0 
global x
x=''
global lista
lista=[]
global alumnoMatriculado
alumnoMatriculado={x:[lista]}

global listaMatriculados
listaMatriculados=[]


def matricularCurso():

    global x
    #x=''
    global listaMatriculados
    #listaMatriculados=[]
    global lista
    #lista=[]
    global alumnoMatriculado
    #alumnoMatriculado={x:[lista]}
    global contador
    global auxiliar
    aux =()
    datos=[]
    print("\tMATRICULA\n")
    #dameCursos()

    x =(input("Identificacion del Estudiante : "))
    codigoCurso =int(input("Codigo del curso : "))
    nota ="-"
    print('contador ? ',contador)
    print('cantidad ? ',len(alumnoMatriculado))
    print('cuale es ?? ? ',(alumnoMatriculado))

    if contador >0:
        print('ya hay un alumno matriculado')
        print('son : ',alumnoMatriculado)

        for i in alumnoMatriculado:
            print('entro al for : ', i)
            if(i==x):
                print('entro al ifif')
                lista = [codigoCurso, nota]
                print('Lista con indice igual ',lista)
                alumnoMatriculado[x].append(lista)
                auxiliar=1  
        if auxiliar ==0:
            print('entro al if del for')
            lista = [codigoCurso, nota]
            print('lista con indice difernte ',lista)
            aux=(x,lista)
            listaMatriculados.append(aux)
            alumnoMatriculado=dict(listaMatriculados)
            
    else:
        print('entro al else')
        lista = [codigoCurso, nota]
        print('Listaaasa',lista)
        aux=(x,lista)
        listaMatriculados.append(aux)
        alumnoMatriculado=dict(listaMatriculados)
        contador=contador+1

    print('Los matriculados son : ',alumnoMatriculado)
    del aux
    #del lista



if __name__ == '__main__':
    valor =8
    while(valor>0):
        matricularCurso()
        valor=valor-1
