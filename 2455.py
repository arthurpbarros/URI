p1,c1,p2,c2 = input().split()
p1 = int(p1)
p2 = int(p2)
c1 = int(c1)
c2 = int(c2)

le = p1*c1
ld = p2*c2
if (le == ld):
    print (0)
elif (le > ld):
    print (-1)
else:
    print (1)
