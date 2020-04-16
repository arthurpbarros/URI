notas_val = 0
soma = 0.0
while (notas_val < 2):
    nota = float(input())
    if (nota >= 0.0 and nota <= 10.0):
        notas_val += 1
        soma += nota
    else:
        print ("nota invalida")

print ("media =","{:.2f}".format(soma/2))
        
