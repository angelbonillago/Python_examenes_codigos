"""
Created on Fri Jun  4 19:26:12 2021
@author: Carlos
"""
# variables globales
global salir
salir = False
global lista
lista =[]
global listaCursos
listaCursos=[]
global listaProfesores
listaProfesores=[]
global listaMatriculados
listaMatriculados=[]

global auxiliar
auxiliar = 0
global contador
contador = 0
global x
x = ''

global alumnoMatriculado
alumnoMatriculado = {x: [lista]}
#

# funciones a usar
def evaluarMenu(op):

    if op == 1:
        registraAlumno()

    elif op == 2:

        registroEmpresa()

    elif op == 3:
        registroCursos()

    elif op == 4:
        registroProfesores()

    elif op == 5:
        matricularCurso()

    elif op == 6:
        actualizarNotas()
    elif op == 7:
        menuConsultas()

    elif op == 8:
        salirDelPrograma()

    else:
        print('opcion Invalido')

def salirDelPrograma():
    global salir
    salir = True
    print("Saliste del programa! ")

def dameMenu():
    global opcion
    print("\n\tMENU-ACADEMIA\n1. Registro de Alumnos\n2. Registro de Empresas\n3. Registro de Cursos\n4. Registro de Profesores\n5. Matricularse en curso \n6. Actualizar Notas\n7. Consultas\n8. Salir")
    opcion = int(input("Opcion ->  "))

def registraAlumno():
    print("\tREGISTRA-ALUMNO\n")
    aux=()
    global diccionarioAlumnos
    diccionarioAlumnos={}
    datos =[]
    identificacion=(input("Identificacion :")) #  '76743743'
    direccion=(input("Direccion : "))
    nombre=(input("Nombre : "))
    telefono=(input("Telefono : "))
    edad=int(input("Edad : "))  #'23'  -> 23
    datos = [direccion, nombre,telefono,edad]
    aux=(identificacion,datos)
    lista.append(aux)
    diccionarioAlumnos=dict(lista)
    print('Los datos son : ',diccionarioAlumnos)
    del aux
    del datos

def dameAlumnos():
    print("Identificacion\tNombre")
    for ident in diccionarioAlumnos:
        print(ident, "           ", diccionarioAlumnos[ident][1])

def dameCursos(): #mostrarme los cursos para que el alumo se matricule
    #cantidad=len(diccionarioCursos)
    print("Codigo-Curso\tNombre-Curso")
    for ident in diccionarioCursos:
        print(ident, "           ", diccionarioCursos[ident][0])

def registroEmpresa():
    
    print("\tREGISTRA-EMPRESA\n")
    dameAlumnos() 
    datos =[]#lista los alumnos
    iden = (input("Identificacion: "))
    #print('identificador a cambiar : ',iden)
    direcciónEmpresa=(input("Direccion Empresa: "))
    nombreEmpresa=(input("Nombre Empresa : "))
    teléfonoEmpresa=(input("Telefono Empresa : "))
    datos = [direcciónEmpresa,nombreEmpresa,teléfonoEmpresa]
    diccionarioAlumnos[iden].append(datos)


    print('Los datos con trabajo : ',diccionarioAlumnos)

def registroCursos():
    print("\tREGISTRA-CURSOS\n")
    global diccionarioCursos
    diccionarioCursos={}
    aux =()
    datos=[]
    codigoCurso = int(input("Codigo del curso : "))
    nombreCurso = (input("Nombre del curso : "))
    horasDuración =int(input("Horas del curso : "))
    fechaIinicio =(input("Fecha Inicio del curso : "))
    fechaFin =(input("Fecha Fin del curso : "))
    totalEstudiantes= int(input("Total de Estudiantes : "))
    cédulaProfesor=(input("Cedula de profesor : "))
    datos = [nombreCurso, horasDuración,fechaIinicio,fechaFin,totalEstudiantes,cédulaProfesor]
    aux=(codigoCurso,datos) 
    listaCursos.append(aux)
    diccionarioCursos=dict(listaCursos)
    print('Los Cursos son : ',diccionarioCursos)
    del aux
    del datos

