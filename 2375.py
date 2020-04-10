diameter = int(input())
l,h,p = input().split(" ")
l = int(l)
h = int(h)
p = int(p)

if (diameter <= l and diameter <= h and diameter <= p):
    print ("S")
else:
    print ("N")