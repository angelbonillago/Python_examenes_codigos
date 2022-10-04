A=int(input("ingrese un numero\n"))
B=int(input("ingrese otro numero\n"))
C=int(input("ingrese un nuemero\n"))
D=int(input("ingrese un nuemero\n"))
if(A > B and A > C and A > D):
    X=A
else:
    if(B > A and B > C and B > D):
        X=B
    else:
        if(C > A and C > B and C > D):
            X=C
        else:
            X=D

if(A < B and A < C and A < D):
    Y=A
else:
    if(B < A and B < C and B < D):
        Y=B
    else:
        if(C < A and C < B and C < D):
            Y=C
        else:
            Y=D

            
print("el mayor es "+str(X)+" y el menor es "+str(Y))