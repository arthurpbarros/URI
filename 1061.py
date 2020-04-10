str1,d1 = input().split()
d1 = int (d1)
h1,m1,s1 = input().split(" : ")
h1 = int(h1)
m1 = int(m1)
s1 = int(s1)
str2,d2 = input().split()
d2 = int(d2)
h2,m2,s2 = input().split(" : ")
h2 = int(h2)
m2 = int(m2)
s2 = int(s2)

t1 = h1*3600 + m1*60 + s1
t2 = (d2-d1)*3600*24 + h2*3600 + m2*60 + s2

total_seg = t2-t1
print (total_seg//(24*3600),"dia(s)")
total_seg %= (24*3600) #Without the days
print (total_seg//3600,"hora(s)")
total_seg %= 3600 #Without the hours
print (total_seg//60,"minuto(s)")
total_seg %= 60 #Without the minutes
print (total_seg,"segundo(s)")