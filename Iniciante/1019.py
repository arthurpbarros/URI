total = int(input())
h = total//3600
total %= 3600
m = total//60
total %= 60

print (str(h)+":"+str(m)+":"+str(total))
