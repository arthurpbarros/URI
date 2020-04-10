valor = int(input())
print (valor)
#print("NOTAS:")
notas100 = int(valor//100)
valor %= 100
print(notas100,"nota(s) de R$ 100,00")
notas50 = int(valor//50)
valor %= 50
print(notas50,"nota(s) de R$ 50,00")
notas20 = int(valor//20)
valor %= 20
print (notas20,"nota(s) de R$ 20,00")
notas10 = int(valor//10)
valor %= 10
print (notas10,"nota(s) de R$ 10,00")
notas5 = int(valor//5)
valor %= 5
print (notas5,"nota(s) de R$ 5,00")
notas2 = int(valor//2)
valor %= 2
print (notas2,"nota(s) de R$ 2,00")
print (valor,"nota(s) de R$ 1,00")
