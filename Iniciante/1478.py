def cria_linha_cres(ini,m):
    for i in range(ini,m,1):
        if (i < m-1):
            print (str(i).rjust(3),end=" ")
        else:
            print (str(i).rjust(3),end="\n")

def cria_linha_decres(ini,total):
    for ini in range(ini,0,-1):
        if (ini == 1 and total):
            print (str(ini).rjust(3),end="\n")
        else:
            print (str(ini).rjust(3),end=" ")
            
def cria_matriz(n):
    for i in range(1,n+1,1):
        if (i == 1):
            cria_linha_cres(i,n+1)
        elif (i == n):
            cria_linha_decres(i,True)
        else:
            cria_linha_decres(i,False)
            cria_linha_cres(2,2+n-i)
            
        
        
n = int(input())
while (n > 0):
    cria_matriz(n)
    print ()
    n = int(input())