c,d = input().split(" ")
c_km,valor_p = input().split(" ")
c,d,c_km,valor_p = int(c),int(d),int(c_km),int(valor_p)

total = c*c_km + c//d * valor_p
print (total)
	
