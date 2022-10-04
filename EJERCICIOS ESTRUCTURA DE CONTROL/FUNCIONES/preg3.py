"""
3. Define una función que convierta radianes en grados. Recuerda que 360 grados son 2𝜋
radianes

"""
import math
def conviertir_radianes_grados(rad):
    return (rad*(180/math.pi))

if __name__ == '__main__':
    radianes =float(input('Ingresa los radianes a convertir : ')) # 3,14
    grados=conviertir_radianes_grados(radianes)
    print('La conversion a grados es : ',grados)