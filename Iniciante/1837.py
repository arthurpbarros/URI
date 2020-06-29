a,b = map(int,input().split())
for r in range(0,abs(b),1):
    if (a-r)%b == 0:
        q = (a-r)//b
        break
    
print (q,r)