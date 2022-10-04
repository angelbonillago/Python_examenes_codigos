def cursoMatriculadoEstudiante():
    diccionarioAlumnos ={'1':['-','ninja'],'2':['-','paolo'],'3':['-','andy'],'4':['-','piter']}
    alumnoMatriculado={'2': [[1, '-'], [4, '-']],'1':[[1,'-']],'3':[[2,'-']]}
    diccionarioCursos={'1':['Logica'],'2':['computacion'],'3':['Redes'],'4':['linux']}
    identificacionEstudiante =(input("Identificacion del Estudiante : "))
    print("CURSOS-POR-ALUMNO\n")
    print("El alumno ",diccionarioAlumnos[identificacionEstudiante][1]," esta matriculado en los cursos : ")

    for ide,value in alumnoMatriculado.items():
        iterando =0
        #print('cantidad de cursos : ',cantidad)
        if(identificacionEstudiante==ide):
            cantidad=len(alumnoMatriculado[ide])
            while(cantidad>0): 
                x = ((alumnoMatriculado[ide][iterando][0])) #tengo el codigo de curso
                parseo = str(x)
                print(diccionarioCursos[parseo][0])
                iterando +=1
                cantidad -=1

def cursosDictaProfesor():
        #datos = [nombre, apellido,direccion,telefono]
    diccionarioCursos={'1':['Logica',23,'4','5',33,'1'],'2':['computacion',25,'4','5',33,'1'],'3':['Redes',23,'4','5',33,'2'],'4':['linux',23,'4','5',33,'2']}
    diccionarioProfesores={'1':['ANGEL','BONILLA','SAN MARTIN','98823231'],'2':['PEDRO','LOLO','PALMERAS','98852318'],'3':['PITER','CASTLE','LIBRE','9885248']}
    cedula= (input("Cedula del Profesor : "))
    print("El Profesor : ",diccionarioProfesores[cedula][0]," ",diccionarioProfesores[cedula][1],' dicta : ')
    #print(diccionarioCursos['1'][0])
    for ide,value in diccionarioCursos.items():
        x=diccionarioCursos[ide][5]
        if(cedula==x):
            print(diccionarioCursos[ide][0])
            

def actualizarNotas():
    alumnoMatriculado={'2': [[1, '-'], [4, '-']],'1':[[1,'-']],'3':[[2,'-'],[1,'-']]}
    #diccionarioCursos={'1':['Logica',23,'4','5',33,'1'],'2':['computacion',25,'4','5',33,'1'],'3':['Redes',23,'4','5',33,'2'],'4':['linux',23,'4','5',33,'2']}
    index =0
    for iden,value in alumnoMatriculado.items():
        identificacionEstudiante =(input("Identificacion del Estudiante : "))
        print('ESTUDIANTE CON IDENTIFICADOR ',identificacionEstudiante)
        cantidad=len(alumnoMatriculado[identificacionEstudiante])
        while(cantidad>0): 
                print('CURSO ',alumnoMatriculado[identificacionEstudiante][index][0])
                nota =int(input("Nota del curso : "))
                alumnoMatriculado[identificacionEstudiante][index][1]=nota
                index +=1
                cantidad -=1
        print('Los Notas actualizadas son : ',alumnoMatriculado)
        index=0
       

def ListCursosEstCalificaciones():
    diccionarioAlumnos ={'1':['-','ninja'],'2':['-','paolo'],'3':['-','andy'],'4':['-','piter'],'5':['-','Alonso']}
    alumnoMatriculado={'2': [[1, 12], [4, 10]],'1':[[1,17]],'3':[[2,13],[1,17]]}
    diccionarioCursos={'1':['Logica',23,'4','5',33,'1'],'2':['computacion',25,'4','5',33,'1'],'3':['Redes',23,'4','5',33,'2'],'4':['linux',23,'4','5',33,'2']}

    identificacionEstudiante =(input("Identificacion del Estudiante : "))
    print("Alumno ",diccionarioAlumnos[identificacionEstudiante][1])
    print("\nCURSOS  -  NOTA")
    index =0
    for ide,value in alumnoMatriculado.items():
        if(identificacionEstudiante==ide):
            cantidad=len(alumnoMatriculado[identificacionEstudiante])
            while(cantidad>0): 
                codigo= alumnoMatriculado[identificacionEstudiante][index][0]
                parse = str(codigo)
                print(diccionarioCursos[parse][0],' - ',alumnoMatriculado[identificacionEstudiante][index][1])
                index +=1
                cantidad -=1
            index=0

        
if __name__ == '__main__':
    #valor = 8
    #while valor > 0:
    ListCursosEstCalificaciones()
    #    valor = valor - 1
