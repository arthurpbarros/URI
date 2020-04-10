a1 = int(input())
a2 = int(input())
a3 = int(input())

total = 0
mac_1 = a2*2+a3*4
mac_2 = a1*2+a3*2
mac_3 = a1*4+a2*2

if(mac_1 <= mac_2 and mac_1 <= mac_3):
    print (mac_1)
elif (mac_2 <= mac_1 and mac_2 <= mac_3):
    print (mac_2)
else:
    print (mac_3)