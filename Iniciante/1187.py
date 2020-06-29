def soma(m):
    soma = 0
    for i in range(0,5):
        for j in range(i+1,11-i):
            soma += m[i][j]
    
    return soma
    
def media(m):
    soma = 0
    cont = 0
    for i in range(0,5):
        for j in range(i+1,11-i):
            soma += m[i][j]
            cont+=1
            
    return soma/cont


matriz = []
op = str(input())
for i in range(12):
    l = []
    for j in range(12):
        l.append(float(input()))
    matriz.append(l)

if(op == "S"):
    print ("{:.1f}".format(soma(matriz)))
elif (op == "M"):
    print ("{:.1f}".format(media(matriz)))
