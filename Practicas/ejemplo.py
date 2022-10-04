

def is_leap(year):
    leap = False
    auxiliar=0
    auxiliar2 = 0
    if year>=1900 and year<pow(10,5):

        if (year % 4 == 0):
            auxiliar = year/100
            auxiliar2 = int(year/100)

            if auxiliar2 == auxiliar:
                auxiliar = year/400
                auxiliar2 = int(year/400)
                if auxiliar2==auxiliar:
                    leap=True
    return leap
    

    


year = int(input())
print(is_leap(year))


"""
num = 1992/100
print(num)
valor = int(num)
print(valor)
"""
