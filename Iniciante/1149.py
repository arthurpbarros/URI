valores = input().split()
#Convert values from string to int
for i in range(len(valores)):
    valores[i] = int(valores[i])

a = valores[0] 
b = 0
valid = False
while (not valid):
    for val in valores[1:]:
        if(val > 0):
            b = val
            valid = True

soma = 0
for val in range(a,a+b,1):
    soma += val
print (soma)
