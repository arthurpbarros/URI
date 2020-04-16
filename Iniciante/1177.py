n = int(input())
t = list(range(0,1000,1))
for i in range(0,1000):
    t[i] = i%n

for i in range(0,1000):
    print ("N[",i,"] = ",t[i],sep="")
