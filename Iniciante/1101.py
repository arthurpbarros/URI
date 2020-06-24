m,n = map(int,input().split())
while (m > 0 and n > 0):
    soma = 0
    if (m <= n):
        for num in range(m,n+1):
            print (num,"",end="")
        soma = ((m+n)*(n-m+1))/2
    else:
        for num in range(n,m+1):
            print (num,"",end="")
        soma = ((m+n)*(m-n+1))/2
    print("Sum=",int(soma),sep="")
    m,n = map(int,input().split())
    
        
