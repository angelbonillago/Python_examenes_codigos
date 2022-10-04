"""if __name__ == '__main__':
   
    litsageneral=[]
    scores=[]
    iterador= int(input("Ingresa un numero entre 2 y 5: "))
    if (iterador>=2 and iterador <=5):
        for x in range(iterador):  
            name = input("Escribe tu nombre: ")
            score = float(input("Nota:  "))
            litsageneral.append([name])
            litsageneral[x].append(score)
            scores.append(score)

        print("--------------------\n",litsageneral)

    minEscore = min(scores)
    print((minEscore))

    print(type(minEscore))
    cuentala=0
    primerNombre=""
    for x in range(len(litsageneral)):
        for y in range(len(litsageneral[x])):
            print(litsageneral[x][y])
            if(minEscore==litsageneral[x][y]):
                cuentala=cuentala+1
                primerNombre = litsageneral[x][y-1]
                #print("ingreso")
                #print("Nombre unico menor",primerNombre)
    if cuentala==1:
        numerosegundo = 0
        print("primer nombre con puntaje bajo",primerNombre)
        scores.remove(minEscore)
        #print(scores)
        numerosegundo=min(scores)

        indice = scores.index(numerosegundo)
        #print(type(indice))
        #print("el indice el segundo menor es ",indice)
#       #numero a comparar
        nuevo = scores[indice]
        nuevo2=int(nuevo)
        #print(type(nuevo2))
        #print("numero a comparar",nuevo2)
        nuevoContador=0
        numero_menor2=""
        for x in range(len(litsageneral)):
            for y in range(len(litsageneral[x])):
                nuevoContador
                if(nuevo2==litsageneral[x][y]):
                    nuevoContador=nuevoContador+1
                    numero_menor2=litsageneral[x][y-1]
                if(nuevoContador>1):
                    print("segundo nombre con puntaje bajo",numero_menor2)
                else:
                    



        print("segundo nombre con puntaje bajo",litsageneral[x][y-1])
    else:
        pass
"""

a = [[ input("Nombre: "), float(input("puntaje: "))] for i in range(int(input("cantidad: ")))]
print(a)
s = sorted(set([x[1] for x in a]))
print(s)
for name in sorted(x[0] for x in a if x[1] == s[1]):
    print (name)





