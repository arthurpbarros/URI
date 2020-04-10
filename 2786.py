l = int(input())
c = int(input())

type1_total = (l*c)/0.5
type1 = l*c + (l-1)*(c-1)
type2 = ((type1_total - type1) - 1)*2

print (type1)
print (int(type2))

'''
15/0.5 = 30 tipo 1
30 tipo 1 - 23 tipo 1 = 7 tipo 1
7 tipo 1 - 1 tipo 1 = 6 tipo 1
6 tipo 1 * 2
'''
