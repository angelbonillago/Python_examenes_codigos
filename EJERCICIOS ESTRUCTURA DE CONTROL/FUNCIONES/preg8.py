"""
8. Define una función llamada raíz_n_esima que devuelve el valor de n√𝑥.
(Nota: recuerda que n√𝑥 es 𝑥1⁄𝑛).

"""

def raíz_n_esima(n,x):
    exponente = float(1/n)
    return pow(x,exponente)
    


if __name__ == '__main__':
    print('Valor de n√𝑥 ')
    n =int(input('Ingresa n : ')) 
    x =int(input('Ingresa x :  '))     
    raiz= raíz_n_esima(n,x)
    print('La raiz-enesima es: ',raiz)
