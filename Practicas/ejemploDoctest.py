

import doctest


def areaTriangulo(base, altura):
    """Calcula el area de un triangulo dado



    """
    return (base*altura)/2


def compruebaEmail(emailUsuario):
    """
    La funcion comprueba Email, evalua un email recibido, en busca de la @.
    Si tiene una sola @, es correcto, si tiene mas @ y si tiene la @ a final, es incorrecto

    >>> compruebaEmail('angel15bg@homtail.com')
    True

    >>> compruebaEmail('angel15bg@homt@ail.com')
    False

    >>> compruebaEmail('angel15bghomtail.com@')
    False

    """
    numarroba = emailUsuario.count('@')
    #print(numarroba)
    
    longitud = len(emailUsuario)
    #print(longitud)
    
    if((numarroba > 0 and numarroba < 2) and (emailUsuario.find('@') != 0) and (emailUsuario.rfind('@') != longitud-1)):
        return True
    else:
        return False
    

'''   	
x = "angel@hotmail.com"
v = x.rfind('@')
print(v)
'''
# print(areaTriangulo(10,5))
#doctest.testmod()
#compruebaEmail('angel15bg@homtail.com')


valor = "holaaaa"
x = valor.count()
print(x)