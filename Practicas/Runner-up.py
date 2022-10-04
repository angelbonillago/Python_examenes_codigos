
def runner_up(n,arr):
	
	if (n>=2 and n<=10) :
		valor=0
		for x in arr:
			if(not(x>=-100 and x<=100)):
				valor=1
		if(valor ==0):
			#Iteramos para no tener puntajes iguales
			contador=0
			max_item = max(arr)
			for x in arr:
				if(max_item==x):
					contador=contador+1

			if(contador==0):
				arr.remove(max_item)
				max_item=max(arr)
				print(max_item)
			else:
				for x in range(contador):
					arr.remove(max_item)
					max_item=max(arr)
				print(max_item)				

	else:
		print("salir")

"""
def runner_up(arr):

	max_valor = max(arr)
	print(max_valor)
"""
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    runner_up(n,arr)