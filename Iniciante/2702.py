f,b,m = input().split()
f = int (f)
b = int (b)
m = int (m)
rf,rb,rm = input().split()
rf = int (rf)
rb = int (rb)
rm = int (rm)

total = 0
if (rf > f):
    total += rf-f
if (rb > b):
    total += rb-b
if (rm > m):
    total += rm-m

print (total)
