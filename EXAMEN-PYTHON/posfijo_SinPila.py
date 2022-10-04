print('51563*-1623^/+2*+')
#lista = ['5', '15', '6', '3', '*', '-', '16','2', '3', '^', '/', '+', '2', '*', '+']
lista = ['7','3','2','^','-','9','5','-','4','*','+'    ,'20','-','5','+']

operadores = ["^", "/", "*", "+", "-", "(", ")"]
i = 0
r = 0
j = 0
pila = []
for j in lista:

    if j in operadores:
        n1 = float(pila[len(pila) - 2])
        n2 = float(pila[len(pila) - 1])
 
        if j == "+":
            r = n1 + n2
 
        if j == "-":
            r = n1 - n2
 
        if j == "*":
            r = n1 * n2
 
        if j == "/":
            r = n1 / n2
 
        if j == "^":
            r = n1 ** n2
 
        pila[len(pila) - 2] = r
        pila.pop(len(pila) - 1)
    else:
        pila.append(j)
 
        i = i + 1
 
#return pila
print("RESULTADO : ",pila )




if __name__ == '__main__':
    pass
