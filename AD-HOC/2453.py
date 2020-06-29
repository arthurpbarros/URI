
palavras = input().split()
traducao = ""
for i in range(len(palavras)):
	max_i = len(palavras)-1
	palavra_atual = palavras[i]
	letras_p = list(palavra_atual)

	j = 0
	for a in letras_p:
		if (j%2 == 1):
			traducao += a
		j+=1

	if (i != max_i):
		traducao += " "

print (traducao)