"""
2. Definir una función que convierta grados Farenheit en grados Centígrados
"""

def convertir_Farenheit_centigrados(grados):
    return ((grados - 32) * 5.0/9.0)

if __name__ == '__main__':
    farenheit =float(input('Ingresa la temperatura en grados Farenheit a convertir : '))
    celsius=convertir_Farenheit_centigrados(farenheit)
    print('La conversion a grados Centígrados es : ',celsius)