x = int(input())
y = int(input())
if (x <= y):
    for n in range(x+1,y,1):
        if n%5 == 2 or n%5==3:
            print (n)
else:
    for n in range(y+1,x,1):
        if n%5 == 2 or n%5==3:
            print (n)
