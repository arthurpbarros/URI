while True:
    n = int(input())
    if (n == 0):
        break
    else:
        soma = 0
        if (n%2 == 0):
            for i in range(n,n+9,2):
                soma += i
            print (soma)    
        else:
            for i in range(n+1,n+10,2):
                soma += i
            print (soma)
            