cod,qnt = input().split()
cod = int(cod)
qnt = int(qnt)

total = 0.0
if (cod == 1):
    total = 4.0 * qnt
elif (cod == 2):
    total = 4.5 * qnt
elif (cod == 3):
    total = 5.0 * qnt
elif (cod == 4):
    total = 2.0 * qnt
elif (cod == 5):
    total = 1.5 * qnt

print ("Total: R$","{:.2f}".format(total))
