n = int(input())
total = 7
if (n > 100):
    total += 20+70*2 + 5*(n-100)
else:
    if (n > 30):
        total += 20 + 2*(n-30)
    else:
        if (n > 10):
            total += n-10

print (total)
