def eh_primo(n):
	if (n <= 1):
		return False
	else:
		for i in range(2,n+1,1):
			if (n%i == 0 and i!=n):
				return False
		return True

n = int(input())
for i in range(n):
	num = int(input())
	if (eh_primo(num)):
		print (num,"eh primo")
	else:
		print (num,"nao eh primo")
