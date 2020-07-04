l,c =map(int,input().split())
m = list()
for i in range(l):
    x = input().split()
    m.append(x)

l1 = 0
c1 = 0

for i in range(1,l-1):
    for j in range(1,c-1):
        if m[i][j] == '42':
            if m[i-1][j-1:j+2]==m[i+1][j-1:j+2]==['7','7','7']:
                if m[i][j-1]==m[i][j+1]=='7':
                    l1=i + 1
                    c1=j + 1

print(l1,c1)