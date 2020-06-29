def soma(matriz):
    soma = 0.0
    for i in range(11): 
        for j in range(i+1,12,1):
            soma += matriz[i][j]
            
    return soma

def media(matriz):
    cont = 0
    media = 0.0
    for i in range(11):
        for j in range(i+1,12,1):
            media += matriz[i][j]
            cont+=1   
    return (media/cont)

op = str(input())
matriz = []
for i in range(12):
    l = []
    for j in range(12):
        n = float(input())
        l.append(n)
    matriz.append(l)
    
if(op == 'S'):
    print ("{:.1f}".format(soma(matriz)))
elif (op == 'M'):
    print ("{:.1f}".format(media(matriz)))
    
    