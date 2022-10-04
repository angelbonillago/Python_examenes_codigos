conjunto =set()
conjunto ={1,2,3,4,5,'Holaz',56.6}

if(1 in conjunto):
    print("1 si se encuentra")
if(1 not in conjunto):
    print("1 si se encuentra")

conjunto.add(5)
conjunto.add(15) #agregar

conjunto.discard(15) #quitar el 15
conjunto.clear() #elminar todo el conjunto
print(conjunto)

a={2,4,6,7}
b={1,5,6,8}
c = a|b #union de dos conjuntos
c =a&b #interseccion
c=a-b #diferencia
c=a^b #diferencia simetrica
print(c)

d={1,2,3,4,5,6,7,8,9}
print(a.issubset(d)) #subconjunto
print(d.issubset(a)) #si d es el superconjunto de a

print(a.isdisjoint(b))#si a es disconection de b, osea si no comparten ningun elemento