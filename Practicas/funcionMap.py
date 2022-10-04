def cuadrado(n,m):
	return n+m

l=[1,2,3,4]
t = (9,8,7,6)
lr=map(cuadrado,l,t)

print(l)
print(t)
print(*lr)