def registroProfesores():
    global diccionarioProfesores
    diccionarioProfesores={}
    aux =()
    datos=[]
    cedula= (input("Cedula del Profesor : ")) 
    nombre= (input("Nombre del Profesor : "))
    apellido= (input("Apellido del Profesor : "))
    direccion= (input("Dieccion del Profesor : "))
    telefono= (input("Telefono del Profesor : "))
    datos = [nombre, apellido,direccion,telefono]
    aux=(cedula,datos) 
    listaProfesores.append(aux)
    diccionarioProfesores=dict(listaProfesores) #convertimos una lista a Dicc
    print('Los datos son : ',diccionarioProfesores)
    del aux
    del datos
    
def matricularCurso():

    global x
    # x=''
    global listaMatriculados
    # listaMatriculados=[]
    global lista
    # lista=[]
    global alumnoMatriculado
    # alumnoMatriculado={x:[lista]}
    global contador
    global auxiliar
    aux = ()
    datos = []
    print("\tMATRICULA\n")
    dameCursos()

    x = (input("Identificacion del Estudiante : "))
    codigoCurso = int(input("Codigo del curso : "))
    nota = "-"
    #print('contador ? ', contador)

    if contador > 0:
        #print('ya hay un alumno matriculado')
        #print('son : ', alumnoMatriculado)
        auxiliar = 0
        for i in alumnoMatriculado:
            #print('entro al for : ', i)
            if i == x: # para ver si el mismo alumno se matriculara en otro curso
                #print('Agregando curso a alumno con identificador: ', x)
                lista = [codigoCurso, nota]
                #print('Lista con indice igual ', lista)
                alumnoMatriculado[x].append(lista)
                auxiliar = 1

        if auxiliar == 0: #para un nuevo alumno que no esta guardado
            #print('entro al if del for')
            registro_curso = [codigoCurso, nota]
            lista_cursos = [registro_curso, ]
            #print('lista con indice difernte ', lista_cursos)
            aux = (x, lista_cursos)
            listaMatriculados.append(aux)
            alumnoMatriculado = dict(listaMatriculados)

    else:
        #print('Primer registro...')
        registro_curso = [codigoCurso, nota]
        lista_cursos = [registro_curso, ]
        #print('Lista', lista_cursos)
        aux = (x, lista_cursos)
        #print('aux', aux)
        listaMatriculados.append(aux)
        alumnoMatriculado = dict(listaMatriculados)
        contador = contador + 1

    print('Los matriculados son : ', alumnoMatriculado)
    del aux
    # del lista
   
def actualizarNotas():
    #identificacionEstudiante =(input("Identificacion del Estudiante : "))
    #codigoCurso =int(input("Codigo del curso : "))
    #nota =(input("Nota del curso : "))
    index =0
    for iden,value in alumnoMatriculado.items():
        identificacionEstudiante =(input("Identificacion del Estudiante : ")) #1
        print('ESTUDIANTE CON IDENTIFICADOR ',identificacionEstudiante)
        cantidad=len(alumnoMatriculado[identificacionEstudiante]) #4
        while(cantidad>0): 
            print('CURSO ',alumnoMatriculado[identificacionEstudiante][index][0])
            nota =int(input("Nota del curso : "))
            alumnoMatriculado[identificacionEstudiante][index][1]=nota
            index +=1
            cantidad -=1
        print('Los Notas actualizadas son : ',alumnoMatriculado)
        index=0

def menuConsultas():
    global consulta
    print("1. Consulta de Cursos matriculados por un estudiante X\n2. Curso con mayor número de estudiantes matriculados\n3. Cursos dictados por un profesor X\n4. Listado de Cursos Tomados por un Estudiante y sus calificaciones")
    consulta = int(input("Opcion ->  "))
    evaluarConsulta(consulta)

def evaluarConsulta(c):
    if c == 1:
        cursoMatriculadoEstudiante()

    elif c == 2:
        cursoMayorEstMatriculados()

    elif c == 3:
        cursosDictaProfesor()

    elif c == 4:
        ListCursosEstCalificaciones()

    else:
        print('opcion Invalido')

