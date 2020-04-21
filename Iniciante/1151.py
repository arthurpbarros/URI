n = int(input())
a = 0
b = 1
for i in range(1,n+1,1):
    if (i == 1):
        print (a) if n == 1 else print (a,end=" ")
    elif (i == 2):
        print (b) if n == 2 else print (b,end=" ")
    else:
        total = a + b
        a = b
        b = total
        print (total) if i == n else print (total,end=" ")
    
