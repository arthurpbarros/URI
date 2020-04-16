n = int(input())
medias = []
for i in range (1,n+1):
	medias.append(input())

for i in range(0,n):
	a,b,c = medias[i].split()
	a = float(a)
	b = float(b)
	c = float(c)
	media = (a*2+b*3+c*5)/10
	print("{:.1f}".format(media))