def is_perfect(n):
    divisores = []
    if (n != 1):
        divisores.append(1)
    met = n//2
    for i in range(2,met+1):
        if(n%i == 0):
            divisores.append(i)
    
    soma = sum(divisores)
    #print (soma,n,divisores)
    return (soma == n)

n = int(input())
for i in range(n):
    num = int(input())
    if (is_perfect(num)):
        print (num,"eh perfeito")
    else:
        print (num,"nao eh perfeito")