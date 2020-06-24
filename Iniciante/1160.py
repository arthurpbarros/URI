from math import floor

casos = int(input())
for i in range(casos):
    pa,pb,ga,gb = input().split()
    pa = int(pa)
    pb = int(pb)
    ga = float(ga)
    gb = float(gb)

    anos = 0
    while (pa <= pb and anos <= 100):
        pa = floor((1+ga/100)*pa)
        pb = floor((1+gb/100)*pb)
        anos += 1
        
    if(anos > 100):
        print ("Mais de 1 seculo.")
    else:
        print (anos," anos.",sep="")
