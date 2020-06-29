def soma_impares(inicio,qnt):
    # 5 7 9 11 13
    
    
    soma = 0
    i = 0
    while (i < qnt):
        soma += inicio
        inicio += 2
        i += 1
    print (soma)


n = int(input())
for i in range(n):
    num,qnt = map(int,input().split())
    if (num%2 == 0):
        soma_impares(num+1,qnt)
    else:
        soma_impares(num,qnt) 