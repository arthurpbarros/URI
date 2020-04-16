renda = float(input())
ir = 0.00
renda_faixa = renda
if (renda <= 2000):
	print ("Isento")
else:
	renda_faixa -= 2000
	if (renda_faixa <= 1000): #ate 3000
		ir += renda_faixa*0.08
	else:
		ir += 1000*0.08
		renda_faixa -= 1000
		if(renda_faixa <= 1500): #ate 4500
			ir += renda_faixa*0.18
		else:
			ir += 1500*0.18
			renda_faixa -= 1500
			ir += renda_faixa*0.28
	print ("R$ "+"{:.2f}".format(ir))







# if (rent <= 3000.00):
# 	rent -= 2000.00
# 	print ("R$ ","{:.2f}".format(rent*0.08))
# elif (rent <= 4500.00):
# 	rent -= 3000.00
# 	print ("R$ ","{:.2f}".format(rent*0.18))
# else:
# 	rent -= 4500
# 	print ("R$ ","{:.2f}".format(rent*0.28))