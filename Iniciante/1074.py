n = int(input())
values = []
for i in range (1,n+1):
	values.append(int(input()))
	
for number in values:
	text = ""
	if (number == 0):
		text += "NULL"
	else:
		if (number%2 ==0):
			text += "EVEN"
		else:
			text += "ODD"
		if (number > 0):
			text += " POSITIVE"
		else:
			text += " NEGATIVE"

	print (text)
