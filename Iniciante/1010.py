total = 0
read = 0
while(read < 2):
    cod,qnt,price = input().split(" ")
    qnt = int(qnt)
    price = float(price)
    total += qnt*price
    read += 1

print("VALOR A PAGAR: R$","{:.2f}".format(total))
