n = int(input())
rows = []
for i in range(0,n):
	a,b = input().split()
	a = float(a)
	b = float(b)

	if (b == 0):
		rows.append("divisao impossivel")
	else:
		rows.append((a/b)) 

for i in range(0,n):
	print (rows[i])
