x,y = map(int,input().split())
for c in range(1,y+1,x):
    for i in range(x):
        if (i == x-1):
            print (c+i)
        else:
            print (c+i,"",end="")
            