def cursoMatriculadoEstudiante():

    identificacionEstudiante =(input("Identificacion del Estudiante : "))
    print("CURSOS-POR-ALUMNO\n")
    print("El alumno ",diccionarioAlumnos[identificacionEstudiante][1]," esta matriculado en los cursos : ")

    for ide,value in alumnoMatriculado.items():
        iterando =0
        if(identificacionEstudiante==ide):
            #print("entra if")
            cantidad=len(alumnoMatriculado[ide]) #3
            while(cantidad>0): 
                #print("while-")
                x = ((alumnoMatriculado[ide][iterando][0])) #tengo el codigo de curso
                #parseo = str(x)
                print(diccionarioCursos[x][0])
                iterando +=1
                cantidad -=1 #2 #1 #0

def cursoMayorEstMatriculados():

    cursosRegistrados=[]
    contador=0
    count = 0
    iterar = 0
    index  =0
    listaValores=[]
    for key,value in diccionarioCursos.items():
        cursosRegistrados.append(key)
        #print(key)

    aux =()
    ideCursos=0
    cantcursosRegistrados=len(cursosRegistrados)
    #for k in range(cantcursosRegistrados):
    #print('cantidad de cursos registrados : ',cantcursosRegistrados)
    while(cantcursosRegistrados>0):
        idDelPrimerCurso=cursosRegistrados[ideCursos]
     #   print('ide del primer curso : ',idDelPrimerCurso)
      #  print('entro al while')
        for key,value in alumnoMatriculado.items():  #entre a los ide de los alumnos
            iterar=len(alumnoMatriculado[key]) #vere cuantos cursos matriculados tiene cada id-alumno
            #cantcursosRegistrados = len(cursosRegistrados)
       #     print('cantidad de cada ide.alumno: ',iterar)
        #    print('entro al for')
            while iterar > 0:
         #       print('entro al 2while')
          #      print('lista?',alumnoMatriculado[key][index][0])
                com = alumnoMatriculado[key][index][0]
                if(idDelPrimerCurso==com):
           #         print('entro al if')
                    contador+=1
                iterar -= 1 
                index += 1
            #print('salio del while')
            index =0
        #guardo cuantos alumnos tiene matriculados en el curso[i]
        cantcursosRegistrados -=1
        ideCursos +=1
        aux =(idDelPrimerCurso,contador)
        listaValores.append(aux)
        contador=0
    #print('cursos :  ',listaValores)

    mayor = listaValores[0][1]
    ide = 0
    #print('mayor de ',mayor)
    for key,value in listaValores:
        #print(value)
        if(mayor<value):
            mayor = value
            ide  = key
            
    print('el curso ',diccionarioCursos[ide+1][0],' tiene : ',mayor,'  alumnos')


def cursosDictaProfesor(): 
    cedula= (input("Cedula del Profesor : "))
    print("El Profesor : ",diccionarioProfesores[cedula][0]," ",diccionarioProfesores[cedula][1],' dicta : ')
    for ide,value in diccionarioCursos.items():
        x=diccionarioCursos[ide][5]
        if(cedula==x):
            print(diccionarioCursos[ide][0])

def ListCursosEstCalificaciones():
    identificacionEstudiante =(input("Identificacion del Estudiante : "))
    print("Alumno ",diccionarioAlumnos[identificacionEstudiante][1])
    print("\nCURSOS  -  NOTA")
    index=0
    for ide,value in alumnoMatriculado.items():
        if(identificacionEstudiante==ide):
            cantidad=len(alumnoMatriculado[identificacionEstudiante])
            while(cantidad>0): 
                codigo= alumnoMatriculado[identificacionEstudiante][index][0]
                #parse = str(codigo)
                print(diccionarioCursos[codigo][0],' - ',alumnoMatriculado[identificacionEstudiante][index][1])
                index +=1
                cantidad -=1
            index=0
       
if __name__ == '__main__':
    while not salir:
        dameMenu()
        evaluarMenu(opcion)
