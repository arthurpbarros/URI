valor = float(input())

print("NOTAS:")
notas100 = int(valor//100)
valor %= 100
print(notas100,"nota(s) de R$ 100.00")
notas50 = int(valor//50)
valor %= 50
print(notas50,"nota(s) de R$ 50.00")
notas20 = int(valor//20)
valor %= 20
print (notas20,"nota(s) de R$ 20.00")
notas10 = int(valor//10)
valor %= 10
print (notas10,"nota(s) de R$ 10.00")
notas5 = int(valor//5)
valor %= 5
print (notas5,"nota(s) de R$ 5.00")
notas2 = int(valor//2)
valor %= 2
print (notas2,"nota(s) de R$ 2.00")
print ("MOEDAS:")
valor *= 100
moeda1 = int(valor//100)
valor %= 100
print (moeda1,"moeda(s) de R$ 1.00")
moeda50 = int(valor//50)
valor %= 50
print (moeda50,"moeda(s) de R$ 0.50")
moeda25 = int(valor//25)
valor %= 25
print (moeda25,"moeda(s) de R$ 0.25")
moeda10 = int(valor//10)
valor %= 10
valor = (valor+0.1)
#print (int(valor+0.1))
print (moeda10,"moeda(s) de R$ 0.10")
moeda5 = int(valor//5)
valor %= 5
print (moeda5,"moeda(s) de R$ 0.05")
moeda01 = int(valor//1)
print (moeda01,"moeda(s) de R$ 0.01")
