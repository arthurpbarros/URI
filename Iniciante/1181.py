row_select = int(input())
operation = input()
soma = 0.0
for j in range(12):
    for i in range(12):
        num = float(input())
        if (j == row_select):
            soma += num

if (operation == "S"):
    print ("{:.1f}".format(soma))
else:
    print ("{:.1f}".format(soma/12))
