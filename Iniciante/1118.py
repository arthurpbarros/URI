correct = 0
soma = 0.0
while (True):
    x = float(input())
    if (x < 0.0 or x > 10):
        print ("nota invalida")
    else:
        soma += x
        if (correct == 1):
            print ("media = {:.2f}".format(soma/2))
            soma = 0
            correct = 0
            print ("novo calculo (1-sim 2-nao)")
            x = float(input())
            while (x < 1.0 or x > 2.0):
                print ("novo calculo (1-sim 2-nao)")
                x = float(input())
            else:
                if (x == 2.0):
                    break
        else:
            correct += 1
