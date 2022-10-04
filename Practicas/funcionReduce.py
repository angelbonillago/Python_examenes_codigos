from functools import reduce 

lista = ['h', 'o', 'l', 'a', '-', 'm', 'u', 'n', 'd', 'o',
         '--', 's', 'o', 'y', '-', 'A', 'n', 'g', 'e', 'l']
def concatenar(a, b):
    return a+b

resultado = reduce(concatenar, lista)
print(*resultado)
