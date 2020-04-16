a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)
if (a == b or a == c or b == c or a==b+c or b==a+c or c==a+b):
    print ("S")
else:
    print ("N")
