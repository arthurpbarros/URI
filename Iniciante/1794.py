n = int(input())
la,lb = input().split()
sa,sb = input().split()

la = int(la)
lb = int(lb)
sa = int(sa)
sb = int(sb)

if (n >= la and n >= sa and n <= lb and n <= sb):
    print ("possivel")
else:
    print ("impossivel")