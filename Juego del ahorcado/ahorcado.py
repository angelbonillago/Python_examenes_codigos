global numLetras
numLetras=0
numIntentos=5
palabras=''
salir=False
palabra=""
destFile = r"Y:\\Python-codigo\\versionPython\\ahorcado\\archivos.txt"
#Y:\Python-codigo\versionPython\ahorcado\archivos.txt
letrasAdivinadas=[]
import random

def asignarPalabra():
    global numLetras
    global palabra
    with open(destFile) as myfile:
        count = sum(1 for line in myfile) #Numero de palabras que tiene el archivo

    palabras = open(destFile,'r').read().split('\n') #obtener la lista de palabras en una lista

    #Ahora elegiremos una al azar.
    azar = random.randint(0, count-1)#se genera el aleatorio para tomar la posicion del archivo

    palabra=palabras[azar] #Se tiene ya la palabra que el usuario debera encontrar
    numLetras=len(palabra)

    #print('La palabra es : ',palabra)
    #print('La palabra tiene : ',numLetras, ' letras ')



if __name__ == '__main__':
    asignarPalabra()
    print('\t\tBIENVENIDO AL JUEGO AHORCADO\nTienes 5 vidas--ADIVINA LA PALABRA\nLa palabra tiene ',numLetras, ' letras ')
    print('_ ' * len(palabra)) #Lineas para la cantidad total de letras
    while not salir:
        #print('La palabra es : ',palabra)
        letra = input("Adivina una letra: ")
        if(len(letra)!=1 and letra.isnumeric()):
            print("Ingresa solo una letra!!!")
        else:
            if letra.lower() in letrasAdivinadas:
                print("letra repetida,sigue jugando")
            else:
                letrasAdivinadas.append(letra) #agregamos a la lista, para controlar letras ingresadas repetidas
 
                if letra.lower() in palabra:
                    print("Letra acertada") 
                    
                else:
                    numIntentos = numIntentos-1
                    print("Letra no encontrada, perdiste un intento")
                    print("Te quedan " + str(numIntentos) + " intentos")
                    
        avance = ""
        contadorLetrasFaltante = 0
        for letra in palabra:
            if letra in letrasAdivinadas:
                avance = avance + letra
            else:
                avance = avance + "_ "
                contadorLetrasFaltante = contadorLetrasFaltante + 1  
        print(avance) #Se muestra el avance del jugador
    
    
        if contadorLetrasFaltante == 0:
            print("Felicitaciones!!! Haz acertado\nLa palabra es: ",palabra)
            salir=True #Salimos del programa
        elif numIntentos==0:
            print("GAME OVER\nLa palabra que debias encontrar fue: ",palabra)
            salir=True #Salimos del programa
            
        
        