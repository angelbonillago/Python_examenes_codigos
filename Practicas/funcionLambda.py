# funcion lambda para el area de un triangulo:
def dameAreaTriangulo(base, altura):

    return (base*altura)/2


# La funcion lambda reduce codigo, ejemplo en el la linea 11

area_triangulo=lambda base, altura:(base*altura)/2


print(area_triangulo(50, 5))
print(area_triangulo(10, 2))
print(area_triangulo(50, 30))


alCubo = lambda numero:numero**3 
alcubo = lambda numero:pow(numero,3)

print(alCubo(5))
print(alCubo(4))
print(alCubo(3))




