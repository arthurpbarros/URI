d1,d2 = input().split()
d1 = int(d1)
d2 = int(d2)

if (d2 >= 0 and d2 <= 2):
    print ("nova")
elif (d2 >= 3 and d2 <= 96):
    if (d1 <= d2):
        print ("crescente")
    else:
        print ("minguante")
else: #(d2 >= 97 and d2 <= 100):
    print ("cheia")
