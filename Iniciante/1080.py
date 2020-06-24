maximum = int(input())
pos_max = 1
for i in range(2,101):
    num = int(input())
    if (num > maximum):
        maximum = num
        pos_max = i

print (maximum)
print (pos_max)
