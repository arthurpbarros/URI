n = int(input())
k = int(input())
comp = []

for i in range(n):
    num = int(input())
    comp.append(num)
    
comp.sort(reverse=True)
m = max(comp)
comp_m = comp.count(m)
vagas = comp_m
if (vagas < k):
    while (vagas < k):
        proximo_m = comp[comp_m]
        comp_m = comp.count(proximo_m)
        vagas += comp_m

print (vagas)
        
