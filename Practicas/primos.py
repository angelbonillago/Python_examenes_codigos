#Programa que muestra los numeros primos
#Modificado por BONILLA GONZALEZ
#CODIGO : 162340B
#---------------------------------------
#función primo
def primo(n):

    c=0
    for i in range(1,n+1):
        if n%i==0:
            c=c+1
    if c>2:
        return False
    else:
        return True



if __name__ == '__main__':
#Programa que lista primos en un rango
    a=int(input('Desde: '))
    b=int(input('Hasta: '))
    for n in range(a,b+1):
        if primo(n):
            print('Número primo: ',n)