qnt = int(input())
nomes = []
values = []
for i in range(0,qnt):
	nome1,op1,nome2,op2 = input().split()
	v1,v2 = input().split()
	v1 = int(v1)
	v2 = int(v2)
	values.append({"v1" : v1,"v2" : v2})
	nomes.append({"nome" : nome1, "opcao": op1,"nome2" : nome2,"opcao2": op2})

for i in range(0,qnt):
	soma = values[i]["v1"]+values[i]["v2"] 
	if(soma%2 == 0):
		if(nomes[i]["opcao"] == "PAR"):
			print (nomes[i]["nome"])
		else:
			print (nomes[i]["nome2"])
	else:
		if(nomes[i]["opcao"] == "IMPAR"):
			print (nomes[i]["nome"])
		else:
			print (nomes[i]["nome2"])