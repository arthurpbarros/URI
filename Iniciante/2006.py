tea = int(input())
t1,t2,t3,t4,t5 = input().split()
t1 = int(t1)
t2 = int(t2)
t3 = int(t3)
t4 = int(t4)
t5 = int(t5)

right = 0
if (t1 == tea):
    right += 1
if (t2 == tea):
    right += 1
if (t5 == tea):
    right += 1
if (t4 == tea):
    right += 1
if (t3 == tea):
    right += 1

print (right)