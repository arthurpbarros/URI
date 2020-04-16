i = 0
while (input().strip() != "0 0"):
	i += 1
	praia,sor = input().split()
	praia = int(praia)
	sor = int(sor)
	for i in range(0,sor):
		x1,x2 = input().split()
		x1 = int(x1)
		x2 = int(x2)
		if (i == 0):
			minimo, maximo = x1,x2
		else:
			if(minimo < x1 and x2 > maximo):
				maximo = x2
			if(x1 < minimo and x2 > maximo):
				minimo = x1
				maximo = x2
			if(x1 < minimo and maximo > x2):
				minimo = x1
	print ("Teste",i)
