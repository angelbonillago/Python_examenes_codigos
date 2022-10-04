
def showCadena(valor):
	linea = ""
	for x in range(valor):
		linea=linea+repr(x+1)
	print(linea)

if __name__ == '__main__':
    n = int(input())
    showCadena(n)


