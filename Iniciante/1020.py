days = int(input())

y = days//365
days %= 365
m = days//30
days %= 30

print (y,"ano(s)")
print (m,"mes(es)")
print (days,"dia(s)")
