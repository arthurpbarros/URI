def troca_extremos(n):
    s = len(n)
    for i in range(s//2):
        troca = n[i]
        n[i] = n[s-1-i]
        n[s-1-i] = troca

    ind = 0
    for i in numeros:
        print ("N["+str(ind)+"] = "+str(i))
        ind += 1
        
        
numeros = []
for i in range(20):
    n = int(input())
    numeros.append(n)

troca_extremos(numeros)
