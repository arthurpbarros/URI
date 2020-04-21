t = int(input()) 
while (t > 0):
    for i in range(1,t+1,1):
        print (i) if i==t else print(i,end=" ")
    t = int(input())
