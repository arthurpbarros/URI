a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)

maior = a
if (b > maior):
    maior = b
if (c > maior):
    maior = c

prod = maior*maior
if(a < b+c and b < a+c and c < a+b):
    if (maior == a):
        p1 = b*b
        p2 = c*c
    elif (maior == b):
        p1 = a*a
        p2 = c*c
    else: #(maior == c):
        p1 = a*a
        p2 = b*b

    if(prod == p1+p2):
        print ("r")
    elif(prod > p1+p2):
        print ("o")
    else:
        print ("a")
else:
    print ("n")
