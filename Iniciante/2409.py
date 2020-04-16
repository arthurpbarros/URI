a,b,c = input().split()
h,l = input().split()
a = int(a)
b = int(b)
c = int(c)
h = int(h)
l = int(l)

#Any two dimensions are lower than h,l
if(b <= h and c <= l) or (c <= h and b <= l) or (c <= h and a <= l) or (a <= h and c <= l) or (a <= h and b <= l) or (b <= h and a <= l):
    print ("S")
else:
    print ("N")