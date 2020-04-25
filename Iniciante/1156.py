s = 0.0
n = 1
den = 1
while (n <= 39):
   s += n/den
   n += 2
   den *= 2

print ("{:.2f}".format(s))
