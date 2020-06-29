v = int(input())
vetor = []

for i in range(10):
    vetor.append(v)
    v *= 2
    
for i in range(10):
    print ("N["+str(i)+"] = "+str(vetor[i]))    