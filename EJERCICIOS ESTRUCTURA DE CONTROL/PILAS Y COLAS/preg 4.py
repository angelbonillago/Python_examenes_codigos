'''
Realizar un procedimiento que ingrese un elemento en la posición N de la cola. Lo mismo para una pila y una lista. Tener en cuenta que los mismos elementos deben quedar en el mismo orden
'''

cola = ["Angel", "Benjamin", "Maria", "Jose","Jesus"]

print("\nEl contenido actual de la cola es: ",cola)

#Agregamos elementos a la cola (Primero en entrar - Primero en salir) En este caso ingresaremos al principio.

cola.append("Lucas")

print("\nEl contenido de la cola agregando al primer elemento es: ", cola)
print("\n############################################################################################################################################################")

pila = [1,2,3,4,5,6,7,8,9]

print("\nEl contenido actual de la pila es: ",pila)

#Agregamos elementos por el último de la pila (Último en entrar - Primero en salir)

pila.append(10)

print("\nEl contenido de la pila agregando el elemento es: ", pila)
print("\n############################################################################################################################################################")

lista = ["Eduardo", 1, "Juan", 5, "Almendra", 9, "Lunes", 20,"Saturno"]

print("\nEl contenido actual de la lista es: ",lista)

#Podemos agregar cualquier elemento de la lista, en este caso sería Almendra.

lista.append(25)

print("\nEl contenido de la lista agregando el elemento es: ", lista)