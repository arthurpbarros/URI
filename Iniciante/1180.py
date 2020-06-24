t = int(input())
val = input().split()

menor = 0
pos = 0
i = 0
for str_num in val:
    n = int(str_num)
    if (i == 0):
        menor = n
    else:
        if (n < menor):
            menor = n
            pos = i
    i+=1


print ("Menor valor:",menor)
print ("Posicao:",pos)
