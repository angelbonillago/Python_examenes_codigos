'''
Realizar un procedimiento que invierta el orden de la cola. Lo mismo para una pila y una lista.
'''

cola = ["Angel", "Benjamin", "Maria", "Jose","Jesus"]

print("\nEl contenido actual de la cola es: ",cola)
print("\nEl contenido de la cola invertida es: ", tuple(reversed(cola)))

pila = [1,2,3,4,5,6,7,8,9]

print("\nEl contenido actual de la pila es: ",pila)
print("\nEl contenido de la pila invertida es: ", tuple(reversed(pila)))

lista = ["Eduardo", 1, "Juan", 5, "Almendra", 9, "Lunes",20,"Saturno"]

print("\nEl contenido actual de la lista es: ",lista)
print("\nEl contenido de la lista invertida es: ", tuple(reversed(lista)))