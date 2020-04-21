t = int(input())
comb = [0,0,0]
while (t != 4):
	if(1 <= t <= 3):
		comb[t-1] += 1
	t = int(input())

print ("MUITO OBRIGADO")
print ("Alcool:",comb[0])
print ("Gasolina:",comb[1])
print ("Diesel:",comb[2])
