n = int(input())
for i in range(n):
	x,y = map(int,input().split())
	soma = 0
	if (x <= y):
		for n in range(x+1,y,1):
			if (n%2 == 1):
				soma += n
	else:
		for n in range(y+1,x,1):
			if (n%2 == 1):
				soma += n
	print (soma)
