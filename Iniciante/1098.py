i = 0
count = 0
while (i <= 2):
    j = 1
    while (j <= 3):
        if (count%5 == 0):
            print ("I=",int(i+0.1),sep="",end=" ")
            print ("J=",int(i+j+0.1),sep="")
        else:
            print ("I={:.1f}".format(i),sep="",end=" ")
            print ("J={:.1f}".format(i+j),sep="")
        j+=1
    i+=0.2
    count += 1
