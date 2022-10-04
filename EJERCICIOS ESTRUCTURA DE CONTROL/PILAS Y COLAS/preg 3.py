'''
Realizar un procedimiento que saque el elemento N de la cola. Lo mismo para una pila y una lista. Tener en cuenta que los mismos elementos deben quedar en el mismo orden
'''

cola = ["Angel", "Benjamin", "Maria", "Jose","Jesus"]

print("\nEl contenido actual de la cola es: ",cola)

#Quitamos elementos por el principio de la cola (Primero en entrar - Primero en salir)

x = cola.pop(0)

print("\nEl elemento quitado de la cola es: ",x)
print("\nEl contenido de la cola quitando el primer elemento es: ", cola)
print("\n############################################################################################################################################################")

pila = [1,2,3,4,5,6,7,8,9]

print("\nEl contenido actual de la pila es: ",pila)

#Quitamos elementos por el último de la pila (Último en entrar - Primero en salir)

y = pila.pop()

print("\nEl elemento quitado de la pila es: ",y)
print("\nEl contenido de la pila quitando el último elemento es: ", pila)
print("\n############################################################################################################################################################")

lista = ["Eduardo", 1, "Juan", 5, "Almendra", 9, "Lunes", 20,"Saturno"]

print("\nEl contenido actual de la lista es: ",lista)

#Podemos quitar cualquier elemento de la lista, en este caso sería Almendra.

z = lista.pop(4)

print("\nEl elemento quitado de la lista es: ", z)
print("\nEl contenido de la lista quitando el elemento es: ", lista)