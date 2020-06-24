def semi_full(vetor): # return True if vetor is semifull
    return (True if (len(vetor) == 4) else False)

def even(ele): # return True if element is even
    return (True if (ele%2 == 0) else False)

def print_v(vetor): # print contend of vetor
    for i in range(len(vetor)): # For generic size of vetor, five or less 
        if (even(vetor[0])):
            print ("par[{}] = {}".format(i,vetor[i]))
        else:
            print ("impar[{}] = {}".format(i,vetor[i]))
    vetor.clear()

def add(vetor,ele): # add ele in vector
    if (semi_full(vetor)):
        vetor.append(ele)
        print_v(vetor)
    else:
        vetor.append(ele)
par = []
impar = []

for i in range(15):
    n = int(input())
    if (even(n)):
        add(par,n)
    else:
        add(impar,n)

print_v(impar)
print_v(par)
