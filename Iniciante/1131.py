op = 1
v_int = v_gre = emp = 0
grenais = 0
    
while (op != 2):
    p_int, p_gre = map(int, input().split())
    print ("Novo grenal (1-sim 2-nao)")
    grenais += 1
    
    op = int(input())
    if (p_int > p_gre):
        v_int += 1
    elif (p_gre > p_int):
        v_gre += 1
    else:
        emp += 1

print (grenais,"grenais")
print ("Inter:"+str(v_int))
print ("Gremio:"+str(v_gre))
print ("Empates:"+str(emp))
if (v_int > v_gre):
    print ("Inter venceu mais")
elif (v_gre > v_int):
    print ("Gremio venceu mais")
else:
    print ("Nao houve vencedor")
    
