"""
4. Define una función que convierta grados en radianes

"""
import math

def conviertir_grados_radianes(grad):
    return (grad*(math.pi/180))

if __name__ == '__main__':
    grados =float(input('Ingresa los grados a convertir : ')) #180
    radianes=conviertir_grados_radianes(grados)
    print('La conversion a grados es : ',radianes)