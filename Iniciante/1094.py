c = 0
r = 0
s = 0

n = int(input())
for i in range (n):
    qnt, typing = input().split(" ")
    qnt = int(qnt)
    if (typing == "S"):
        s += qnt
    elif (typing == "C"):
        c += qnt
    elif (typing == "R"):
        r += qnt

total = c+r+s
print ("Total:",total,"cobaias")
print ("Total de coelhos:",c)
print ("Total de ratos:",r)
print ("Total de sapos:",s)
print ("Percentual de coelhos: {:.2f} %".format(c*100/total))
print ("Percentual de ratos: {:.2f} %".format(r*100/total))
print ("Percentual de sapos: {:.2f} %".format(s*100/total))
